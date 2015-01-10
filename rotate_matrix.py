import numpy as np

def rotate(a):
    a = a.T
    b=np.matrix([[]])
    columns = np.shape(a)[1]
    for i in xrange(columns-1,-1, -1):
        b.append(a[i])
    return b

def main():
    a = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
    print a
    a = rotate(a)
    print a
    
if __name__ == "__main__":
    main()
