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
            
    def get_inorder_tree(self):  
        if not self:
            return
                   
        if self.l:
            for node in self.l.get_inorder_tree():
                yield node
        yield self
        if self.r:	
            for node in self.r.get_inorder_tree():
                yield node
        
    def copy_tree(self):          
        if self is None:
            return
            
        left = self.l.copy_tree() if (self.l is not None) else None
        right = self.r.copy_tree() if (self.r is not None) else None	
        return Tree(self.v, left, right)
    
