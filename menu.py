# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 09:57:08 2018

@author: Prakhar Tripathi
"""





def ls(linea):
    x=int(input('item to be searched='))
    for i in range(e):
        if x==i:
           print(l.index(x))
           break
        
        
def dele(dee):
     x=int(input('enter the element to be deleted='))
     for i in range(e):
         if x==i:
            l.remove(x)
            print('list=',l)
            break
         
         

t=int(input('Size=='))
l=[] 
for y in range(t):
    e=int(input('element='))
    l.append(e)
    
print('choice menu:')
print('1 for deletion')
print('2 for search')
ch=int(input('='))
if   ch==1:
     dele(l)
     
if    ch==2:
      ls(l) 
    
      