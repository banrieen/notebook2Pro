#include "pch.h"
#include "SysInfo.h"
#include "BasementAlgorithms.h"
#include "ClassicProblems.h"

using namespace winrt;
using namespace Windows::Foundation;

void HelloDatetime();
void RandomNum();

int main()
{
    init_apartment();
    Uri uri(L"http://aka.ms/cppwinrt");
    printf("Hello, %ls!\n", uri.AbsoluteUri().c_str());

    HelloDatetime();
    RandomNum();
    system("PAUSE");
}


void HelloCpu()
{
    /** Call cpuinfo print function !
        运行一个实例影响本机 CPU 的使用率曲线！
    */
    CpuInfo localCI;
    localCI.SimpleCpuUsrageLine();
}

void HelloDatetime()
{
    /** 基本的年月日处理
    1. 给定年份判断其有多少天
    */
    AboutDatetime localDT;
    localDT.DaysOfYear();
}

void NormalSort()
{
    /** 基础查找和排序算法
    */
    int array[] = { 34,65,12,43,67,5,78,10,3,70 };
    int len = sizeof(array) / sizeof(int);
    int low, high;
    low = 0;
    high = len - 1;

    SortAndQuery BASort;
    std::cout << "The orginal array are: \n";
    BASort.display(array, len);
    //mergeSort(array, low, high);
    BASort.QuickSort(array, low, high);
    std::cout << "The sorted arrayare: ";
    BASort.display(array, len);
}

void RandomNum()
{
    /** 生成随机数
    */
    RandomNumber rn;
    rn.RandomInt();
}