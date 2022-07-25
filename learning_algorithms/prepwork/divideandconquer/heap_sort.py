import math
from enum import Enum


class HeapType(Enum):
    MAX = "MAX"
    MIN = "MIN"


def is_complete_binary_tree_recursive(l, n=None, i=0):
    """return true if array(l) is complete binary tree

    logic: None only allowed at the end of array with no non-null elems in between None
    check ith with i+1th. if l[i] == None and l[i+1] != None: retur False
    Time: O(n)
    """
    if n is None:
        n = len(l)
        # print(f"starting is_complete_binary_tree_recursive: {l} {n}")
    # print(f"traversing {i}")
    if i + 1 >= n:  # base condition (NOTE: picking i+1 since previous iteration will capture i>=n case)
        return True
    if l[i] == None and l[i + 1] != None:
        # print(f"BT broke at l[{i}]={l[i]}")
        return False
    return is_complete_binary_tree_recursive(l, n, i + 1)


def is_complete_binary_tree_iterative(l):
    """return true if array(l) is complete binary tree - `is_complete_binary_tree_recursive` in iteration format
    Time: O(n)
    """
    n = len(l)
    for i in range(n):
        if i + 1 >= n:  # base condition
            return True
        if l[i] == None and l[i + 1] != None:
            return False
    return True


def is_heap_recursive(l, n=None, i=0, heap_type=HeapType.MAX):
    """Navigate a given list to see if list is a heap

    For a max-heap:
    1. complete binary tree (i.e. no None/null in the middle, only allowed at the end)
    2. parent > 2 children
    """
    if n == None:  # initialize
        print(f"Starting traversing: {l} {i} {heap_type}")
        n = len(l)
        if not is_complete_binary_tree_iterative(l):
            print("not complete binary tree")
            return False
        # corner case - convert None -> smallest number
    #     smallest = 0
    #     change_null_to_smallest = False
    #     for j in range(n):
    #         if l[j] is None:
    #             change_null_to_smallest = True
    #         if l[j] is not None and l[j] < smallest:
    #             smallest = l[j]
    #     if change_null_to_smallest:
    #         print(f"smallest: {smallest}")
    #         if smallest < 0:
    #             null = smallest*2
    #         else:
    #             null = -1
    #         for j in range(n):
    #             if l[j] is None:
    #                     l[j] = null
    #         print(f"Now traversing: {l} with null: {null}")
    print(f"traversing l[{i}]={l[i] if i<n else -1}")

    # i = root
    leftchild = 2 * i + 1
    rightchild = 2 * i + 2
    # NOTE: defaulting to True since if i reach end of the tree without setting is_tree to False, i am a heap
    left_is_tree = True
    if (leftchild < n):  # if leftchild is present
        if l[leftchild] is None:  # if leaf reached, mark left is tree as True
            left_is_tree = True
        elif ((heap_type == HeapType.MAX and l[i] >= l[leftchild])
              or  # if max, parent > child, else parent < child
              (heap_type == HeapType.MIN and l[i] <= l[leftchild])):
            left_is_tree = is_heap_recursive(l, n, leftchild, heap_type)
        else:
            left_is_tree = False

    if not left_is_tree:
        print(f"left child not a heap at l[{i}]={l[i]}")
        return left_is_tree

    right_is_heap = True
    if (rightchild < n):
        if l[rightchild] is None:  # if right reached, mark left is tree as True
            right_is_heap = True
        elif ((heap_type == HeapType.MAX and l[i] >= l[rightchild])
              or (heap_type == HeapType.MIN and l[i] <= l[rightchild])):
            right_is_heap = is_heap_recursive(l, n, rightchild, heap_type)
        else:
            right_is_heap = False

    if not right_is_heap:
        print(f"right child not a heap at l[{i}]={l[i]}")

    return right_is_heap


def swap(l, i, j):
    l[i], l[j] = l[j], l[i]
    # more verbose way
    # tmp = l[i]
    # l[i] = l[j]
    # l[j] = tmp
    # print(f"swapped: l[{i}]={l[j]}, l[{j}]={l[i]} -> l[{i}]={l[i]}, l[{j}]={l[j]}")


def move_leaf_to_root_max_heap(l, i):
    """move given leaf (i) from leaf to root - done as part of heap insertion"""
    # print("move_leaf_to_root_max_heap start", l, i)
    if i <= 0:  # base condition
        return
    p = math.floor((i - 1) / 2)
    # print(i, p)
    if l[i] > l[p]:  # if leaf > parent, swap
        swap(l, i, p)
        i = p  # go to parent
    else:
        i = i - 1  # go to next leaf
    move_leaf_to_root_max_heap(l, i)
    # print("move_leaf_to_root_max_heap end", l, i)


def move_root_to_leaf_max_heap(l, i, n):
    # i represents root
    print("move_root_to_leaf_max_heap start", l, i, n)
    leftchild = 2 * i + 1
    rightchild = 2 * i + 2
    if leftchild >= n:  # base condition (picking smaller index since we want to account for situation where there is only one child)
        return
    largestchild = leftchild
    otherchild = rightchild
    if rightchild < n and l[largestchild] < l[
            rightchild]:  # we need 1st check rightchild is within the bounds and only then compare
        largestchild = rightchild
        otherchild = leftchild
    # print(f"largestchild: {largestchild}, leftchild: {leftchild}, rightchild: {rightchild}")
    if l[i] < l[largestchild]:  # if root < child, swap
        swap(l, i, largestchild)
        i = largestchild  # visit largest child
    else:
        i = otherchild
    move_root_to_leaf_max_heap(l, i, n)
    # print("move_root_to_leaf_max_heap end", l, i)


def heap_sort_using_insertion(l):
    """
    Goal: Sort using heap-sort approach
    Logic:
        0. parent = floor((i-1)/2); leftchild = 2i+1; rightchild = 2i+2
        1. build max-heap using insert operation
            a. append new elem to end of list
            b. move new elem from leaf to root by comparing with its parent and swapping
        2. remove largest elem from max-heap using remove operation
            a. swap last-elem (leaf) with largest-elem, last-elem becomes root of subtree
            b. move last-elem from root to leaf by comparing with its largest child and swapping
    
    pseudo-code
        # e.g. l=[0,1,2,3]
        n = len(l)
        mh = []
        for e in l:    # insert operation
            mh.append(e) # 1.a.
            move_leaf_to_root_max_heap(mh, len(mh)-1) # 1.b. len(mh)-1 represents leaf
        
        n = len(mh)
        for i in range(mh): # remove operation
            swap(mh, i, n-1)
            move_root_to_leaf_max_heap(mh, i, n) # 2.b. i represents root
        
        algo move_leaf_to_root_max_heap(l, i)
            # i represents leaf, always starts from end (n-1) and finishes at 0
            if i <= 0:    # base condition
                return
            p = floor((i-1)/2)
            if l[i] > l[p]: # if leaf > parent, swap
                swap(i,p)
                i = p # visit parent
            else:
                i = i - 1 # visit next parent
            move_leaf_to_root(l, i)
        
        algo move_root_to_leaf_max_heap(l, i, n)
            # i represents root
            leftchild = 2i+1; rightchild = 2i+2
            if rightchild >= n: # base condition
                return
            largestchild = leftchild
            if l[largestchild] < l[rightchild]:
                largestchild = rightchild
            if l[i] < l[largestchild]:    # if root < child, swap
                swap(l, i, largestchild)
            i = largestchild # visit largest child
            move_root_to_leaf_max_heap(l, i, n)
            
    Time: O(nlogn)
    Space: O(n) - since its creating a new list to store max-heap
    For faster and cleaner approach: use heapify as used in `heap_sort_using_heapify`
    """
    mh = []  # max-heap
    for e in l:
        mh.append(e)
        move_leaf_to_root_max_heap(mh, len(mh) - 1)  # move e from leaf -> root
    # print("max-heap built", mh)
    assert is_heap_recursive(mh)
    n = len(mh)
    for lasti in range(
            n - 1, -1, -1
    ):  # remove operation from root to leaf where the size of heap reduces in each iteration
        # NOTE: we start at n-1 because for 1st iteration after the swap, the size of heap is reduced by 1
        # NOTE: lasti also indicates the lenght we want of heap
        root = 0  # root is always the 1st elem, since we will be removing it one by one and putting it at the end
        # print(f"swapping {mh[root]} with {mh[lasti]} mh[{lasti}]")
        swap(mh, lasti, root)
        move_root_to_leaf_max_heap(l=mh, i=root,
                                   n=lasti)  # 2.b. i represents root
        # print("tmp mh", mh)
    return mh


def heapify(l, n, i):
    """For given root (i) move root -> leaf to ensure at the end we have max-heap
    Logic:
    Same as `move_root_to_leaf_max_heap`
    Time: O(n)
    """
    lc = 2 * i + 1  # left-child
    rc = 2 * i + 2  # right-child

    # NOTE: base condition is not of (lc < n; rc < n)
    rooti = i  # default next root to be current root
    if lc < n and l[i] < l[lc]:  # if root < left-child
        rooti = lc  # new root should be left-child
    if rc < n and l[rooti] < l[rc]:  # if new root < right-child
        rooti = rc  # new root should be right-child
    if rooti != i:  # if new root is different from current root
        swap(l, rooti, i)
        heapify(l, n, rooti)  # visit new root


def heap_sort_using_heapify(l):
    """This approach compared to `heap_sort_using_insertion`
    follows heapify approach as explained in
    https://www.notion.so/ammul/2-6-3-Heap-Heap-Sort-2f398aa1d4d34ecf923ca2deaddc7599#96b4e496656543beb18567aef7f24b4d

    Overall logic:
    1. navigate leaf (right) -> root (left) (i.e. in reverse) and for each elem as root of subtree,
    perform remove operation by moving elem from root -> leaf
    (i.e. `move_root_to_leaf_max_heap` or what was done during remove operation) to build max-heap 1st.
    2. similar to remove operation, swap 1st elem with last elem and perform heapify to ensure
    max-heap is built.

    Main difference compared to `heap_sort_using_insertion`:
    1. heap_sort_using_insertion uses insertion which requires O(n) space
    2. heap_sort_using_insertion traverses root -> leaf to build max-heap

    Time taken: O(nlogn)
    """
    # 1. navigate leaf -> to build max-heap:
    # since we navigate from leaf -> root, and we need to heapify each elem,
    # we can skip the lowest level since they are already heapified (since they are leafs)
    n = len(l)
    last_leaf = n - 1  # NOTE: we need to start from parent of last leaf to save iterations
    parent_of_last_leaf = math.floor((last_leaf - 1) / 2)
    # print(f"starting heapsort for l: {l} n: {n} parent_of_last_leaf: {parent_of_last_leaf}")
    for i in range(
            parent_of_last_leaf, -1, -1
    ):  # go backward right -> left (or leaft -> root) until top 0 (including top root=0)
        # print(f"navigating l[{i}]={l[i]}")
        heapify(l, n, i)
    # print(f"resulting in-place max-heap: {l}")

    # 2. for each root (0), swap with last elem and heapify
    # NOTE: since we need to swap with last elem, reverse loop
    # NOTE: no need for lasti to be 0 since swap with itself won't do anything
    for lasti in range(last_leaf, 0, -1):
        swap(l, 0, lasti)
        heapify(l, lasti, i)
    # print(f"resulting in-place sorted max-heap: {l}")


def test_heap_sort():
    testcases = [
        [2, 3, 4],
        [1, 1, 1],
        [3, 2, 1, 0],
        [5, 1, 2, 4],
        [11, 1, 10, 10],
        [5, 6, 10, 20, 30, 50, 11],
        [1, 2, 3, 0],
    ]
    for l in testcases:
        # r = heap_sort_using_insertion(l)
        # assert r == sorted(l)
        heap_sort_using_heapify(l)
        original_l = l[:]
        # print("result", original_l, l, sorted(l), original_l == sorted(l))
        assert l == sorted(original_l)


def test_navigate_heap():
    testcases = [
        ([1, 2, 3, None], True),
        ([1, None, None, None], True),
        ([1, None, 2, None], False),
        ([1, None, None, None, 2], False),
        ([1, None], True),
        ([None, 1], False),
        ([2, None, None, 1], False),
        ([2, None, None, None, 1], False),
        ([2, None, 1, None], False),
        ([2, None, None, 1, None], False),
        ([1], True),
        ([None], True),
    ]
    for l, expected in testcases:
        r = is_complete_binary_tree_recursive(l)
        assert r == expected
        r = is_complete_binary_tree_iterative(l)
        assert r == expected

    testcases = [
        ([50, 30, 20, 10, 11, 5, 6], HeapType.MAX, True),  # good case
        ([50, 30, 20, 10, 11, 5, 60], HeapType.MAX, False),  # bad case
        ([1, 30, 20, 10, 11, 5, 60], HeapType.MAX, False),  # bad case
        ([50, 30, 1, 10, 11, 5], HeapType.MAX, False),  # bad case
        ([50, 30, 20, 10, 11, 5,
          None], HeapType.MAX, True),  # corner good case
        ([50, 30, 20, 10, 11, -5,
          None], HeapType.MAX, True),  # corner good case
        ([50, 30, 20, None, None, None,
          None], HeapType.MAX, True),  # corner good case
        ([50, 30, 20, None, 11, 5, 6], HeapType.MAX, False),  # corner bad case
        ([50, 30, 20, 10, 11, 5, 6], HeapType.MIN, False),  # good case
        ([10, 20, 30, 21, 22, 31, None], HeapType.MIN, True),  # good case
    ]
    for l, heap_type, expected in testcases:
        r = is_heap_recursive(l, heap_type=heap_type)
        assert r == expected


def main():
    # test_navigate_heap()
    test_heap_sort()


main()
