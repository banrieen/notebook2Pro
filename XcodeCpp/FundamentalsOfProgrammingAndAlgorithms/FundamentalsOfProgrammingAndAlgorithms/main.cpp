//
//  main.cpp
//  FundamentalsOfProgrammingAndAlgorithms
//
//  Created by lizhen on 2019/10/8.
//  Copyright © 2019 lizhen. All rights reserved.
//

#include <iostream>

#include "fac.hpp"

int fac();

int main(int argc, const char * argv[])
{
    // insert code here...
    // std::cout << "Hello, World!\n";
    fac();
    return 0;
}

int fac()
{
    int n = 0;
    long m;
    printf("input an integer number: ");
    scanf("%d", &n);
    m = facNum(n);
    printf("%d! = %ld \n", n,m);
    return (0);
}
