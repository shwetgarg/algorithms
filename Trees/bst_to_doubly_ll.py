from tree import *

class BstToDoublyLinkedList(Tree):
    def convert_to_doubly_ll(self):
        prev = None

        for node in self.get_inorder_tree():
            node.l = prev
            if prev is None:
                head = node
            else:
                prev.r = node
            prev = node
        return head
    
    def print_doubly_ll(self):
        print self.v
        if self.r is not None:
            self.r.print_doubly_ll()
    

def main():
    a = BstToDoublyLinkedList(1)
    b = BstToDoublyLinkedList(4)
    c = BstToDoublyLinkedList(6)
    d = BstToDoublyLinkedList(8)
    e = BstToDoublyLinkedList(2, a)
    f = BstToDoublyLinkedList(3, e, b)
    g = BstToDoublyLinkedList(7, c, d)
    h = BstToDoublyLinkedList(5, f, g)
    
    head = h.convert_to_doubly_ll()
    head.print_doubly_ll()

if __name__ == "__main__":
    main()
