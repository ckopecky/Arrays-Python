'''
Things we need for an advanced array:

1 - size of it and protection from going past that
2 - size of the items in the array
3 - to append, we need space
4 - track allocated and used
5 - if we run out of space, we need to make a new array with more space, then copy each item over. 

'''

# make a dynamic array

class DynamicArray:
    def __init__(self, capacity = 8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * capacity

    def append(self, value):
        # add something to the end
        if self.count >= self.capacity:
            self.resizeArray()
        self.storage[self.count] = value
        self.count += 1

    def insert(self, value, index):
        # add to somewhere
        if self.count >= self.capacity:
            self.resizeArray()
        for i in range(self.count, index, -1):
            self.storage = self.storage[i - 1]
        
        self.storage[index] = value
        self.count += 1

    def remove(self, index):
        # find the index we want
        value = self.storage[index]
        # replace with the next value and move down list till end
        for i in range(index, self.count - 1, 1):
            self.storage[i] = self.storage[i+1]
        # subtract from count
        self.count -= 1
        return value

    def printItem(self):
        for value in self.storage:
            print(value)

    def resizeArray(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]

        self.storage = new_storage


    def add_to_front():
        self.insert(value, 0)





