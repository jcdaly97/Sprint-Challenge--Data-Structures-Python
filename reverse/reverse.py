class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev = None):
        #checks if the list is empty
        if node is None:
            return node
        #checks if we've reached the end of the list
        #sets a new head
        if node.next_node is None:
            self.head = node
            return node
        #reccurs
        next_step = self.reverse_list(node.next_node)
        #swaps the link between a node and it's next_node
        node.next_node.next_node = node
        node.next_node = None
        return next_step
        

            
        

        
