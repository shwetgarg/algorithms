import sys
from collections import deque

class Tree:	
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r
        
    def print_inorder_traversal(self):            
        if self is None:
            return
            
        if self.l is not None:
            self.l.print_inorder_traversal()
        print self.v
        if self.r is not None:
            self.r.print_inorder_traversal()
            
    def get_inorder_traversal(self):  
        if not self:
            return
                   
        if self.l:
            for node in self.l.get_inorder_traversal():
                yield node
        yield self
        if self.r:	
            for node in self.r.get_inorder_traversal():
                yield node
            
    def get_preorder_traversal(self):  
        if not self:
            return
        
        yield self	       
        if self.l:
            for node in self.l.get_preorder_traversal():
                yield node		
        if self.r:	
            for node in self.r.get_preorder_traversal():
                yield node
                
    def get_level_order_traversal(self):  
        if not self:
            return
            
        level = 0
        this_level_queue = deque([self])
        while this_level_queue:
            next_level_queue = []
            level += 1
            yield level		
            for node in this_level_queue:
                yield node
                if node.l:
                    next_level_queue.append(node.l) 
                if node.r:
                    next_level_queue.append(node.r)				 
            this_level_queue = next_level_queue
        
    def copy_tree(self):          
        if self is None:
            return
            
        left = self.l.copy_tree() if (self.l is not None) else None
        right = self.r.copy_tree() if (self.r is not None) else None	
        return Tree(self.v, left, right)
    
