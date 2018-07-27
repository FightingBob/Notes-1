#  BUGLAN


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
