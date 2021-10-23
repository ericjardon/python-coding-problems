# A HashSet is a data structure for storing unique elements.
# Very useful for searching and retrieving, constant time.

# Methods of the HashSet:
# add(x)
# contains(x)
# remove(x)

"""A HashSet is partitioned into Buckets, each of which is associated with
 a unique value obtained from the hashing function. Usually mod. En each bucket,
 searching is done sequentially. It is better the less elements per bucket we
 have, so our hashing function must be a good one."""

class Bucket:
    """A bucket corrresponds to a single hash value of the Hash Table. Its array contents are called 'keys' too."""
    def __init__(self):
        self.bucket = []

    def get(self, key):
        """Linear search for the specified key.
            returns: True if present, False otherwise"""
        for k in self.bucket:
            if key == k:
                return True
        return False

    def remove(self, key):
        """ Linear searches then removes from the bucket array the specified key"""
        for i, k in enumerate(self.bucket):
            if k == key:
                del self.bucket[i]

    def update(self, key):
        """ Inserts specified 'key' (value) in bucket if it doesn't exist.
            Linear search for the key, if not found append it."""
        found = False
        for i, k in enumerate(self.bucket):
            # enumerate uses two elements at each iteration, the index and the value at the index
            if k == key:        # if it already exists just reassign it where we found it?
                self.bucket[i] = key
                found = True
                break
        if not found:       # if it does not exist yet, insert it last the bucket array
            self.bucket.append(key)

    class MyHashSet:
        def __init__(self):
            self.key_space = 2096       # close to 2 ^11
            self.hash_table = [Bucket() for _ in range(self.key_space)]
            # create an array of bucket objects of size key_space.
            # since it's an array, accessing any bucket is O(1)

        # For any CRUD operations, always compute the hash
        def add(self, key):         # uses bucket.update()
            hash = key%self.key_space       # hash function. get the hash value pointing to the Bucket
            self.hash_table[hash].update(key)
            # insert the key in the bucket associated with the hash val

        def remove(self, key):      # uses bucket.delete()
            hash = key%self.key_space       # hash function
            self.hash_table[hash].remove(key)

        def contains(self, key):        # uses bucket.get()
            hash = key%self.key_space       # hash function
            return self.hash_table[hash].get(key)   # just determine if the given key is present or not

## so a hash set relies on the buckets being able to find, add and delete elements in their hash bucket.
## the number of buckets is equivalent to the number of distinct values that our hash function produces.
## if the has function is modulus, mod(n) has n different values in range.