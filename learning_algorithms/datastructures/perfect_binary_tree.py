"""https://www.programiz.com/dsa/perfect-binary-tree

https://www.notion.so/ammul/Binary-Tree-and-Binary-Search-Tree-DS-6a41bfb93bd349c7a61db606d779a366#a1028e3fa1bf4bbfa79a6d68cf431ec4
"""


class Node:
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

    def __repr__(self):
        return f"Node({self.v},l={self.l.v if self.l else None},r={self.r.v if self.r else None})"


def get_tree_depth_for_perfect_bt(root: Node) -> int:
    """Simply use left-most node to find depth of tree. idea is that if we find a none value, we know the dept
    e.g. for [1,2,3], depth is 2
    aka returns total no. of levels
    """
    d = 0
    n = root
    while n:
        n = n.l
        d += 1
    print(f"for root {root} depth is {d}")
    return d


def is_perfect_bt(root: Node, total_levels: int, root_level: int):
    """This works for all cases
    Basic logic is:
    1. if both children are null (can only happen when its leaf level)
    2. and leaf level + 1 == total level
    """
    print(
        f"navigating {root} with total_levels: {total_levels}, current root_level: {root_level}"
    )
    if root is None:
        return True
    if root.l is None and root.r is None:
        # if both child are leaf AND current level + 1 == total levels, its a perfect-bt
        leaf_level = root_level
        return total_levels == leaf_level + 1
    if root.l is None or root.r is None:
        # if only 1 child is leaf, its not a perfect-bt
        return False
    return is_perfect_bt(root.l, total_levels,
                         root_level + 1) and is_perfect_bt(
                             root.r, total_levels, root_level + 1)


def is_perfect_bt_fails_on_complete_bt(root: Node):
    """This works for all case but fails if BT is a complete BT - e.g. [1,2,3,4,5,None,None]
    Fixed in is_perfect_bt()"""
    print(f"navigating {root}")
    if root is None:
        return True
    if root.l is None and root.r is None:
        # if both child are leaf, its a perfect-bt
        return True
    if root.l is None or root.r is None:
        # if only 1 child is leaf, its not a perfect-bt
        return False
    return is_perfect_bt_fails_on_complete_bt(
        root.l) and is_perfect_bt_fails_on_complete_bt(root.r)


def main():
    print("running perfect_binary_tree")
    cases = (
        (True, "[1,2,3,4,5,6,7] - perfect",
         Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))),
        (False, "[1,None,3,4,5,6,7] - not perfect",
         Node(1, None, Node(3, Node(5), Node(6)))),
        (False, "[1,2,3,4,5,None,None] - not perfect - complete BT",
         Node(1, Node(2, Node(4), Node(5)), Node(3))),
        (True, "[1] - perfect", Node(1)),
        (False, "[1,2] - not perfect", Node(1, Node(2))),
    )
    for expected, description, root in cases:
        found = is_perfect_bt(root, get_tree_depth_for_perfect_bt(root), 0)
        print(f"case: '{description}' - root {root} is perfect: {found}")
        assert found == expected


main()
