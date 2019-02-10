# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 10:21:24 2018

@author: Prakhar Tripathi
"""

def sel(a):
    for i in range(0,len(l)-1):
        min=a[i]
        
        for j in range(i+1,len(l)):
            if a[i]>a[j]:
                min=a[i]
                a[i]=a[j]
                a[j]=min
        print("sorted list=",a)
t=int(input('Size=='))
l=[] 
for y in range(t):
    e=int(input('elements='))
    l.append(e)
    
sel(l)