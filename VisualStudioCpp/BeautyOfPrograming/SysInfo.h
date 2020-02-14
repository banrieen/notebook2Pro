#pragma once
#include <iostream>
#include <windows.h>
#include <stdlib.h>
#include <math.h>

class CpuInfo
{

public:
	CpuInfo();
	~CpuInfo();
	void SimpleCpuUsrageLine();
	void sin_line(int argc, char* argv[]);
	void CSimpleCpuUsrageLine();
};


class AboutDatetime
{
public:
	AboutDatetime();
	~AboutDatetime();
	int DaysOfYear();
};