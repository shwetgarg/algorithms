from tree import Tree

def main():
    a = Tree(1)
    b = Tree(4)
    c = Tree(6)
    d = Tree(8)
    e = Tree(2, a)
    f = Tree(3, e, b)
    g = Tree(7, c, d)
    h = Tree(5, f, g)

    print "####### Left View ########"
    print_next = False
    for node in Tree.get_level_order_traversal(h):
        if not isinstance(node, Tree):
            print_next = True
        elif print_next:
            print node.v
            print_next = False
            
    print "####### Right View ########"
    prev = None
    for node in Tree.get_level_order_traversal(h):
        if not isinstance(node, Tree) and prev:
            print prev.v
        prev = node
    print node.v
            
if __name__ == "__main__":
    main()
