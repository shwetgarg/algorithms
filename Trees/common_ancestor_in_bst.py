from tree import *


def get_common_ancestor(tree, v1, v2):
    if not tree:
        return

    if tree.v < v1 and tree.v < v2:
        if tree.r: return get_common_ancestor(tree.r, v1, v2)
    elif tree.v > v1 and tree.v > v2:
        if tree.l: return get_common_ancestor(tree.l, v1, v2)
    else:
        return tree


def main():
    a = Tree(1)
    b = Tree(4)
    c = Tree(6)
    d = Tree(8)
    e = Tree(2, a)
    f = Tree(3, e, b)
    g = Tree(7, c, d)
    h = Tree(5, f, g)

    node = get_common_ancestor(h, 1, 4)
    if node: print node.v


if __name__ == "__main__":
    main()
