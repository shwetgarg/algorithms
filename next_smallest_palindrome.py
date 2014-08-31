def increment_and_propogate(no, mid):
    carry = 1
    i = mid
    while(carry > 0 and i >= 0):
        carry = (no[i] + 1) / 10
        no[i] = (no[i] + 1) % 10
        i -= 1
    if i < 0 and carry > 0:
        no = [carry] + no
        
    return no
     
def get_mirror_copy(no, length):
    mid = (length-1)/2
    if length%2 == 0:
        return no[:mid+1] + no[mid::-1]	
    else:
        return no[:mid+1] + no[mid-1::-1]

def get_next_smallest_palindrome_no(no):
    no = [int(i) for i in str(no)]
    length = len(no)
    mid = (length-1)/2
    
    i = mid - 1 if length % 2 else mid
    j = mid + 1 
    while (i >= 0 and no[i] == no[j]):
        i -= 1
        j += 1
        
    if (i < 0 or no[i]  < no[j]):
        no = increment_and_propogate(no, mid)
    
    no = get_mirror_copy(no, length)
    
    return ''.join(str(i) for i in no)

def main():
    no = 12321	
    print get_next_smallest_palindrome_no(no)
    no = 123321
    print get_next_smallest_palindrome_no(no)	
    no = 99999
    print get_next_smallest_palindrome_no(no)	
    no = 999999
    print get_next_smallest_palindrome_no(no)	
    no = 243316
    print get_next_smallest_palindrome_no(no)	
    no = 24316
    print get_next_smallest_palindrome_no(no)	
    no = 213346
    print get_next_smallest_palindrome_no(no)	
    no = 21346
    print get_next_smallest_palindrome_no(no)
    
if __name__ == "__main__":
    main()
