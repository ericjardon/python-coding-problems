# We need prime numbers for our hash function (table size)
# Source code: https://github.com/TheAlgorithms/Python/blob/master/data_structures/hashing/hash_table.py
from prime_numbers import next_prime

class HashTable:
    """Basic hash table with Open addressing & Linear Probing"""
    def __init__(self, table_size, load_factor=None, lim_load=None):
        " Load factor: how full the hash table can be before its size is increased"
        self.table_size = table_size
        self.values = [None] * self.table_size
        self.load_factor = 0.75 if load_factor is None else load_factor
        self.lim_load = 1 if load_factor is None else load_factor
        self._aux_list = []
        self._keys = set()

    @property
    def keys(self):
        return self._keys

    def balanced_factor(self):
        return sum([1 for slot in self.values if slot is not None]) / (
                self.table_size * self.load_factor
        )

    def hash_function(self, key):
        return key % self.table_size

    # for functionality visualization in console
    def step_by_step(self, step_order):
        print(f"step {step_order}")
        print([i for i in range(len(self.values))])
        print(self.values)

    def bulk_insert(self, vals):
        i = 1
        self._aux_list = vals
        for val in vals:
            self.insert_data(val)
            self.step_by_step(i)
            i += 1

    def insert_data(self, value):
        key = self.hash_function(value)

        if self.values[key] is None:
            self._set_value(key, value)

        elif self.values[key] == value:
            pass    # don't update if not necessaru

        else:
            collision_resolution = self.collision_resolution(key, value)
            if collision_resolution is not None:
                self._set_value(collision_resolution, value)
            else:
                # No available key found in table. Expand
                self.rehashing()
                self.insert_data(value)  # try again

    def _set_value(self, key, data):
        pass

    def collision_resolution(self, key, data):
        new_key = self.hash_function(key+1)     # get next key
        while self.values[key] is not None and self.values[new_key] != key:
            # keep looking for an empty slot while
            if self.values.count(None) > 0:
                new_key = self.hash_function(new_key+1)
            else:
                new_key = None
                break
        return new_key

    def rehashing(self):
        previous_vals = [value for value in self.values if value != None]
        self.table_size = next_prime(self.table_size, factor=2) # resize the table
        self._keys.clear()  # empty out the keys set
        self.values = [None for _ in range(self.table_size)]
        for v in previous_vals: # reinsert every val previously in table
            self.insert_data(v)