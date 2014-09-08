from tree import Tree

def sum_path(sum, node):
    l_val , r_val = None, None
    
    if not node:
        return
        
    if not node.l and not node.r:		
        return sum + node.v, node
    if node.l:
        l_val = sum_path(sum + node.v, node.l)
    if node.r:	
        r_val = sum_path(sum + node.v, node.r)
    
    return max(l_val,r_val)
    
def print_tree(node, leaf_node):
    if not node:
        return 
        
    if not node.l and not node.r and node == leaf_node:
        return [node.v]
    elif not node.l and not node.r:
        return 
    
    if node.l:	
        left = print_tree(node.l, leaf_node)
        if left:
            left.append(node.v) 
            return left
    if node.r:
        right = print_tree(node.r, leaf_node)
        if right:
            right.append(node.v) 
            return right

def main():
    a = Tree(1)
    b = Tree(4)
    c = Tree(6)
    d = Tree(8)
    e = Tree(2, a)
    f = Tree(3, e, b)
    g = Tree(7, c, d)
    h = Tree(5, f, g)

    node_sum, node = sum_path(0, h)
    
    path = print_tree(h, node)
    print path
    
if __name__ == "__main__":
    main()
