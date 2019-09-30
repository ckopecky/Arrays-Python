'''
what does a hash table do? 

an array that uses indexes based of your hash method

it's a data structure that uses a hash function to keep track of where data is put. Each piece of information to be stored has a name, which called a key. Each key is matched up with a piece of data called a value. 




'''
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
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
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
        pass


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
        index = self._hash_mod(key)
        current_pr = self.storage[index]
        last_pr = None

        while current_pr is not None and current_pr.key != key:
            last_pr = current_pr
            current_pr = last_pr.next

        if current_pr is not None:
            current_pr.value = value
        
        else:
            new_pr = LinkedPair(key, value)
            new_pr.next = self.storage[index]
            self.storage[index] = new_pr




    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current_pr = self.storage[index]
        last_pr = None

        while current_pr is not None and current_pr.key != key:
            last_pr = current_pr
            current_pr = last_pr.next
        
        if current_pr is None:
            print("ERROR: Unable to remove entry with key " + key)
        
        else: 
            if last_pr is None:
                self.storage[index] = current_pr.next
            else:
                last_pr.next = current_pr.next

        


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        
        index = self._hash_mod(key)
        current_pr = self.storage[index]

        while current_pr is not None:
            if(current_pr.key == key):
                return current_pr.value
            current_pr = current_pr.next



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity = 2 * self.capacity
        self.storage = [None] * self.capacity

        current_pr = None
        for item in old_storage:
            current_pr = item
            while current_pr is not None:
                self.insert(current_pr.key, current_pr.value)
                current_pr = current_pr.next



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
