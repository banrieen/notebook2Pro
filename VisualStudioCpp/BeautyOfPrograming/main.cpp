# include <stdio.h>

void pause()
{
	int j;
	printf("\n psrint '0' to quit !\n");
	scanf_s("%d", &j);
}

void main()
{
	int i, a[10];
	for (i=0; i<=9; i++)
		scanf_s("%d", &a[i]);
	for (i = 9; i >=0; i--)
		printf("%4d", a[i]);
	pause();
	printf("\n");
	// return 0;
}

