class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        # Even when a linked list is empty, the head must always exist.
        self.head = None

    def reverse(self):
        previous = None
        current = self.get_head()
        next = None
        while current is not None:
            self.printer()
            next = current.next_element
            current.next_element = previous
            previous = current
            current = next
        self.head = previous

    def length(self):
        # Complexity: O(n)
        temp = self.get_head()
        i = 0
        while temp is not None:
            i += 1
            temp = temp.next_element
        return i


    def get_head(self):
        # Complexity : O(1)
        return self.head

    def insert_at_head(self, data):
        # Complexity : O(1)
        temp_node = Node(data)
        temp_node.next_element = self.head
        self.head = temp_node
        return self.head

    def insert_at_tail(self, data):
        # Complexity: O(n)
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        temp = self.head
        while temp.next_element is not None:
            temp = temp.next_element
        temp.next_element = new_node
        return

    def insert_at_value(self, data, index):
        # Complexity: O(n)
        new_node = Node(data)
        if self.is_empty():
            if index == 0:
                self.head = new_node
                return
            else:
                print("The list is empty!")
        temp = self.head
        for i in range(index):
            if temp is None:
                print("The index is out of range")
            temp = temp.next_element
        temp.next_element = new_node
        return

    def find_mid(self):
        # Complexity : O (n)
        l = self.length()
        temp = self.get_head()
        if l % 2 == 0:
            l = l-1
        for i in range(int(l/2)):
            temp = temp.next_element
        return temp.data

    def remove_duplicates(self):
        # Complexity : O (n)
        ls = []
        temp = self.get_head()
        while temp:
            ls.append(temp.data)
            if temp.next_element and temp.next_element.data in ls:
                print("duplicate!" + str(temp.next_element.data))
                temp.next_element = temp.next_element.next_element
            else:
                temp = temp.next_element

    def search(self, data):
        # Complexity: O(n)
        if self.is_empty():
            return
        temp = self.head
        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.next_element

        return False

    def delete_at_head(self):
        # Complexity: O(1)
        first_elem = self.get_head()
        if first_elem is not None:
            self.head = first_elem.next_element
            first_elem.next_element = None
        return

    def delete_value(self, value):
        # Complexity: O(n)
        temp = self.get_head()
        while temp is not None:
            if self.search(value) is not None:
                if temp.data == value:
                    self.delete_at_head()
                    return
                if temp.next_element.data == value:
                    temp.next_element = temp.next_element.next_element
                    return
            temp = temp.next_element

    def printer(self):
        # Complexity : O(n)
        if self.is_empty():
            print("The list is empty")
            return False
        else:
            temp = self.head
            while temp.next_element is not None:
                print(temp.data, end=' - >')
                temp = temp.next_element
            print(temp.data, end=' -> None')
            return True

    def is_empty(self):
        # Complexity : O(1)
        if self.head is None:
            return True
        else:
            return False



def detect_loop(lst):
    # Complexity: O (n^2)
    one_step = lst.get_head()
    two_step = lst.get_head()
    while one_step and two_step and two_step.next_element:
        one_step = one_step.next_element
        two_step = two_step.next_element.next_element
        if one_step == two_step:
            return True
    return False


def union(lst1,lst2):
    l1 = lst1.get_head()
    l2 = lst2.get_head()
    while l1:
        while l2:
            if l1.data != l2.data:
                lst1.insert_at_tail(l2.data)
            l2 = l2.next_element
        l1 = l1.next_element
    return lst1


def intersection(list1,list2):
    # Complexity : max( O(mn), O(min(m,n)^2)
    l = LinkedList()
    l2 = list2.get_head()
    while l2:
        l1 = list1.get_head()
        while l1:
            if l1.data == l2.data:
                l.insert_at_tail(l2.data)
            l1 = l1.next_element
        l2 = l2.next_element
    l.remove_duplicates()
    l.printer()
    return l


def find_nth(lst, n):
    length = lst.length()
    temp = lst.get_head()
    for i in range(length-n):
        temp = temp.next_element

    return temp.data
