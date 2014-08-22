import sys

class Tree:	
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r
        
    def print_inorder_tree(self):            
        if self is None:
            return
            
        if self.l is not None:
            self.l.print_inorder_tree()
        print self.v
        if self.r is not None:
            self.r.print_inorder_tree()
            
    def copy_tree(self):          
        if self is None:
            return
            
        left = self.l.copy_tree() if (self.l is not None) else None
        right = self.r.copy_tree() if (self.r is not None) else None
        
        return Tree(self.v, left, right)
