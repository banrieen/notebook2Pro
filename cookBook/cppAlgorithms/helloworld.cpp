// #include <iostream>
// using namespace std;

// int main()
// {
//     char name[64] = "xiaoxiao";
//     cout << "Input Your Name: ";
//     // cin >> a;
//     cout << name <<" Hello, World!";
//     return 0;
// }


#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{

   vector<string> msg {"Hello", "C++", "World", "from", "VS Code!"};

   for (const string& word : msg)
   {
       cout << word << " ";
   }
   cout << endl;
}
