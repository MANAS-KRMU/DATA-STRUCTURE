class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __init__(self):
        self.head = None


def insertion_at_start(self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node   
   
Node(25)
