def max_heapify(l, n, i):
    '''
    send root -> leaf by swapping root with largest child
    '''
    print(f"heapifying {l}/{n}/{i}")
    largesti = i
    li = 2 * i + 1
    ri = 2 * i + 2
    if li < n and l[li] > l[largesti]:
        largesti = li
    if ri < n and l[ri] > l[largesti]:
        largesti = ri
    if largesti != i:
        print(f"swapping {largesti}({l[largesti]}) with {i}(l[i])")
        l[i], l[largesti] = l[largesti], l[i]
        max_heapify(l, n, largesti)


def min_heapify(l, n, i):
    '''
    send root -> leaf by swapping root with smallest child
    '''
    print(f"heapifying {l}/{n}/{i}")
    smallesti = i
    li = 2 * i + 1
    ri = 2 * i + 2
    if li < n and l[li] < l[smallesti]:
        smallesti = li
    if ri < n and l[ri] < l[smallesti]:
        smallesti = ri
    if smallesti != i:
        print(f"swapping {smallesti}({l[smallesti]}) with {i}(l[i])")
        l[i], l[smallesti] = l[smallesti], l[i]
        min_heapify(l, n, smallesti)


def is_heap(l, max_heap=True):
    n = len(l)
    for i in range(n):
        li = 2 * i + 1
        ri = 2 * i + 2
        if max_heap:
            if (li < n and l[i] < l[li]) or (ri < n and l[i] < l[ri]):
                return False
        else:
            if (li < n and l[i] > l[li]) or (ri < n and l[i] > l[ri]):
                return False
    return True


def build_heap(l, max_heap=True):
    n = len(l)
    for i in range(int(n / 2) - 1, -1, -1):
        if max_heap:
            max_heapify(l, n, i)
        else:
            min_heapify(l, n, i)


def delete(l: list, e, max_heap=True):
    n = len(l)
    i = l.index(e)
    if i == -1:
        return False
    if i >= int(n / 2):
        print("removing leaf")
        return l.remove(e)
    else:
        print(f"swapping with leaf {l[-1]}")
        l[-1], l[i] = l[i], l[-1]
        v = l.pop()
        build_heap(l, max_heap=max_heap)
        return v


def heap_sort(l):
    build_heap(l, max_heap=True)
    n = len(l)
    for i in range(n - 1, 0, -1):
        rooti = 0
        l[rooti], l[i] = l[i], l[rooti]
        max_heapify(l, n=i, i=rooti)


def main():
    l = [10, 20, 15, 12, 40, 25, 18]
    build_heap(l)
    assert l == [40, 20, 25, 12, 10, 15, 18]

    l = [10, 20, 15, 12, 40, 25, 18]
    build_heap(l, max_heap=False)
    assert l == [10, 12, 15, 20, 40, 25, 18]

    l = [10, 20, 15, 12, 40, 25, 18]
    assert is_heap(l) is False
    l = [40, 20, 25, 12, 10, 15, 18]
    assert is_heap(l) is True
    l = [10, 20, 30, 40]
    assert is_heap(l) is False

    l = [10, 20, 15, 12, 40, 25, 18]
    build_heap(l, max_heap=True)
    assert l == [40, 20, 25, 12, 10, 15, 18]
    assert delete(l, 25) == 25
    assert is_heap(l)

    l = [10, 20, 15, 12, 40, 25, 18]
    l = [30, 20, 50, 100, 1]
    heap_sort(l)
    assert l == sorted(l)
    print("COMPLETED")


main()
