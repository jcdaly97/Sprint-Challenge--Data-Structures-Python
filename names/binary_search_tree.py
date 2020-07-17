
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BSTNode(value)
                else:
                    self.left.insert(value)
            elif value >= self.value:
                if self.right is None:
                    self.right = BSTNode(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value  
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        current = self
        while(current.right):
            current = current.right
        return current.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)
        fn(self.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = [node]
        while queue:
            current = queue.pop(0)
            print(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)   

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        current = node

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            
            else:
                current = stack.pop()
                print(current.value)
                current= current.right

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node.value)
            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)
            print(node.value)


bst = BSTNode(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
print(bst.contains(5))
#bst.dft_print(bst)