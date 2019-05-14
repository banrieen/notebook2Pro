#include <iostream>

using namespace std;


int main()
{
    cout << "Hello world!" << endl;
    int a, b, c, i,j,k,t;
    b=100;
    c=200;
    t=10;
        for (i=1;i<=t;i++)
    {
        b++;
        c=c-2;
        a = b+c;
    }
    k=a;   //最小值 k==290
    j=a;
    for (i=1;i<=t;i++)
    {
        b++;
        c=c-2;
        a = b+c;
     //三角形输出
            while (a-k<0)
            {
                 k--;
              cout<<"   "<<" ";
             }
   // 补全三角形为矩形,K为最大值

   k=j;

         while (k-(a+10)<=0)
           {
             k++;
             cout<<a<<" ";
            }
   k=j;

  //输出反三角形，用 | 符号隔开 a==k
     cout<<" "<<"|"<<"  ";
         while (k-(a+10)<=0)
           {
             k++;
             cout<<a<<" ";
            }
   k=j;
     cout<<endl;
    }
    return 0;
}
