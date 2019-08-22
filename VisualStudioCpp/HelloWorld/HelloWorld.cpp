// HelloWorld.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>
#include "Calculator.h"
using namespace std;

int main()
{
	double x = 0.0;
	double y = 0.0;
	double result = 0.0;
    char oper = '+';
	cout << "输入要计算的数字： " << endl;
	Calculator H;
	while (true)
	{
		cin >> x >> oper >> y;
		result = H.Calculate(x, oper, y);
		cout << "Result is: " << result << endl;
	}

}

void quickSort(int a[], int, int);
void merge(int a[], int low, int mid, int high);
void mergeSort(int a[], int low, int high);
void display(int a[], int len);
void quick_sort(int array[], int low, int high);


int main_bak_cpu()
{
	for (; ; )
	{
		for (int i = 0; i < 960000; i++)
			;
		//sleep(10);
	}
	return 0;
}

int main_bak()
{
	int a, *iptr, *jptr, *kptr;
	//cout << 'The point init addr of : '<< &a;
	iptr = &a;

	std::cout << "Hello Sort World!\n";
	int array[] = { 34,65,12,43,67,5,78,10,3,70 };
	int len = sizeof(array) / sizeof(int);
	display(array, len);
	cout << "The orginal arrayare:" << endl;
	//quickSort(array, 0, len - 1);
	int low, high;
	low = 0;
	high = len - 1;
	//mergeSort(array, low, high);
	quick_sort(array, low, high);
	cout << "The sorted arrayare:" << endl;
	display(array, len);
	system("pause");
	return 0;
}

void display(int array[],int len)
{
	int k;
	for (k = 0; k < len; k++)
		cout << array[k] << ",";
	cout << endl;
}

void quickSort(int s[], int l, int r)
{
	if (l < r)
	{
		int i = l, j = r, x = s[l];
		while (i < j)
		{
			while (i < j && s[j] >= x) // 从右向左找第一个小于x的数
				j--;
			if (i < j)
				s[i++] = s[j];
			while (i < j && s[i] < x) // 从左向右找第一个大于等于x的数
				i++;
			if (i < j)
				s[j--] = s[i];
		}
		s[i] = x;
		quickSort(s, l, i - 1); // 递归调用
		quickSort(s, i + 1, r);
	}
}
// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单



void merge(int a[], int low, int mid, int high) {
	// subarray1 = a[low..mid], subarray2 = a[mid+1..high], both sorted
	// 归并排序
	int N = high - low + 1;
	int *b = new int[N]; // 讨论: 为什么我们需要一个临时的数组 b?
	int left = low, right = mid + 1, bIdx = 0;
	while (left <= mid && right <= high) // 归并
		b[bIdx++] = (a[left] <= a[right]) ? a[left++] : a[right++];
	while (left <= mid) b[bIdx++] = a[left++]; // leftover, if any
	while (right <= high) b[bIdx++] = a[right++]; // leftover, if any
	for (int k = 0; k < N; k++) a[low + k] = b[k]; // copy back
}

void mergeSort(int a[], int low, int high) {
	// 要排序的数组是 a[low..high]
	if (low < high) { // base case: low >= high (0 or 1 item)
		int mid = (low + high) / 2;
		mergeSort(a, low, mid); // 分成一半

		mergeSort(a, mid + 1, high); // 递归地将它们排序
		merge(a, low, mid, high); // 解决: 归并子程序
	}
}

int partition(int a[], int i, int j)
{
	int pivot = a[i];
	int m = i;
	for (int k = i+1; k < j; k++)
	{
		if (a[k] < pivot)
		{
			m++;
			swap(a[k], a[m]);
		}
	}
	swap(a[i], a[m]);
	return m;
}

void quick_sort(int array[], int low, int high)
{
	if (low < high)
	{
		int m = partition(array, low, high);
		quick_sort(array, low, m-1);
		quick_sort(array, m+1, high);
	}
	
}