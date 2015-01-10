import sys
import numpy as np

a=[]
length_pos=0
length_neg=0

while 1:
    try:
        no = int(sys.stdin.readline())
        a.append(no)
        if (no >= 0):
            length_pos+=1
        else:
            length_neg+=1
    except KeyboardInterrupt:
        break
a = sort(a,length_pos,length_neg)
print a


def sort(a,length_pos,length_neg):
    if (length_pos==0 or length_neg==0)
        return a
        
    neg_index=0
    pos_index=length_neg	
    i=0	
    temp_index=pos_index
    temp=a[pos_index]
    

    
    while (i<(length_neg) and (neg_index<length_neg or pos_index<length_pos)):	
        if (a[i] < 0):
            neg_index += 1
        else:
            while(temp>=0)
            
    print "\n" + str(length_pos)
    print a


