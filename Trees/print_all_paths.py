from tree import Tree

def print_all_paths(node, depth = 0, path = []):
    if not node:	
        return
    
    path.append(node.v)	
    if not node.l and not node.r:	
        print path
        path.pop()
        return
        
    depth += 1
    if node.l:
        print_all_paths(node.l, depth, path)
    if node.r:
        print_all_paths(node.r, depth, path)
    path.pop()	

def main():
    a = Tree(1)
    b = Tree(4)
    c = Tree(6)
    d = Tree(8)
    e = Tree(2, a)
    f = Tree(3, e, b)
    g = Tree(7, c, d)
    h = Tree(5, f, g)

    print_all_paths(h)
    
if __name__ == "__main__":
    main()
