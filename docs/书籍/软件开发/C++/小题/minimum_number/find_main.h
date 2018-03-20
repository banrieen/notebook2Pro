#ifndef FIND_MAIN_H
#define FIND_MAIN_H
unsigned find_main(const unsigned* V,unsigned n)
{
    unsigned j = 0,i = 1;
    for(;i<n;i++)
    {rth/
        if(V[i]<V[j])
        j = i;
    }
            return j;
}


#endif // FIND_MAIN_H_INCLUDED
