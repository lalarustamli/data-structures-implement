import ctypes


class MyArray(object):
    def __init__(self):
        self.n = 0  # Count of the elements, default 0
        self.capacity = 1  # Default capacity
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, item):
        if not 0 <= item <= self.n:
            return IndexError('Out of bound!')
        return self.array[item]

    def _resize(self, new_cap):
        big_array = self.make_array(new_cap)

        for item in range(self.n):
            big_array[item] = self.array[item]

        self.array = big_array
        self.capacity = new_cap

    def append(self, item):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)

        self.array[self.n] = item
        self.n += 1

    def insert_at(self, item, index):
        if index < 0 or index > self.n:
            print("please enter appropriate index..")
            return

        if self.n == self.capacity:
            self._resize(2 * self.capacity)

        for i in range(self.n - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]

        self.array[index] = item
        self.n += 1

    def pop(self):
        if self.n == 0:
            print("This array is empty")
            return

        self.array[self.n-1] = 0
        self.n -= 1

    def make_array(self, new_cap):
        new_arr = new_cap * ctypes.py_object
        return new_arr()


arr = MyArray()
arr.append(1)
arr.append(2)

print(len(arr))
