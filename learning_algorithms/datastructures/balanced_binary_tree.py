"""
https://www.programiz.com/dsa/balanced-binary-tree

"""


class Node:
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r
        self.h = 0  # height

    def __repr__(self):
        return f"Node({self.v},l={self.l.v if self.l else None},r={self.r.v if self.r else None})"


def is_balanced_tree(root: Node) -> bool:
    """
    Logic:
    1. calculate height for each node - defaults to 0
    2. use post-order traversal to calculate height beginning with leaf 1st and root last
    3. node height = max(left + right) + 1 # +1 because each level is difference of 1
    4. finally, use the height to check if difference b/w left and right is <= 1

    """
    if root is None:
        return True

    balanced_l = is_balanced_tree(root.l)
    balanced_r = is_balanced_tree(root.r)
    lh = root.l.h if root.l else 0
    rh = root.r.h if root.r else 0
    root.h = max(lh, rh) + 1
    print(f"root {root} height is {root.h}")
    if abs(lh - rh) <= 1:
        return balanced_l and balanced_r

    return False


def main():
    cases = (
        [
            True, "[1,2,3,4,5,6,7]",
            Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
        ],
        [True, "[1,2,3,4]",
         Node(1, Node(2, Node(4)), Node(3))],
        [
            False, "[1,2,None,4,None,None,None,8]",
            Node(1, Node(2, Node(4, Node(8))))
        ],
        [
            False, "[1,2,3,4,5,None,None,None,None,10]",
            Node(1, Node(2, Node(4), Node(5, Node(10))), Node(3))
        ],
    )
    for expected, description, root in cases:
        r = is_balanced_tree(root)
        print(f"root {root} is perfect: {r}")
        assert r == expected


main()
