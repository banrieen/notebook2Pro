#include "pch.h"
#include "BasementAlgorithms.h"

SortAndQuery::SortAndQuery()
{
}

SortAndQuery::~SortAndQuery()
{
}


void SortAndQuery::display(int array[], int len)
{
	int k;
	for (k = 0; k < len; k++)
		std::cout << array[k] << ",";
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


void merge(int a[], int low, int mid, int high) {
	// subarray1 = a[low..mid], subarray2 = a[mid+1..high], both sorted
	// 归并排序
	int N = high - low + 1;
	int* b = new int[N]; 
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


//划分子分区计算基准位置
int Partition(int arr[], int nLower, int nUpper)
{
	int pivot = arr[nLower]; //取第一个记录为基准记录；
	int nLeft = nLower + 1; //加1 ，pivot 无需和自身比较；
	int nRight = nUpper;
	int temp;
	do {
		while (nLeft <= nRight && arr[nLeft] <= pivot)  //将nLeft逐渐增大，知道找到pivot的下标为止；
			nLeft++;
		while (nLeft <= nRight && arr[nRight] > pivot)   //将
			nRight--;
		//R[nLeft,nRight]区间的长度(元素数)大于1时，交换R[nLeft]和R[nRight]
		if (nLeft < nRight)
		{
			temp = arr[nLeft];
			arr[nLeft] = arr[nRight];
			arr[nRight] = temp;
			nLeft++;
			nRight--;
		}
	} while (nLeft < nRight);  //当nLeft==nRight时，停止循环；
	//把基准记录pivot放到正确位置，即nLeft和nRight同时指向的位置；
	temp = arr[nLower];
	arr[nLower] = arr[nLeft];
	arr[nRight] = temp;
	return nRight;

}


int SortAndQuery::QuickSort(int arr[], int nLower, int nUpper)
{
	int pivotpos;  //基准下标；
	if (nLower < nUpper)  //仅在区间长度大于1时才排序；
	{
		pivotpos = Partition(arr, nLower, nUpper); //划分子区间知道基准下标，（QuictSort的关键）；
		QuickSort(arr, nLower, pivotpos + 1);      //对做区间递归排序；
		QuickSort(arr, pivotpos + 1, nUpper);      //对有区间递归排序；
	}
	return 0;
}
