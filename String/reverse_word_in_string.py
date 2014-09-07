def reverse_string(string):
    string = string.split()
    for word in string:
        print word[::-1], 

def main():
    string = "my name is shweta garg"
    reverse_string(string)	

if __name__ == "__main__":
    main()
    
