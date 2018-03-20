#ifndef OUTPUT_ALL_H_INCLUDED
#define OUTPUT_ALL_H_INCLUDED

void output_all(const unsigned* V,unsigned n)
{
    //输出结果中每行最多12个随机数
    const unsigned NL = 12;
    unsigned i = 1;
    for(;i<=NL;i++)
    {
          printf("%5d ",i);  //显示1～12列的序号
    }
    printf("\n");
    for(i=1;i<n;i++)
    {
        if(i%(NL + 1) != 0)
          printf("%5d ",V[i]);
         else
          printf("\n");
    }
    printf(0 == n ?"  ":"\n");
}

#endif // OUTPUT_ALL_H_INCLUDED
