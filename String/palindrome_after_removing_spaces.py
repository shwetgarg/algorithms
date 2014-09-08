def if_palindrome(string):
    start = 0
    end = len(string) - 1
    
    while (start <= end):
        if string[start] == " ":
            start += 1
        elif string[end] == " ":
            end -= 1
        elif string[start] != string[end]:
            return False
        else:
            start += 1
            end -= 1
    
    return True

def main():
    string = "race car"
    print if_palindrome(string)	

    string = "races car"
    print if_palindrome(string)	

if __name__ == "__main__":
    main()
