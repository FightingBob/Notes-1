import pytest

from adt import Array, Bag, EmptyError, FullError, \
    LinkedList, Queue, ArrayQueue, Deque, Stack, \
    ArrayStack, CollectionDequeStack, HashTable, \
    DictADT, SetADT
from double_link_list import CycleDoubleLinkedList


def test_bag():
    bag = Bag()

    bag.add(1)
    bag.add(2)
    bag.add(3)
    assert len(bag) == 3
    bag.remove(2)
    assert len(bag) == 2
    for i in bag:
        assert i == 1 or 3


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


def test_array_queue():
    aq = ArrayQueue(3)
    aq.push(1)
    aq.push(2)
    aq.push(3)

    assert len(aq) == 3

    with pytest.raises(FullError) as excinfo:
        aq.push(4)

    assert 'full' in str(excinfo)
    assert aq.pop() == 1
    assert aq.pop() == 2
    assert aq.pop() == 3

    with pytest.raises(EmptyError) as excinfo:
        aq.pop()

    assert 'empty' in str(excinfo)
    assert len(aq) == 0


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


def test_array_stack():
    s = ArrayStack(3)
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


def test_deque_stack():
    s = CollectionDequeStack(3)
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


def test_set():
    s = SetADT()
    s.add(1)
    s.add(1)
    s.add(1)
    s.add(2)
    s.add(2)
    s.add(2)
    s.add(3)

    assert sorted(list(s)) == [1, 2, 3]

    s2 = SetADT()
    s2.add(1)
    s2.add(4)
    s2.add(5)

    assert sorted(list(s & s2)) == [1]
    assert sorted(list(s | s2)) == [1, 2, 3, 4, 5]
    assert sorted(list(s - s2)) == [2, 3]

    s.remove(3)
    assert 3 not in s

    assert s.pop()
    assert s.pop()

    with pytest.raises(KeyError) as excinfo:
        s.pop()

    assert 'empty' in str(excinfo)
