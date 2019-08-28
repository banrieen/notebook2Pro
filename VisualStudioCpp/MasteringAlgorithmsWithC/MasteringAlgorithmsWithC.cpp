// MasteringAlgorithmsWithC.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>
#include <Windows.h>
#include "BeautyOfPrograming.h" // 编程之美 试题
#include "OpenJudge.h"   // 北大 openjudge 试题

using namespace std;

int main()

{
	int rst = 0;

    std::cout << "Hello World!\n"; 
	char * tempChar[10];
	/* BeautyOfPrograming cu;
	cu.sin_line(1, tempChar);
	*/
	OpenJudge oj;
	rst = oj.DaysOfYear();
	

	Sleep(500); // 设置系统等待时间500ms

}


// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单
