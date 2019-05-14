//Program
//	a p2p chat with select
//History
//	Xinspace	2 APRIL	First release
//
/*
use:
	client:  $./a.out server_ip_addr server_port
	server:	 $./a.out server_port
*/
#include "myhead.h"

#define BUFSIZE 512	//buf size

void *client_talk(void *);	//client part in this program
void *server_talk(void *);	//server part in this program

int main(int argc, char **argv)	
{
	if(3 == argc)	//argc == 3, instructing that this is client.
	{
		pthread_t tidc;
		pthread_create(&tidc, NULL, client_talk, (void *)argv);
		pthread_join(tidc, NULL);
	}
	else if(2 == argc)	//argc == 2, instructing that this is server
	{
		pthread_t tids;
		pthread_create(&tids, NULL, server_talk, (void *)argv);
		pthread_join(tids, NULL);
	}

	printf("in main!\n");
	
	return 0;
}

void *client_talk(void *arg)
{
	char **argu = (char **)arg;

	int connfd;
	struct sockaddr_in server;
	int port;
	int maxfd;
	int n;
	int nbytes;
	char buf[BUFSIZE];
	fd_set rdfs, ordfs;

	if(-1 == (connfd = socket(PF_INET, SOCK_STREAM, 0)))
		FUNW("socket");

	if(-1 == (port = atoi(argu[2])))
		FUNW("atoi");

	server.sin_family = PF_INET;
	server.sin_port = htons(port);
	inet_aton(argu[1], &(server.sin_addr));

	if(-1 == connect(connfd, (struct sockaddr *)(&server), sizeof(server)))
		FUNW("connect");

//	printf("connected to host:%s port:%s\n", inet_ntoa(server.sin_addr), htons(server.sin_port));

	FD_ZERO(&rdfs);
	FD_ZERO(&ordfs);
	FD_SET(connfd, &ordfs);	
	FD_SET(STDIN_FILENO, &ordfs);
	maxfd = connfd;	//connfd is the best file descriptor which in the rdfs(read file set)

	for(;;)
	{
		rdfs = ordfs;
		if(-1 == (n = select(maxfd + 1, &rdfs, NULL, NULL, NULL)))	//select function just monit read
		{
			FUNW("select");
		}
		else
		{
			if(FD_ISSET(connfd, &rdfs))	//if connfd is read-ready
			{
				if(-1 == (nbytes = read(connfd, buf, BUFSIZE)))
					FUNW("read");

				if(0 == strncasecmp(buf, "quit", 4))
				{
					printf("he quit!\npress any key to quit!\n");
					getchar();
					break;
				}

				fprintf(stdout, "%s.%u:%s\n", inet_ntoa(server.sin_addr), htons(server.sin_port), buf);

				memset(buf, 0, sizeof(buf));
			}
			else if(FD_ISSET(STDIN_FILENO, &rdfs))	//if stdin is read-ready
			{
				if(-1 == (nbytes = read(STDIN_FILENO, buf, BUFSIZE)))
					FUNW("read");

				if(0 == strncasecmp(buf, "quit", 4))
				{
					printf("you quit!\npress any key to quit!\n");
					getchar();
					sprintf(buf, "quit!\n");
					write(connfd, buf, strlen(buf));
					break;
				}

				buf[--nbytes] = 0;

				if(-1 == (nbytes = write(connfd, buf, strlen(buf))))
					FUNW("write");

				printf("I:%s\n", buf);

				memset(buf, 0, sizeof(buf));
			}
		}
	}

	close(connfd);

	return ((void *)NULL);
}

void *server_talk(void *arg)
{
	char **argu = (char **)arg;

	int listen_fd;
	int connfd;
	int maxfd;
	int port;
	struct sockaddr_in server;
	struct sockaddr_in client;
	int n;
	int nbytes;
	char buf[BUFSIZE];
	socklen_t addrlen;
	fd_set rdfs, ordfs;

	if(-1 == (listen_fd = socket(PF_INET, SOCK_STREAM, 0)))
		FUNW("socket");

	memset(&server, 0, sizeof(server));
	memset(&client, 0, sizeof(client));

	if(-1 == (port = atoi(argu[1])))
		FUNW("atoi");

	server.sin_family = PF_INET;
	server.sin_port = htons(port);
	server.sin_addr.s_addr = htonl(INADDR_ANY);

	if(-1 == bind(listen_fd, (struct sockaddr *)(&server), sizeof(server)))
		FUNW("bind");

	if(-1 == listen(listen_fd, 10))
		FUNW("listen");

	FD_ZERO(&rdfs);
	FD_ZERO(&ordfs);

	FD_SET(STDIN_FILENO, &ordfs);
	FD_SET(listen_fd, &ordfs);

	maxfd = listen_fd;

	addrlen = sizeof(client);

	for(;;)
	{
		rdfs = ordfs;
		if(0 > (n = select(maxfd + 1, &rdfs, NULL, NULL, NULL)))	//same as client_talk function's select
		{
			FUNW("select");
		}
		else
		{
			if(FD_ISSET(listen_fd, &rdfs))	//if listen_fd is read_ready, we can accept new connect
			{
				if(-1 == (connfd = accept(listen_fd, (struct sockaddr *)(&client), &addrlen)))
					FUNW("accept");

				maxfd = maxfd > connfd ? maxfd : connfd;	//if connfd is greater than maxfd, then change them

				FD_SET(connfd, &ordfs);	//insert the connfd to ordfs

				printf("connected to host:%s port:%u\n", inet_ntoa(client.sin_addr), htons(client.sin_port));
			}
			else if(FD_ISSET(STDIN_FILENO, &rdfs))
			{
				if(0 > (nbytes = read(STDIN_FILENO, buf, sizeof(buf))))
					FUNW("read");

				if(0 == strncasecmp(buf, "quit", 4))
				{
					printf("you quit!\npress any key to quit!\n");
					getchar();
					sprintf(buf, "quit!\n");
					write(connfd, buf, strlen(buf));
					break;
				}

				buf[--nbytes] = 0;

				printf("I:%s\n", buf);

				if(0 > (nbytes = write(connfd, buf, strlen(buf))))
					FUNW("write");

				memset(buf, 0, sizeof(buf));
			}
			else if(FD_ISSET(connfd, &rdfs))
			{
				if(0 > (nbytes = read(connfd, buf, sizeof(buf))))
					FUNW("read");

				if(0 == strncasecmp(buf, "quit", 4))
				{
					fprintf(stdout, "he quit!\npress any key to quit!\n");
					getchar();
					break;
				}

				printf("%s.%u:%s\n", inet_ntoa(client.sin_addr), htons(client.sin_port), buf);

				memset(buf, 0, sizeof(buf));
			}
		}
	}

	close(listen_fd);
	close(connfd);

	return ((void *)NULL);
}
