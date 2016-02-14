from tree import *


def convert_to_doubly_ll(tree):
    prev = None

    for node in tree.get_inorder_traversal():
        node.l = prev
        if prev is None:
            head = node
        else:
            prev.r = node
        prev = node
    return head


def print_doubly_ll(tree):
    print tree.v
    if tree.r is not None:
        print_doubly_ll(tree.r)


def main():
    a = Tree(1)
    b = Tree(4)
    c = Tree(6)
    d = Tree(8)
    e = Tree(2, a)
    f = Tree(3, e, b)
    g = Tree(7, c, d)
    h = Tree(5, f, g)

    head = convert_to_doubly_ll(h)
    print_doubly_ll(head)


if __name__ == "__main__":
    main()
