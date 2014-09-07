def print_pairs(no_list, sum):
    start = 0
    end = len(no_list) - 1
    while(start <= end):
        if no_list[start] + no_list[end] == sum:
            print no_list[start], no_list[end]
            start += 1
            end -= 1
        elif no_list[start] + no_list[end] < sum:
            start += 1
        else:
            end -= 1
    
def main():
    no_list = [1,2,3,4,5,6,7,8]
    sum = 5
    
    print_pairs(no_list, sum)

if __name__ == "__main__":
    main()
