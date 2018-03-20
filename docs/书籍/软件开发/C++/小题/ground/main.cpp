#include <iostream>

using namespace std;

int  main()
{
    string name;
    int  pennies;
    int nickels;
    int dimes;
    int quarters;
    int dollars;
    int totalDollars;
    int change;
    int totalCents;
    //Read user' first name.
    cout <<"Enter your first name : ";
    cin >>name ;
    //Read  in the count of nickels and pennies.
    cout<<"Enter the number of dollars:";
    cin >>dollars ;
    cout <<"Enter the number of quarters: ";
    cin >>quarters ;
    cout<<"enter the number of dimes: ";
    cin >>dimes;
    cout <<"Enter the nuber of nickels: " ;
    cin>>nickels ;
    cout <<"Enter the number of pennies: ";
    cin >>pennies;
    //compute the total value in cent.
    totalCents = 100 * dollars + 25 * quarters + 10 * dimes + 5 * nickels + pennies ;
    //find the value in dollars and change.
    totalDollars= totalCents / 100;
    change = totalCents %100;
    //display the value in dollars and change.
    cout <<"Coin credit: "<<name <<endl;
    cout <<"Dollars:"<<totalDollars<<endl;
    cout <<"Cents: "<< change <<endl;
    return 0;
}
