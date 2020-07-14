class MyStack:
    def __init__(self):
        self.stack_list = []

    def size(self):
        # Complexity: O(1)
        return len(self.stack_list)

    def is_empty(self):
        # Complexity: O(1)
        return self.size() == 0

    def top(self):
        # Complexity: O(1)
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def push(self, value):
        # Complexity: O(1)
        self.stack_list.append(value)

    def pop(self):
        # Complexity: O(1)
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


def check_balanced(string):
    # Complexity: O(n)
    stack = MyStack()
    for i in string:
        if i == '(':
            stack.push(i)
        else:
            stack.pop(i)
    return stack.stack_list == []
