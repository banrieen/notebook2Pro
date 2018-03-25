#include <iostream>

using namespace std;

class padding
{
    private :
    char a;
    int b;
    double c;
    public:
    padding(char c='a',int i=100,double d=2.3):a(c),b(i),c(d) {}
};
int main()
{
    cout << "Hello world!" << endl;
    padding al;
    std::cout <<"size of padding == "<<sizeof(padding)<<endl ;
    char * p=(char *)(&al);
    int int_len=sizeof(int);
    std::cout<<*p<<endl;
    std::cout<<int_len<<endl;

    return 0;
}
