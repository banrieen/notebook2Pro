#include "pch.h"
#include "SysInfo.h"

#define GetCPUTictCount() _rdtsc()

CpuInfo::CpuInfo()
{
}

CpuInfo::~CpuInfo()
{
}

void CpuInfo::SimpleCpuUsrageLine()
{
	CONST DWORD busyTime = 100;
	CONST DWORD idleTime = busyTime;
	std::cout << "Hello Cpu !\n";
	DWORD startTime = 0;
	while (true)
	{
		startTime = GetTickCount64();
		// Do busy loop
		while ((GetTickCount64() - startTime) < busyTime)
			;
		Sleep(idleTime);
	}
}

void CpuInfo::CSimpleCpuUsrageLine()
{
	std::cout << "通过CPU频率，计算CPU在1s内可执行的命令，以及休眠时间模拟使用量！";
	for (; ; )
	{
		for (float i = 0.0; i < 9600000000000000; i++)
		{
			GetTickCount64();
			Sleep(10);
		}
	}
}


void CpuInfo::sin_line(int argc, char* argv[])
{
	char cpuInfo[] = "";

	// Make task manager fenerate sine graph
	const int SAMPLING_COUNT = 200;
	const double PI = 3.1415926535;
	const int TOTAL_AMPLITUDE = 300;
	DWORD busySpan[SAMPLING_COUNT];
	int amplitude = TOTAL_AMPLITUDE / 2;
	double radian = 0.0;
	double radianIncrement = 2.0 / (double)SAMPLING_COUNT;
	for (int i = 0; i < SAMPLING_COUNT; i++)
	{
		busySpan[i] = (DWORD)(amplitude + (sin(PI * radian) * amplitude));
		radian += radianIncrement;
		printf("%d\t%d\n", busySpan[i], TOTAL_AMPLITUDE - busySpan[i]);

	}
	DWORD startTime = 0;
	for (int j = 0; ; j = (j + 1) % SAMPLING_COUNT)
	{
		startTime = GetTickCount64();
		while ((GetTickCount64() - startTime) <= busySpan[j])
			;
		Sleep(TOTAL_AMPLITUDE - busySpan[j]);
	}

}

AboutDatetime::AboutDatetime()
{
}

AboutDatetime::~AboutDatetime()
{
}

int AboutDatetime::DaysOfYear()
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
	printf("请输入年份以便计算该年总天数： \n");
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
	printf("%d 年共有 %d 天\n", year, days);
	return 0;
}
