class Node:
    def __init__(self, data):
        self.data = data
        self.previous_element = None
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None
