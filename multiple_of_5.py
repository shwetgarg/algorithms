import sys

def is_power_of_five(decimal_no):
    while (((decimal_no % 5) == 0) and decimal_no > 1):    # While x is even and > 1 
        decimal_no /= 5
    return (decimal_no == 1)

def boolean_to_decimal(no):
    decimal_no = 0
    for digit in no:
        if int(digit):
            decimal_no = decimal_no * 2 + 1
        else:
            decimal_no = decimal_no * 2
            
    return decimal_no

def main(argv):
    no = argv[0]
    length = len(no)

    M = [[0]*length for i in range(length)]
    for i in range(length):
        for j in range(length-i):
            print int(no[j:j+i+1])
            decimal_no = boolean_to_decimal(no[j:j+i+1])
            print decimal_no
            M[i][j] = is_power_of_five(decimal_no)
            print M[i][j]
        
    print M

if __name__ == "__main__":
    main(sys.argv[1:])
