from collections import deque

from double_link_list import CycleDoubleLinkedList


class Bag:

    def __init__(self, maxsize=5):
        self.maxsize = maxsize
        self._item = []

    def add(self, item):
        if len(self) > self.maxsize:
            raise Exception('the bag is full')
        else:
            self._item.append(item)

    def remove(self, item):
        if item not in self._item:
            raise Exception('not exits in bag')
        else:
            self._item.remove(item)

    def __len__(self):
        return len(self._item)

    def __iter__(self):
        for item in self._item:
            yield item


class Array:

    def __init__(self, size=32, init=None):
        self._size = size
        self._item = [init] * self._size

    def __len__(self):
        return len(self._item)

    def __getitem__(self, key):
        return self._item[key]

    def __setitem__(self, key, value):
        self._item[key] = value

    def clear(self, value=None):
        for i in range(len(self._item)):
            self._item[i] = value

    def __iter__(self):
        for item in self._item:
            yield item


class Node:

    def __init__(self, value=None, next=None):
        self.value, self.next = value, next


class LinkedList:

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.length = 0
        self.tailnode = None

    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('liked list is full')

        node = Node(value)
        if self.tailnode is None:
            self.root.next = node
        else:
            self.tailnode.next = node

        self.tailnode = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('liked list is full')

        node = Node(value)
        headnode = self.root.next
        self.root.next = node
        node.next = headnode
        self.length += 1

    def iter_node(self):
        currnode = self.root.next
        if self.tailnode is None:
            return None
        while currnode is not self.tailnode:
            yield currnode
            currnode = currnode.next
        yield currnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def remove(self, value):
        currnode = self.root.next
        prevnode = self.root
        while currnode.next is not None:
            if currnode.value == value:
                prevnode.next = currnode.next
                del currnode
                self.length -= 1
                return
            prevnode = currnode
            currnode = currnode.next

    def find(self, value):
        index = 0
        for item in self:
            if item == value:
                return index
            index += 1

        return -1

    def pop(self):
        if self.root.next is None:
            raise Exception("pop from empty linked list")
        currnode = self.root.next
        while currnode.next is not None:
            if currnode.next is self.tailnode:
                value = self.tailnode.value
                self.length -= 1
                currnode.next = None
                self.tailnode = currnode
                return value
            currnode = currnode.next
        value = currnode.value
        del currnode
        self.root.next = None
        self.length -= 1
        return value

    def popleft(self):
        if self.root.next is None:
            raise Exception("pop from empty linked list")
        headnode = self.root.next
        value = headnode.value
        self.root.next = headnode.next
        if headnode is self.tailnode:
            self.tailnode = None
        self.length -= 1
        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0
        self.tailnode = None


class FullError(Exception):
    pass


class EmptyError(Exception):
    pass


class Queue:

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._item = LinkedList()

    def __len__(self):
        return len(self._item)

    def push(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise FullError("Queue is Full cannot push item")
        self._item.append(value)

    def pop(self):
        if len(self) <= 0:
            raise EmptyError("Queue pop from empty queue")
        return self._item.pop()


class ArrayQueue:
    """fifo first in first out"""

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = Array(size=self.maxsize)
        self.head = 0
        self.tail = 0

    def push(self, value):
        if len(self) >= self.maxsize:
            raise FullError("ArrayQueue is full")

        self.array[self.head % self.maxsize] = value
        self.head += 1

    def pop(self):
        if len(self) <= 0:
            raise EmptyError("ArrayQueue is empty")

        value = self.array[self.tail % self.maxsize]
        self.tail += 1
        return value

    def __len__(self):
        return self.head - self.tail


class Deque(CycleDoubleLinkedList):
    """fifo: first in first out"""

    def pop(self):
        tailnode = self.tailnode()
        node = super().remove(tailnode)
        if not node:
            raise EmptyError('Deque is empty')
        return node.value

    def popleft(self):
        headnode = self.headnode()
        node = super().remove(headnode)
        if not node:
            raise EmptyError('Deque is empty')
        return node.value


class Stack(Deque):
    """lifo: last in first out"""

    def push(self, value):
        self.append(value)

    def pop(self):
        return super().pop()

    def is_empty(self):
        return len(self) == 0


class ArrayStack:
    """lifo last in first out"""

    def __init__(self, maxsize=32):
        self.maxsize = maxsize
        self.item = Array(maxsize)
        self.head = 0

    def push(self, value):
        if len(self) >= self.maxsize:
            raise FullError("ArrayStack is full")
        self.item[self.head % self.maxsize] = value
        self.head += 1

    def pop(self):
        if len(self) <= 0:
            raise EmptyError("ArrayStack is empty")
        value = self.item[self.head - 1]
        self.head -= 1
        return value

    def __len__(self):
        return self.head

    def is_empty(self):
        return len(self) == 0


class CollectionDequeStack:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.deque = deque(maxlen=self.maxsize)

    def push(self, value):
        if len(self) >= self.maxsize:
            raise FullError("CollectionDequeStack is full")
        self.deque.append(value)

    def pop(self):
        if len(self) <= 0:
            raise EmptyError("ArrayStack is empty")
        return self.deque.pop()

    def __len__(self):
        return len(self.deque)

    def is_empty(self):
        return len(self) == 0


class Slots:

    def __init__(self, key, value):
        self.key, self.value = key, value


class HashTable:
    """哈希表"""
    UNUSED = None
    EMPTY = Slots(None, None)

    def __init__(self):
        """init fuction"""
        self._table = Array(size=8, init=HashTable.UNUSED)
        self.length = 0

    @property
    def _load_factory(self):
        """load factory if x > 0.8 need rehash add space"""
        return self.length / float(len(self._table))

    def __len__(self):
        """return hash table's length"""
        return self.length

    def _hash(self, key):
        """hash fuction use build-in hash()"""
        return abs(hash(key)) % len(self._table)

    def _find_key(self, key):
        """when happend hash collision need find a slot index"""
        index = self._hash(key)
        _len = len(self._table)

        while self._table[index] is not HashTable.UNUSED:
            if self._table[index] is HashTable.EMPTY:
                index = (index * 5 + 1) % _len
                continue
            elif self._table[index].key == key:
                return index
            else:
                index = (index * 5 + 1) % _len
        return None

    def _slot_can_insert(self, index):
        """judge slot can insert to hashtable"""
        return self._table[index] in (HashTable.UNUSED, HashTable.EMPTY)

    def _find_slot_for_insert(self, key):
        """find a empty slot fot insert"""
        index = self._hash(key)
        _len = len(self._table)

        while not self._slot_can_insert(index):
            index = (index * 5 + 1) % _len

        return index

    def __contains__(self, key):
        """in operation symbol magic method"""
        index = self._find_key(key)
        return index is not None

    def add(self, key, value):
        """add element to hashtable"""
        if key in self:
            index = self._find_key(key)
            self._table[index] = Slots(key, value)
            return False
        else:
            index = self._find_slot_for_insert(key)
            self._table[index] = Slots(key, value)
            self.length += 1
            if self._load_factory >= 0.8:
                self._rehash()

            return True

    def _rehash(self):
        """rehash index"""
        oldtable = self._table
        newsize = len(self._table) * 2
        self._table = Array(newsize, HashTable.UNUSED)
        self.length = 0

        for slot in oldtable:
            if slot not in (HashTable.UNUSED, HashTable.EMPTY):
                index = self._find_slot_for_insert(slot.key)
                self._table[index] = slot
                self.length += 1

    def get(self, key, default=None):
        """return the value of hashtable's key"""
        index = self._find_key(key)
        if index is None:
            return default
        else:
            return self._table[index].value

    def remove(self, key):
        """remove element from hashtable"""
        index = self._find_key(key)
        if index is None:
            raise KeyError("key not found")
        else:
            value = self._table[index].value
            self.length -= 1
            self._table[index] = HashTable.EMPTY
            return value

    def __iter__(self):
        """yield slot's key where has slot"""
        for slot in self._table:
            if slot not in (HashTable.UNUSED, HashTable.EMPTY):
                yield slot.key


class DictADT(HashTable):

    def __setitem____(self, key, value):
        self.add(key, value)

    def __getitem__(self, key, default=None):
        index = self._find_key(key)
        if not index:
            raise KeyError("key not found")
        return self.get(key, default)

    def _iter_slot(self):
        for slot in self._table:
            if slot not in (HashTable.UNUSED, HashTable.EMPTY):
                yield slot

    def items(self):
        for slot in self._iter_slot():
            yield (slot.key, slot.value)

    def keys(self):
        for slot in self._iter_slot():
            yield slot.key

    def values(self):
        for slot in self._iter_slot():
            yield slot.value


class SetADT(HashTable):

    def add(self, key):
        return super().add(key, True)

    def __and__(self, other):
        """a & b notice and not add"""
        new_set = SetADT()
        for element in self:
            if element in other:
                new_set.add(element)
        return new_set

    def __or__(self, other):
        """a | b"""
        new_set = SetADT()
        for element_a in self:
            new_set.add(element_a)
        for element_b in other:
            new_set.add(element_b)
        return new_set

    def __sub__(self, other):
        new_set = SetADT()
        for element in self:
            if element not in other:
                new_set.add(element)
        return new_set

    def remove(self, key):
        if key not in self:
            raise KeyError('key not found')
        else:
            super().remove(key)
            return True

    def pop(self):
        if len(self) == 0:
            raise KeyError('set is empty')
        size = len(self)
        import random
        rnum = random.randint(0, size)
        index = 1
        for key in self:
            if index == rnum:
                break
        super().remove(key)
        return key
