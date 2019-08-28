#include "OpenJudge.h"
#include <Windows.h>
//#include <iostream>
using namespace std;

OpenJudge::OpenJudge()
{
}


OpenJudge::~OpenJudge()
{
}

int OpenJudge::DaysOfYear()
{
	/*
	计算天数。
    总时间限制:	1000ms  内存限制:10000kB
    描述：
	    输入年份，输出该年份有多少天
	输入：
		一行，一个整数
	输出
		一行，一个整数
	样例输入
	    2008
	样例输出
    366
	*/
	int year = 0;
	int days = 0;
	scanf_s("%d", &year);
	if (year % 400 == 0)
		days = 366;
	else
	{
		if (year % 4 == 0 && year % 100 != 0)
			days = 366;
		else
			days = 365;
	}
	printf("%d\n", days);
	// Sleep(100);
	return 0;
}


/* Openjude 提交实例
#include <iostream>
using namespace std;

int main()
{
	int year = 0;
	int days = 0;
	scanf_s("%d", &year); // 提交时改为 scanf
	if (year % 400 == 0)
		days = 366;
	else
	{
		if (year % 4 == 0 && year % 100 != 0)
			days = 366;
		else
			days = 365;
	}
	printf("%d\n", days);
	return 0;
}

int main_MOM() {
	int tzNum = 0;
	int i = 0;
	int tzPrices[10001];
	scanf("%d", &tzNum);
	//memset(tzPrices, 0, sizeof(tzPrices));
	for (int t = 0; t < tzNum; t++)
	{
		while (scanf("%f", &tzPrices[i]))
		{
			++i;
			if (i >= 5)
			{
				for (int j = 0; j <= i; j++)
				{
					if ((i - j) == 5)
					{
						printf("%f ", tzPrices[i] - tzPrices[j]);
					}
				}
			}

		}
		printf("\n");
	}
	return 0;
}

*/