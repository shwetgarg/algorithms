from tree import *

def main():
    a = Tree(1)
    b = Tree(4)
    c = Tree(6)
    d = Tree(8)
    e = Tree(2, a)
    f = Tree(3, e, b)
    g = Tree(7, c, d)
    h = Tree(5, f, g)

    print "####### Inorder Traversal ########"
    Tree.print_inorder_tree(h)

    print "####### Inorder Traversal with yield ########"
    for node in Tree.get_inorder_tree(h):
        print node.v

if __name__ == "__main__":
    main()
