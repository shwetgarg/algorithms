def find_first_decreasing_no_from_end(no, length):
    current = 0	
    pos_of_decreasing_no = 1

    for i in reversed(no):
        if int(i) < current:
            first_decreasing_no_from_end = int(i)
            pos_of_decreasing_no = length - pos_of_decreasing_no
            break
        current = int(i)
        pos_of_decreasing_no += 1
        
    return first_decreasing_no_from_end, pos_of_decreasing_no

def arrange_digits_in_correct_order(no, length, first_decreasing_no_from_end, pos_of_decreasing_no):
    pos_of_just_bigger_digit = 1
    for i in reversed(no):
        if int(i) > first_decreasing_no_from_end:
            pos_of_just_bigger_digit = length - pos_of_just_bigger_digit
            no[pos_of_decreasing_no], no[pos_of_just_bigger_digit] = no[pos_of_just_bigger_digit], no[pos_of_decreasing_no]
            break
        pos_of_just_bigger_digit += 1

    pos_of_decreasing_no += 1
    
    pos_of_just_bigger_digit = length - 1 
    while (pos_of_decreasing_no < pos_of_just_bigger_digit):
        no[pos_of_decreasing_no], no[pos_of_just_bigger_digit] = no[pos_of_just_bigger_digit], no[pos_of_decreasing_no]
        pos_of_decreasing_no += 1
        pos_of_just_bigger_digit -= 1
        
    return no
    
def find_just_higher_no_with_same_digits(no):
    no = list(str(no))
    length = len(no)
    
    first_decreasing_no_from_end, pos_of_decreasing_no = find_first_decreasing_no_from_end(no, length)
    new_no = arrange_digits_in_correct_order(no, length, first_decreasing_no_from_end, pos_of_decreasing_no)
    
    func = lambda nums: int(''.join(i for i in no))
    return func(new_no)

def main():
    no = 9272861
    print find_just_higher_no_with_same_digits(no)
    
if __name__ == "__main__":
    main()
