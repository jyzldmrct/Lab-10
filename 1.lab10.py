class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert (self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node (data)
                else:
                    self.left.insert (data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                      self.right.insert(data)

   def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()
                    
root = Node('F')
root.insert('B')
root.insert('A')
root.insert('D')
root.insert('C')
root.insert('E')
root.insert('G')
root.insert('H')
root.insert('I')


root.PrintTree()
