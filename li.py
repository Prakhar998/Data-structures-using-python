# @Prakhar
class Node:
	#cons
	def __init__(self):
		self.data=None
		self.next=None
		
	#create data part
	def set_data(self,data):
		self.data=data
	#get data
	def get_node(self):
		return self.data
	#create next part
	def set_next(self,next):
		self.next=next
	def get_next(self):
		return self.next
    #check    
    def check_next(self):
    	return self.next !=None
    def ins_beg(self,data):
    	new_node=Node()
    	new_node.set_data(data)
    	if self.head==0
    	self.head=new_node
    	else:
    		new_node.set_data(data)
    		self.head=new_node
    		self.length +=1

l=Node()
l.ins_beg(3)
l.ins_beg(4)