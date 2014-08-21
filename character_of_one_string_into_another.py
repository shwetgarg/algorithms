import sys

def fill_char_in_map(string):
	char_map = {}	
	for char in string:	
		char_map[char] = (char_map[char] + 1) if char in char_map else 1
	return char_map

def find_window_size(string, chars_to_find, length):
	has_found = {}
	count = 0
	start = 0
	end = 0
	min_window_len = sys.maxint
	min_start = 0
	min_end = 0
	
	for char in string:
		if char not in chars_to_find:
			end += 1
			continue
		
		has_found[char] = (has_found[char] + 1) if char in has_found else 1
		count = (count + 1) if ((has_found[char] - 1) < chars_to_find[char]) else count	
		end += 1
		
		if (count == length):	
			while (1):
				if (string[start] in chars_to_find) and (has_found[string[start]] == chars_to_find[string[start]]):
					break
				elif (string[start] in chars_to_find) and (has_found[string[start]] > chars_to_find[string[start]]):
					has_found[string[start]] -= 1
					start += 1
				elif (string[start] not in chars_to_find):
					start += 1
			
			window_len = end - start
			if (window_len < min_window_len):
				min_window_len = window_len
				min_start = start
				min_end = end
				
	return min_window_len
	
def main():
	main_string = "computer engineering"
	sring_to_be_searched = "not"
	
	len_of_string_to_be_searched = len(sring_to_be_searched)
	chars_to_find = fill_char_in_map(sring_to_be_searched)
	print find_window_size(main_string, chars_to_find, len_of_string_to_be_searched)

if __name__ == "__main__":
	main()
	
