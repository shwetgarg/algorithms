from tree import Tree

def get_tree(ino, pre):
    if len(ino) <= 0:
        return

    for i in range(len(ino)):
        if ino[i] == pre[0]:
            break;

    return Tree(ino[i], get_tree(ino[:i], pre[1:i+1]), get_tree(ino[i+1:], pre[i+1:]))

def main():
    ino = ['g', 'd', 'h', 'b', 'e', 'i', 'a', 'f', 'j', 'c']
    pre = ['a', 'b', 'd', 'g', 'h', 'e', 'i', 'c', 'f', 'j']
    
    root = get_tree(ino, pre)
    root.print_inorder_traversal()

if __name__ == "__main__":
    main()

