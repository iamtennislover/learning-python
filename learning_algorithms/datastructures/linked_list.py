class _Node:
    def __init__(self, data, prev, nex):
        # content of node
        self.data = data
        # pointers
        self.prev = prev
        self.next = nex

    def __repr__(self):
        return f"{self.prev.data if self.prev else 'None'}->Node:{self.data}->{self.next.data if self.next else 'None'}"


class DoublyLinkedList():
    def __init__(self):
        self._size = 0
        self._head: _Node = None
        self._tail: _Node = None
        self._iter_node = None

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self.size() == 0

    def clear(self):
        """Empty list - O(n)"""
        # travesing a linked list from head -> tail
        # and clearing the pointers/data
        trav = self._head
        while (trav is not None):
            _next = trav.next
            trav.next = trav.prev = trav.data = None
            trav = _next
        self._head = self._tail = None
        self._size = 0

    def add(self, elem):
        """Append elem to tail of LL - O(1)"""
        self.add_last(elem)

    def add_first(self, elem):
        """Insert elem to beginning of LL - O(1)"""
        if self.is_empty():  # since empty, given elem becomes head and tail
            self._head = self._tail = _Node(elem, None, None)
        else:  # since head already exists, given elem becomes new head
            # create new head with next=current head and
            # current head's previous=new head
            # NOTE: current head becomes node after head
            # NOTE: Keep https://www.notion.so/ammul/Coding-Interview-Tips-ba01443201884d4282d4b664ebb73ef5 in mind
            self._head.prev = _Node(elem, None, self._head)
            # assign new elem to head
            self._head = self._head.prev
        self._size += 1

    def add_last(self, elem):
        """Insert elem to end of LL - O(1)"""
        if self.is_empty():  # since empty, given elem becomes head and tail
            self._head = self._tail = _Node(elem, None, None)
        else:  # since tail already exists, given elem becomes new tail
            # create new tail with prev=current tail
            # NOTE: current tail becomes node previous to tail
            self._tail.next = _Node(elem, self._tail, None)
            # assign new elem to tail
            self._tail = self._tail.next
        self._size += 1

    def peek_first(self):
        # get value of 1st node
        if self.is_empty(): raise RuntimeError("Empty")
        return self._head.data

    def peek_last(self):
        # get value of last node
        if self.is_empty(): raise RuntimeError("Empty")
        return self._tail.data

    def remove_first(self):
        """Remove 1st node - O(1)"""
        if self.is_empty(): raise RuntimeError("Empty")
        data = self._head.data
        self._head = self._head.next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        else:
            self._head.prev = None
        return data

    def remove_last(self):
        """Remove last node - O(1)"""
        if self.is_empty(): raise RuntimeError("Empty")
        data = self._tail.data
        self._tail = self._tail.prev
        self._size -= 1
        if self.is_empty():
            self._head = None
        else:
            self._tail.next = None
        return data

    def remove_at(self, index):
        """Remove an elem at given index - O(n)"""
        if index >= self._size or index < 0: raise ValueError()
        # find index pointing to a node
        # to save time, if index closer to head, start loop from head, else tail
        if (index >= self._size / 2):
            node = self._tail
            for i in range(self._size, 0, -1):
                if index == i: break
                node = node.prev
        else:
            # start from head
            node = self._head
            for i in range(self._size):
                if index == i: break
                node = node.next
        # once node is found matching index, remove it
        return self._remove(node)

    def remove(self, elem):
        """Remove node matching given elem (i.e. data)"""
        node = self._head
        for i in range(self._size):
            if node.data == elem:
                self._remove(node)
                return True
            node = node.next

        return False

    def _remove(self, node: _Node):
        """remove a given node - O(1)"""
        # if node is head, remove it
        if node.prev == None: return self.remove_first()
        # if node is tail, remove it
        if node.next == None: return self.remove_last()
        # if node is in middle
        data = node.data
        # skip given node from its prev and next
        # e.g. removing 3 in [1,2,3,4,5]
        next_node = node.next
        prev_node = node.prev
        next_node.prev = prev_node  # 4 -> 2
        prev_node.next = next_node  # 2 -> 4
        self._size -= 1
        node.prev = node.next = node.data = None
        node = None  # clear entire node
        return data

    def index_of(self, elem):
        """get index of elem"""
        node = self._head
        for i in range(self._size):
            if node.data == elem:
                return i
            node = node.next

        return -1

    def __iter__(self):
        return self

    def __next__(self):
        if self._iter_node == None:  # set it first time
            self._iter_node = self._head
        if self.is_empty() or self._iter_node in [None, -1]:  # last iteration
            raise StopIteration
        r = self._iter_node.data
        if self._iter_node == self._tail:  # need a way to differential tail vs head
            self._iter_node = -1
        else:
            self._iter_node = self._iter_node.next
        return r

    def __repr__(self):
        if self.is_empty():
            return "EmptyList"

        # below also works:
        # s = []
        # node = self._head
        # for i in range(self._size):
        #     s.append(str(node.data))
        #     node = node.next

        s = []
        node = self._head
        while True:
            s.append(str(node.data))
            if node.next == None:
                break
            node = node.next
        x = " -> ".join(s)
        return f"DoublyLinkedList: [{x}]"

    def reverse(self):
        """Reverse in place

        logic: iterate/recurse starting from head, and only
        - set previous to next (e.g. in 0->1, 0's previous becomes 1)
        - set next to previous (e.g. in 0->1, 0's next becomes None)
        """
        n = self._head
        while n:
            p = n.prev
            n0 = str(n)
            n.prev = n.next
            n.next = p
            n = n.prev  # go left to right
            # print("xxx", n0, n)
        self._head, self._tail = self._tail, self._head
        """FAILED TO WORK
        Logic: following same logic as reversing a list by swapping opposite ends n/2 times

        Tracing:
        start list tmp_head tmp_tail (ending results)
        - [0,1,2,3,4] 0 4
        0 [4,1,2,3,0] 1 3
        1 [4,3,2,1,0] 
        '''
        tmp_head = self._head
        tmp_tail = self._tail
        for i in range(self._size // 2):
            print(i, "before", tmp_head, tmp_tail)
            before_tmp_head_prev = tmp_head.prev
            before_tmp_head_next = tmp_head.next
            before_tmp_tail_prev = tmp_tail.prev
            tmp_head.prev = tmp_head.next
            tmp_head.next = tmp_tail.next
            tmp_tail.prev = before_tmp_head_prev
            tmp_tail.next = before_tmp_tail_prev
            tmp_head = before_tmp_head_next
            tmp_tail = before_tmp_tail_prev
            print(i, "after", tmp_head, tmp_tail)
        self._head, self._tail = self._tail, self._head
        print("final", self._head, self._tail, tmp_head, tmp_tail)
        '''
        """


def main():
    d = DoublyLinkedList()
    assert str(d) == "EmptyList"
    d.add_first(20)
    assert d._head == d._tail
    #   print(d._size, d._head, d._tail, d)
    #   return
    d.add_first(10)
    #   print(d._size, d._head, d._tail, d)
    #   return
    d.add_last(30)
    print(d._size, d._head, d._tail, d)
    assert "DoublyLinkedList: [10 -> 20 -> 30]" == str(d)
    #   return
    for i in d:
        print("iterating", i)
    assert d._size == 3
    assert d.index_of(30) == 2
    d.add_last(40)
    print(d)
    assert d.remove(30)
    print(d)
    assert d.remove_at(1) == 20
    print(d)

    n = 5
    d = DoublyLinkedList()
    for i in range(n):
        d.add_last(i)
    assert str(d) == "DoublyLinkedList: [0 -> 1 -> 2 -> 3 -> 4]"
    d.reverse()
    assert str(d) == "DoublyLinkedList: [4 -> 3 -> 2 -> 1 -> 0]"
    print("COMPLETED DLL")
    return


main()
