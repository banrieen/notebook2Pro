#include "BeautyOfPrograming.h"
#include <iostream>
#include <windows.h>
#include <stdlib.h>
#include <math.h>

#define GetCPUTictCount() _rdtsc()

using namespace std;

void BeautyOfPrograming::CpuUserage()
{
	CONST DWORD busyTime = 100;
	CONST DWORD idleTime = busyTime;
	std::cout << "Hello Cpu !\n";
	INT64 startTime = 0;
	while (true)
	{
		DWORD startTime = GetTickCount();
		// Do busy loop
		while ((GetTickCount() - startTime) < busyTime)
			;
		Sleep(idleTime);
	}

}

void BeautyOfPrograming::SimpleCpuUsrageLine()
{
	std::cout << "通过CPU频率，计算CPU在1s内可执行的命令，以及休眠时间模拟使用量！";
	for (; ; )
	{
		for (int i = 0; i < 9600000000000000; i++)
		{
			GetTickCount64()
				;
			Sleep(10);
		}
	}
}


int BeautyOfPrograming::sin_line(int argc, char *argv[])
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
		startTime = GetTickCount();
		while ((GetTickCount() - startTime) <= busySpan[j])
			;
		Sleep(TOTAL_AMPLITUDE - busySpan[j]);
	}

	return 0;
}
