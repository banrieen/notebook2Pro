// MasteringAlgorithmsWithC.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>
#include <Windows.h>
#include "BeautyOfPrograming.h"
using namespace std;
int main_DO();

int main()

{
    std::cout << "Hello World!\n"; 
	char * tempChar[10];
	main_DO();
	// BeautyOfPrograming cu;
	// cu.sin_line(1, tempChar);

}


// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单

// 入门提示: 
//   1. 使用解决方案资源管理器窗口添加/管理文件
//   2. 使用团队资源管理器窗口连接到源代码管理
//   3. 使用输出窗口查看生成输出和其他消息
//   4. 使用错误列表窗口查看错误
//   5. 转到“项目”>“添加新项”以创建新的代码文件，或转到“项目”>“添加现有项”以将现有代码文件添加到项目
//   6. 将来，若要再次打开此项目，请转到“文件”>“打开”>“项目”并选择 .sln 文件


/*
#include<stdio.h>
#include<string.h>
int main_ONN()
{
	int n, m;
	while (scanf_s("%d", &n) != EOF)
	{
		m = 0;
		for (int i1 = 0; i1 <= n; ++i1) {
			for (int i2 = 0; i2 <= n; ++i2) {
				for (int i3 = 0; i3 <= n; ++i3) {
					for (int i4 = 0; i4 <= n; ++i4) {
						for (int i5 = 0; i5 <= n; ++i5) {
							for (int i6 = 0; i6 <= n; ++i6) {
								if (n == 100 * i6 + 50 * i5 + 20 * i4 + 10 * i3 + 5 * i2 + i1) {
									++m;
									printf("方案%d：100元：%d张 50元：%d张 20元：%d张 10元：%d张 5元：%d张 1元：%d张\n",m,i6,i5,i4,i3,i2,i1);
								}
							}
						}
					}
				}
			}
		}
		printf("%d\n", m);
	}
	return 0;
}

// 2暴力，暴力的优化版，把剩余钱可能存在的面值的情况都试一下，符合条件的自增，测试n = 200结果大概1秒出来
#include<stdio.h>
int main_ONM()
{
	int n, m;
	while (scanf_s("%d", &n) != EOF)
	{
		m = 0;
		for (int i1 = 0; i1 <= n; ++i1) {
			for (int i2 = 0; i2 <= (n - i1) / 5; ++i2) {
				for (int i3 = 0; i3 <= (n - i1 - i2 * 5) / 10; ++i3) {
					for (int i4 = 0; i4 <= (n - i1 - i2 * 5 - i3 * 10) / 20; ++i4) {
						for (int i5 = 0; i5 <= (n - i1 - i2 * 5 - i3 * 10 - i4 * 20) / 50; ++i5) {
							for (int i6 = 0; i6 <= (n - i1 - i2 * 5 - i3 * 10 - i4 * 20 - i5 * 50) / 100; ++i6) {
								if (n == 100 * i6 + 50 * i5 + 20 * i4 + 10 * i3 + 5 * i2 + i1) {
									++m;
									printf("方案%d：100元：%d张 50元：%d张 20元：%d张 10元：%d张 5元：%d张 1元：%d张\n",m,i6,i5,i4,i3,i2,i1);
								}
							}
						}
					}
				}
			}
		}
		printf("%d\n", m);
	}
	return 0;
}
*/
//3 动态规划，解释起来比较复杂，对每个面值可能的情况每次循环进行一次兑换的考虑，第一次考虑由1元组成的情况，
// 第二次循环考虑对1和5元组成的情况，第三次考虑由1元、5元和10元组成的情况，以此类推，
// 考虑6次，比如n = 10时，第一次循环temp[0~9] = 1，第二次循环temp[0~4] = 之前的1, temp[5~9] = 之前的1 + 1 = 2,
// temp[10] = 之前的2 + 1 = 3
#include <stdio.h>
int main_DO()
{
	int a[6] = { 1,5,10,20,50,100 }, n;
	while (scanf_s("%d", &n) != EOF)
	{
		int temp[10000] = { 0 };
		temp[0] = 1;
		for (int i = 0; i < 6; i++) {
			for (int j = 1; j <= n; j++) {
				if (j >= a[i])
					temp[j] += temp[j - a[i]];
				    printf("%d\n",temp[j]);
			}
			printf("\n");
		}
		printf("%d\n", temp[n]);
	}
	return 0;
}
/*
// 4动态规划，在上一个基础上嵌套循环的j每次不必要从1开始，因为每次1~a[i] - 1都是不符合后面的if条件的，
// 这部分是无用循环，所以在符合钱数大于下一次的面值a[i]的时候直接让j从a[i]开始循环，此时也省了后面的if判断条件，注释掉即可
#include <stdio.h>
int main()
{
	int a[6] = { 1,5,10,20,50,100 }, n;
	while (scanf("%d", &n) != EOF)
	{
		int temp[10000] = { 0 };
		temp[0] = 1;
		for (int i = 0; i < 6; i++) {
			for (int j = a[i]; j <= n; j++) {
				//	if(j>=a[i])
				temp[j] += temp[j - a[i]];
				//printf("%d\n",temp[j]);
			}
			//	printf("\n");
		}
		printf("%d\n", temp[n]);
	}
	return 0;
}

5动态规划 + 动态数组
上面的算法都是在a[10000]内的，如果n >= 10000的话，数组溢出，
如果把数组开大浪费内存空间，开小了n输入限制，所以采用动态数组的方式，n是多少就有n + 1个数组

动态数组格式


#include <stdlib.h>//所需头文件
int* a;
int N;
scanf("%d", &N);//获取数组大小
a = (int*)malloc(N * sizeof(int));//分配空间
free(a);//释放内存




#include <stdio.h>
#include<stdlib.h>
int main_scan()
{
	int a[6] = { 1,5,10,20,50,100 }, n;
	while (scanf("%d", &n) != EOF)
	{
		int* temp = (int*)malloc(sizeof(int) * (n + 1));//n+1防止下面temp[j]溢出
		temp[0] = 1;
		for (int i = 0; i < 6; i++)
			for (int j = a[i]; j <= n; j++)
				temp[j] += temp[j - a[i]];
		printf("%d\n", temp[n]);
		free(temp);
	}
	return 0;
}
因为int范围 - 2~31到2~31，所以int最大2147483647，对应本题到n为4094或4095，4096超int范围

6动态规划 + 动态数组 + 扩大应用范围
既然动态数组，那么改变数据类型long long，可以求更大的n对应的结果 
#include <stdio.h>
#include<stdlib.h>
int main()
{
	int a[6] = { 1,5,10,20,50,100 }, n;
	while (scanf("%d", &n) != EOF)
	{
		long long* temp = (long long*)malloc(sizeof(long long) * (n + 1));
		temp[0] = 1;
		for (int i = 0; i < 6; i++)
			for (int j = a[i]; j <= n; j++)
				temp[j] += temp[j - a[i]];
		printf("%lld\n", temp[n]);
		free(temp);
	}
	return 0;
}

*/