# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity=2):
        self.capacity = capacity  # Number of buckets in the hash table
        self.count = 0
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        h = 5381
        for c in key:
            h = (h * 33) + ord(c)
        return h


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # if (self.count / self.capacity) > 0.8: # resize at 80% load capacity
        #     self.resize()   

        #djb2 hashing
        hash_key = self._hash_djb2(key)
        index = hash_key % self.capacity

        # if the index is empty insert a linkedpair here and increase the count by 1
        if self.storage[index] is None: 
            self.storage[index] = LinkedPair(key, value)
            self.count += 1

        else: # iterate through linked list; key match = overwrite value; no key match = insert LinkedPair, count + 1
            temp = self.storage[index]
            while temp.next and temp.key != key:
                temp = temp.next
            if temp.key == key:
                temp.value = value
            else:
                temp.next = LinkedPair(key, value)
                self.count += 1  


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        #djb2 hashing
        hash_key = self._hash_djb2(key)
        index = hash_key % self.capacity

        if self.storage[index] is None: # key not found
            return print(f'{key} not found in table.')

        else: # iterate through linked list; key match = remove value, counter - 1
            temp = self.storage[index] # get list from storage at index

            if temp.key == key: # first key in list is a match
                self.storage[index] = temp.next # set to next linked pair or None
            
            while temp.next: # other keys in storage
                next_link = temp.next # get next linked pair in list

                if next_link.key == key:
                    if next_link.next:
                        temp.next = next_link.next
                    else:
                        temp.next = None

                temp = next_link 
        
        self.count -= 1
        print(f'{key} removed from table.')


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        #djb2 hashing
        hash_key = self._hash_djb2(key)
        index = hash_key % self.capacity

        if self.storage[index] is not None:
            temp = self.storage[index]
            while temp is not None:
                if temp.key == key:
                    return temp.value
                temp = temp.next

        return print(f'{key} not found in table.')


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        temp_ht = HashTable(self.capacity)

        for thing in self.storage:
            current = thing
            while current:
                temp_ht.insert(current.key, current.value)
                current = current.next
        
        self.storage = temp_ht.storage

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
