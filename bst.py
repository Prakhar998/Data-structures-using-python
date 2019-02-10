class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

 
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:

                if self.right is None:
                    self.right = Node(data)
                else
                    self.right.insert(data)
        else:

            self.data = data
    def lookup(self, data, parent=None):
    	 if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def delete(self, data):
    	node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()
   	def delete(self, data):
    ...
    elif children_count == 1:
        # if node has 1 child
        # replace node with its child
        if node.left:
            n = node.left
        else:
            n = node.right
        if parent:
            if parent.left is node:
                parent.left = n
            else:
                parent.right = n
            del node
        else:
            self.left = n.left
            self.right = n.right
            self.data = n.data

root.insert(3)
root.insert(6)
root.insert(8)
node, parent = root.lookup(6)
root.delete(14)

