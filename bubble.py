# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 09:57:02 2018

@author: Prakhar Tripathi
"""

def bubble(bub):
     for j in range(len(bub)):
         for k in range(len(bub)-1):
             if bub[k]>bub[k+1]:
                 bub[k],bub[k+1]=bub[k+1],bub[k]
         print('\n sorted list=',bub)
         print('\n')
         
def bs(bse):
    x=int(input('Enter the element to be searched='))
    for i in range(0,len(l/2)):
        if x==i:
            print('element found')
            print(l.index)
            break
        if x!=i:
            if x<range(l/2):
                len(l)=len((l/2)-1)
                for i in range(0,len(l))        
         
         
t=int(input('Size=='))
l=[] 
for y in range(t):
    e=int(input('elements='))
    l.append(e)
    
bubble(l)    
bs(l)