# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 10:45:55 2018

@author: Prakhar Tripathi
"""

class con:
    def _init_(self,cap):
        self.top=-1
        self.cap=cap
        self.array=[]
        self.out=[]
        self.prec={'+':1,'-':1,'*':2,'/':2,'^':3}
    def emp(self):
        return True if self.top == -1 else False
    def pe(self):
        return self.array[-1]
    def pop(self):
        if not self.emp():
            self.top =-1
            return self.array.pop()
        else:
            return "$"
    def push(self,op):
        self.top+=1
        self.array.append(op)
    def iso(self,ch):
        return ch.isalpha
    def nog(self,i):
        try:
            a=self.prec[i]
            b=self.prec[self.pe()]
            return True if a<=b else False
        except KeyError:
            return False
    def itp(self,exp):
        for i in exp:
uq            