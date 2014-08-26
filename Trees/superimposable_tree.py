import sys
from tree import *

class SuperimposableTree(Tree):
    def get_superimposable_tree(n1, n2):
        if n1 is None and n2 is None:
            return None
        elif n1 is not None and n2 is not None and n1.v == n2.v:
            left = None
            right = None
            if (n1.l):
                left = SuperimposableTree.get_superimposable_tree(n1.l, n2.l)
            elif (n2.l):
                left = SuperimposableTree.get_superimposable_tree(n2.l, n1.l)
            if (n1.r):
                right = SuperimposableTree.get_superimposable_tree(n1.r, n2.r)
            elif (n2.r):
                right = SuperimposableTree.get_superimposable_tree(n2.r, n1.r)
            if left != "error" and right != "error":
                return Tree(n1.v, left, right)
            else:
                return "error"
        elif n1 is not None and n2 is not None and n1.v != n2.v:
            return "error"
        elif n1 is None:
            return n2.copy_tree()
        elif n2 is None:
            return n1.copy_tree()
                
def main():
    print "####### Case 1: #########"
    a1 = SuperimposableTree(2)
    b1 = SuperimposableTree(1, a1)

    a2 = SuperimposableTree(5)
    b2 = SuperimposableTree(1, None, a2)

    new_tree = SuperimposableTree.get_superimposable_tree(b1, b2)
    print ".....Tree 1....."
    b1.print_inorder_traversal()
    print ".....Tree 2....."
    b2.print_inorder_traversal()	
    print "....Superimposed Tree...."
    if new_tree != "Not Superimposable":
        new_tree.print_inorder_traversal()
    else:
        print "error"
        
    print "\n####### Case 2: #########"
    a1 = SuperimposableTree(1)
    b1 = SuperimposableTree(5, a1)

    a2 = SuperimposableTree(5)
    b2 = SuperimposableTree(2, None, a2)

    new_tree = SuperimposableTree.get_superimposable_tree(b1, b2)
    print ".....Tree 1....."
    b1.print_inorder_traversal()
    print ".....Tree 2....."
    b2.print_inorder_traversal()	
    if new_tree != "error":
        print "....Superimposed Tree...."
        new_tree.print_inorder_traversal()
    else:
        print "Not Superimposable Tree"

if __name__ == "__main__":
    main()
