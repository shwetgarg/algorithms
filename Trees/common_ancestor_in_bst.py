from tree import *

class CommonAncestor(Tree):
    def get_common_ancestor(self, v1, v2):
        if not self:
            return
        
        if self.v < v1 and self.v < v2:
            if self.r:	return self.r.get_common_ancestor(v1, v2)
        elif self.v > v1 and self.v > v2:
            if self.l: return self.l.get_common_ancestor(v1, v2)
        else: return self	
        
def main():
    a = CommonAncestor(1)
    b = CommonAncestor(4)
    c = CommonAncestor(6)
    d = CommonAncestor(8)
    e = CommonAncestor(2, a)
    f = CommonAncestor(3, e, b)
    g = CommonAncestor(7, c, d)
    h = CommonAncestor(5, f, g)
    
    node = h.get_common_ancestor(1, 4)
    if node: print node.v 
    
if __name__ == "__main__":
    main()
