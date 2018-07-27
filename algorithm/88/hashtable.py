from adt import Array


class Slot:

    def __init__(self, key, value):
        self.key, self.value = key, value


class HashTable:
    UNUSE = None
    EMPTY = Slot(None, None)

    def __init__(self):
        """define basic data"""
        self._table = Array(size=8, init=HashTable.UNUSE)
        self.length = 0

    def __len__(self):
        """return hashtable's length"""
        return self.length

    @property
    def _load_factory(self):
        return self.length / float(len(self._table))

    def _hash(self, key):
        return abs(hash(key)) % len(self._table)

    def _find_key(self, key):
        """receiver a key return key's index or None"""
        index = self._hash(key)
        _len = len(self._table)
        while self._table[index] is not HashTable.UNUSE:
            if self._table[index] is HashTable.EMPTY:
                #  used but removed
                index = (index * 5 + 1) % _len
                continue
            elif self._table[index].key == key:
                # slot.key == key
                return index
            else:
                index = (index * 5 + 1) % _len

        return None  # not found return None

    def __contains__(self, key):
        """behave like a in b"""
        index = self._find_key(key)
        return index is not None

    def _find_slot_can_insert(self, index):
        return self._table[index] in (HashTable.UNUSE, HashTable.EMPTY)

    def _find_slot_for_insert(self, key):
        index = self._hash(key)
        _len = len(self._table)

        while not self._find_slot_can_insert(index):
            index = (index * 5 + 1) % _len
        return index

    def _rehash(self):
        newsize = len(self._table) * 2
        oldtable = self._table
        self._table = Array(size=newsize, init=HashTable.UNUSE)
        self.length = 0

        for slot in oldtable:
            if slot not in (HashTable.UNUSE, HashTable.EMPTY):
                index = self._find_slot_for_insert(slot.key)
                self._table[index] = slot
                self.length += 1

    def add(self, key, value):
        if key in self:
            # update
            index = self._find_key(key)
            self._table[index] = Slot(key, value)
            return False
        else:
            # index is None means need find a new index
            index = self._find_slot_for_insert(key)
            self._table[index] = Slot(key, value)
            self.length += 1
            if self._load_factory >= 0.8:
                self._rehash()
            return True

    def remove(self, key):
        if key not in self:
            raise KeyError("key not found")
        else:
            index = self._find_key(key)
            value = self._table[index].value
            self.length -= 1
            self._table[index] = HashTable.EMPTY
            return value

    def get(self, key, default=None):
        index = self._find_key(key)
        if index is None:
            return default
        return self._table[index].value

    def __iter__(self):
        for slot in self._table:
            if slot not in (HashTable.UNUSE, HashTable.EMPTY):
                yield slot.key
