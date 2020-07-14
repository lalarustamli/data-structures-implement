class Myqueue:
    def __init__(self):
        self.queue_list = []

    def size(self):
        # Complexity: O(1)
        return len(self.queue_list)

    def is_empty(self):
        # Complexity: O(1)
        return self.size() == 0

    def front(self):
        # Complexity: O(1)
        if self.is_empty():
            return None
        else:
            return self.queue_list[0]

    def back(self):
        # Complexity: O(1)
        if self.is_empty():
            return None
        else:
            return self.queue_list[-1]

    def enqueue(self, value):
        # Complexity: O(1)
        self.queue_list.append(value)

    def deque(self):
        # Complexity: O(n)
        # Here we have implemented queue using python list. However, if the queue is implemented using a Linked list,
        # the time complexity can be optimized to O(1).
        if self.is_empty():
            return None
        else:
            head = self.front()
            self.queue_list.remove(head)
            return head
