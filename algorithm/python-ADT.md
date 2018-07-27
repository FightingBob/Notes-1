# 算法复杂度

## 时间复杂度

## 空间复杂度

## 基础示例


# python ADT / 抽象数据结构

## Array

### 图示

![](https://ds055uzetaobb.cloudfront.net/image_optimizer/7bfe2713ecaf427164d14018608b826ffbeea531.jpg)

### 方法/时间复杂度

- \_\_swetitem__
- \_\_getitem__
- clear()
- in
- iter
- len()


### 代码

```python
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
```

### 单元测试

```python
def test_array():
    size = 10
    array = Array(size)
    array[0] = 1
    array[1] = 3
    array[2] = 4

    assert array[0] == 1
    assert 1 in array

    array.clear()
    assert array[0] is None
```

### 应用场景


## linked list

### 图示
![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/612px-Singly-linked-list.svg.png)

### 方法

### 代码

```python
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
```

### 单元测试

```python
def test_linked_list():
    ll = LinkedList()
    ll.append(0)
    ll.append(1)
    ll.append(2)

    assert len(ll) == 3
    ll.appendleft(3)
    assert list(ll) == [3, 0, 1, 2]

    ll.remove(0)
    assert list(ll) == [3, 1, 2]
    assert ll.find(3) == 0
    assert ll.find(0) == -1

    assert ll.pop() == 2
    assert list(ll) == [3, 1]

    assert ll.popleft() == 3
    assert list(ll) == [1]

    ll.clear()
    assert list(ll) == []
    ll = LinkedList()
    ll.append(1)
    ll.popleft()
    assert list(ll) == []

    ll = LinkedList(maxsize=2)
    ll.append(1)
    ll.append(2)
    try:
        ll.append(3)
    except Exception:
        assert 1
    else:
        assert 0
```

### 应用场景

## double liked list

### 图示

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Doubly-linked-list.svg/915px-Doubly-linked-list.svg.png)

### 方法

### 代码

```python
class Node:

    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next


class CycleDoubleLinkedList:

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('cycle double linked list is full')
        node = Node(value=value)
        tailnode = self.tailnode()
        self.root.prev = node
        tailnode.next = node
        node.next = self.root
        node.prev = tailnode
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('cycle double linked list is full')
        node = Node(value=value)
        if self.root.next is self.root:
            self.root.next = node
            self.root.prev = node
            node.prev = self.root
            node.next = self.root
        else:
            headnode = self.headnode()
            self.root.next = node
            node.prev = self.root
            node.next = headnode
            headnode.prev = node
        self.length += 1

    def remove(self, node):
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1
            return node

    def iter_node(self):
        if self.root.next is self.root:
            return
        currnode = self.root.next
        while currnode.next is not self.root:
            yield currnode
            currnode = currnode.next
        yield currnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        if self.root.prev is self.root:
            return
        currnode = self.root.prev
        while currnode.prev is not self.root:
            yield currnode
            currnode = currnode.prev
        yield currnode
```

### 单元测试

```python
def test_double_link_list():
    dll = CycleDoubleLinkedList()

    assert len(dll) == 0
    dll.append(0)
    dll.append(1)
    dll.append(2)

    assert dll.length == 3

    assert len(dll) == 3
    assert list(dll) == [0, 1, 2]
    headnode = dll.headnode()
    dll.remove(headnode)

    assert len(dll) == 2
    assert list(dll) == [1, 2]
    dll.appendleft(9)

    assert len(dll) == 3
    assert list(dll) == [9, 1, 2]

    assert [node.value for node in dll.iter_node()] == [9, 1, 2]
    assert [node.value for node in dll.iter_node_reverse()] == [2, 1, 9]
    d = CycleDoubleLinkedList()

    assert list(d) == []
    assert d.headnode() == d.root.next
    assert d.tailnode() == d.root.prev

    d = CycleDoubleLinkedList(maxsize=2)
    d.append(0)
    d.append(1)
    try:
        d.append(3)
    except Exception:
        assert 1
    else:
        assert 0

```

### 应用场景

## queue / FIFO

### 图示

![](http://blog.longjiazuo.com/wp-content/uploads/2017/05/11-94.png)

### 方法


### 代码

```python
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
```

### 单元测试

```python
def test_queue():
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)

    assert len(queue) == 3
    assert queue.pop() == 3
    assert queue.pop() == 2
    assert queue.pop() == 1

    queue = Queue(maxsize=2)
    queue.push(1)
    queue.push(2)

    with pytest.raises(FullError) as excinfo:
        queue.push(3)

    assert "Full" in str(excinfo)

    queue.pop()
    queue.pop()

    with pytest.raises(EmptyError) as excinfo:
        queue.pop()

    assert "empty" in str(excinfo)

```

### 应用场景

## deque

### 图示

### 方法

### 代码

```python
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

```

### 单元测试

```python
def test_deque():
    cdll = Deque(3)

    cdll.append(1)
    cdll.append(2)
    cdll.appendleft(3)

    assert len(cdll) == 3

    with pytest.raises(Exception) as excinfo:
        cdll.append(4)

    assert 'full' in str(excinfo)
    assert cdll.pop() == 2
    assert cdll.pop() == 1
    assert cdll.pop() == 3

    with pytest.raises(Exception) as excinfo:
        cdll.pop()

    assert 'empty' in str(excinfo)

    cdll.appendleft(1)
    cdll.appendleft(2)
    cdll.appendleft(3)

    assert cdll.popleft() == 3
    assert cdll.popleft() == 2
    assert cdll.popleft() == 1

    with pytest.raises(Exception) as excinfo:
        cdll.pop()

    assert 'empty' in str(excinfo)
```

### 应用场景

## Stack / LIFO

### 图示

### 方法

### 代码

```python
class Stack(Deque):
    """lifo: last in first out"""

    def push(self, value):
        self.append(value)

    def pop(self):
        return super().pop()

    def is_empty(self):
        return len(self) == 0
```

### 单元测试

```python
def test_stack():
    s = Stack(3)
    s.push(1)
    s.push(2)
    s.push(3)

    assert len(s) == 3

    with pytest.raises(Exception) as excinfo:
        s.push(4)

    assert 'full' in str(excinfo)
    assert s.pop() == 3
    assert not s.is_empty()
    assert s.pop() == 2
    assert s.pop() == 1

    with pytest.raises(Exception) as excinfo:
        s.pop()

    assert 'empty' in str(excinfo)
    assert s.is_empty()
    assert len(s) == 0

```
### 应用场景

## HashTable

### 图示

### 方法

### 代码

```python
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
```

### 单元测试

```python
def test_hashtable():
    h = HashTable()

    assert len(h) == 0

    h.add(1, 1)
    h.add(2, 1)
    h.add(3, 1)
    h.add(4, 1)

    assert sorted(list(h)) == [1, 2, 3, 4]

    assert len(h)
    assert 1 in h
    assert 2 in h
    assert 3 in h
    assert 4 in h

    h.remove(1)

    assert len(h) == 3
    assert h.remove(2) == 1
    assert h.remove(3) == 1
    assert h.remove(4) == 1
    assert len(h) == 0

    for i in range(50):
        h.add(i, i)

    assert sorted(list(h)) == list(range(50))

    assert len(h) == 50
    assert 1 in h
    assert 2 in h
    assert 3 in h
    assert 4 in h
    assert 5 in h
    assert 6 in h
    assert 7 in h
    assert 8 in h

    assert h.get(1) == 1
    assert h.get(3) == 3
    assert h.get(4) == 4
    assert h.get(5) == 5
    assert h.get(5, 6) == 5
    assert h.get(50, 6) == 6

    assert h.remove(1) == 1
    assert h.remove(2) == 2
    assert h.remove(3) == 3
    assert h.remove(4) == 4
    assert h.remove(5) == 5
    assert h.remove(6) == 6
    assert h.remove(7) == 7
    assert h.remove(8) == 8

    with pytest.raises(KeyError) as excinfo:
        h.remove(51)

    assert 'key not found' in str(excinfo)
```

### 应用场景

## dict

### 图示

### 方法

### 代码

```python
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
```

### 单元测试

```python
def test_dict():
    d = DictADT()
    d.add(1, 2)
    d.add(2, 3)
    d.add(3, 5)

    assert d[1] == 2
    assert d[2] == 3
    assert d[3] == 5

    assert (1, 2) in list(d.items())
    assert 5 in list(d.values())
    assert 1 in list(d.keys())

    for i in range(5, 20):
        d.add(i, i)

    for i in range(5, 20):
        assert d[i] == i

    d.remove(1)

    with pytest.raises(KeyError) as excinfo:
        d[1]

    assert 'key not found' in str(excinfo)
```

### 应用场景

## set

### 图示

### 方法

### 代码

### 单元测试

### 应用场景
