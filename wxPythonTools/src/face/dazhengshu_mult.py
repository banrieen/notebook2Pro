# -*- coding: UTF-8 -*-

'''
Created on Apr 8, 2018

@author: Lizhen
'''

class dazhengshuMult:
    def __init__(self,numa,numb):
        if a and b:
            self.a = numa
            self.b = numb
        
    def mult(self):
        
        lena = len(self.a)
        lenb = len(self.b)
        c = [0 for k in range(0,lena+lenb)]
        for i in range(0,lena):
            for j in range(0,lenb):
                c[i+j+1] += int(self.a[i]) * int(self.b[j])
            
        for m in range(0,len(c)):
            if(c[m] > 9):
                c[m+1] += c[m]//10 
                c[m] = c[m]%10
                
        c.reverse()
        
        return int(''.join([str(ci) for ci in c])) 
    
if __name__ == "__main__":
    a = list(input())
    b = list(input())
    dsm = dazhengshuMult(a,b)
    print(dsm.mult())
    