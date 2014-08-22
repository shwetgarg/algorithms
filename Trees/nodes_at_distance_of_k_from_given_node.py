''' Find all the Node at the distance K from a given node in a Binary tree. Print them in any order.'''

from tree import *

def get_nodes_at_distance_k(node, k):
    if (k == 0):
        return [node.v]
    
    left_nodes = get_nodes_at_distance_k(node.l, k-1) if node.l else []
    right_nodes = get_nodes_at_distance_k(node.r, k-1) if node.r else []
    return left_nodes + right_nodes

def main():	
    a = Tree(1)
    b = Tree(4)
    c = Tree(6)
    d = Tree(8)
    e = Tree(2, a)
    f = Tree(3, e, b)
    g = Tree(7, c, d)
    h = Tree(5, f, g)
    print get_nodes_at_distance_k(h, 2)
    print get_nodes_at_distance_k(a, 2)
    print get_nodes_at_distance_k(e, 1)

if __name__ == "__main__":
    main()
