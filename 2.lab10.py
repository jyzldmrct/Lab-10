class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def traversepreorder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.traversepreorder()
        if self.right:
            self.right.traversepreorder()

    def traverseinorder(self):
        if self.left:
            self.left.traverseinorder()
        print(self.data, end=' ')
        if self.right:
            self.right.traverseinorder()

    def traversepostorder(self):
        if self.left:
            self.left.traversepostorder()
        if self.right:
            self.right.traversepostorder()
        print(self.data, end=' ')

root = Node('F')
root.left = Node('B')
root.right = Node('G')
root.left.left = Node('A')
root.left.right = Node('D')
root.left.right.left = Node('C')
root.left.right.right = Node('E')
root.right.right = Node('I')
root.right.right.left = Node('H')

print("Preorder: ", end="")
root.traversepreorder()
print("\nInorder: ", end="")
root.traverseinorder()
print("\nPostorder: ", end="")
root.traversepostorder()
