class DynamicArray:
    def _init_(self, capacity=8):
        self.capacity = capacity #length of allocation
        self.count = 0 # how much is being used
        self.storage = [None] * self.capacity

    def insert(self, index, value):
        if self.count == self.capacity:
            self.resize
            return

            # shift elements to the right
            for i in range(self.count, index):
                self.storage[i] = self.storage[i-1]

            # insert value
            self.storage[index] = value
            self.count += 1

    def append(self, value):
        self.insert(self.count, value)

    def resize(self): 
        self.capacity *= 2 # double the capacity
        new_storage = [None] * self.capacity        
        for i in range(self.count): # copy current array over to new array
            new_storage[i] = self.storage[i]
        self.storage = new_storage # point to new block of memory

    def replace(self, index, value):
        self.storage[index] = value

    def add_to_front(self, value):
        self.insert(0, value)

    def slice(self, beginning_index, end_index):
        # need beginning and end index
        # create a sub-array to store values
        # copy beginning_index through end_index to the subarray
        # keep or delete original array
        # return the sub-array
