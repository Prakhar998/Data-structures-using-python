# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 10:24:17 2018

@author: Prakhar Tripathi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:05:23 2018

@author: Prakhar Tripathi
"""

class Node(object):
    #constructor
    def __init__(self,data):
        self.data=data;
        self.next=None;
        
class ll(object):
        def _init_(self):
            self.head=None;
            self.size=0;
            
        def insertStart(self,data):
            
            
            newNode=Node(data)
             newNode.next=self.head;
               self.head=newNode;
            
                
        def app(self,ne):
            ne=node(data)
            if self.head is None:
                self.head=ne
                return
            last=self.head
            while(last.Next):
                last=last.Next
            last.next=ne
            
        def pl(self):
            temp=self.head
            while(temp):
                print temp.data;
                temp=temp.Next


        def insend(self,data):
            
            newNode=Node(data);
            while actualNode.nextNode is not None:
             actualNode=actualNode.nextNode;
             actualNode.nextNode=newNode;
        def travlist(self):
            actualNode=self.head;
           
            while actualNode is not None:
               print("%d"%actualNode.data);
               actualNode=actualNode.nextNode;
               

            
if _name_=='_main_':
    linkist=ll();
    linkist.append(10);
    linkist.append(12);
         





        # -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:05:23 2018

@author: Prakhar Tripathi
"""

class Node(object):
    #constructor
    def __init__(self,data):
        self.data=data;
        self.next=None;
        
class ll(object):
        def _init_(self):
            self.head=None;
            self.size=0;
            
        def insertStart(self,data):
            
            
            newNode=Node(data)
             newNode.next=self.head;
               self.head=newNode;
            
                
        def app(self,ne):
            ne=node(data)
            if self.head is None:
                self.head=ne
                return
            last=self.head
            while(last.Next):
                last=last.Next
            last.next=ne
            
        def pl(self):
            temp=self.head
            while(temp):
                print temp.data;
                temp=temp.Next


        def insend(self,data):
            
            newNode=Node(data);
            while actualNode.nextNode is not None:
             actualNode=actualNode.nextNode;
             actualNode.nextNode=newNode;
        def travlist(self):
            actualNode=self.head;
           
            while actualNode is not None:
               print("%d"%actualNode.data);
               actualNode=actualNode.nextNode;
               

            
if _name_=='_main_':
    linkist=ll();
    linkist.append(10);
    linkist.append(12);
         





        