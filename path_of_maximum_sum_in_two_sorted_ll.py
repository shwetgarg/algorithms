''' Given two sorted linked lists. You start with a one of the two lists and then move till the end. You may switch to the other list only at the point of intersection (which mean the two node with the same value in different lists.) You have to find the path of maximum sum '''

from llist import sllist

def get_max_path(list1, list2):
    final_list = sllist()
    templist1 = sllist()
    templist2 = sllist()
    node1 = list1.first
    node2 = list2.first
    sum1 = sum2 = 0
    
    while node1 and node2:
        if node1.value == node2.value:
            if sum1 > sum2:
                final_list.extend(templist1) 
            else:
                final_list.extend(templist2)
            final_list.append(node1)
            templist1 = sllist()
            templist2 = sllist()
            node1 = node1.next      
            node2 = node2.next     
            sum1 = sum2 = 0
        elif node1.value < node2.value:
            templist1.append(node1)
            sum1 += node1.value
            node1 = node1.next
        elif node2.value < node1.value:
            templist2.append(node2)
            sum2 += node2.value
            node2 = node2.next
    while node1:
        final_list.append(node1)
        node1 = node1.next
    while node2:
        final_list.append(node2)
        node2 = node2.next
                        
    return final_list

def main():
    list1 = sllist([1, 3, 30, 90, 120, 240, 511])
    list2 = sllist([0, 3, 12, 32, 90, 125, 240, 249])
    print get_max_path(list1, list2)
    
if __name__ == "__main__":
    main()
