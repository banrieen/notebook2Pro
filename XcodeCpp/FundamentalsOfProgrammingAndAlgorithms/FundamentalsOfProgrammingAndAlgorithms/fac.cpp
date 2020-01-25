//
//  fac.cpp
//  FundamentalsOfProgrammingAndAlgorithms
//
//  Created by lizhen on 2020/1/21.
//  Copyright © 2020 lizhen. All rights reserved.
//

#include "fac.hpp"


long facNum(int n)
{
    long f = 0.0;
    if(n<0)
        printf("n < 0, data error! ");
    else if(n==0 | n==1)
        f = 1;
    else
        f = facNum(n-1)*n;
    return(f);
}
