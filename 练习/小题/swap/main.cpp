#include <iostream>
#include <string>

template <class T>
void swap(T* x,T* y)
{
    std::cout<<"swap(T* ,T*) called.\n";
    if(*x != *y)
    {
        T tmp=*x;
        *x =*y;
        *y = tmp ;
    }
}
void swap(int& x,int& y)
{
    std::cout<<"swap(int&, int&) called .\n";
    if(x != y)
    {
        x ^= y;
        y ^= x;
        x ^= y;
    }
}
//using namespace std;
using  std::cout;
int main()
{
    int a = 9, b = 1 ;
    swap(a,b);
    cout<<a<<"  "<<b<<"\n\n";

    double c = 3.3,d = 3.72;
    swap(&c,&d);
    cout<<c<<"  "<<d<<"\n\n";
    char e = 'm',f = 'M';
    swap(&e , &f);
    cout<<e<<"  "<<f<<"\n\n";

   // char* str1="string 1";
   // char* str2="string 2";
   std::string str1("string 1"),str2("string 2");
   str1.swap(str2);
   // std::swap(str1,str2);
    cout<<str1<<"   "<<str2<<"\n\n";

    cout << "Hello world!" << "\n\n";
    return 0;
}
