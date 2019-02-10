# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 09:49:07 2018

@author: Prakhar Tripathi
"""

def enq(l, front, rear):
    if( front == rear == i - 1) :
        print ("Overflow")
        
        
    if(front == rear and rear == -1):
        front = rear = 0;
    else :
        rear = rear + 1
        l.append(l)
            

i=int(input('Size=='))
l=[] 
front = rear = -1
for y in range(0,i):
    if(y == 0) :
        front = front  + 1
    e=int(input('elements='))
    l.append(e)
    rear==i
    
enq(l, front, rear)       
print(l)