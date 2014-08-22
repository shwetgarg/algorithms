'''Given two string str and pat. Find minimum window in str which contains all characters/words from string pat.'''

import sys

def fill_content_in_map(string):
    content_map = {}	
    for content in string:	
        content_map[content] = (content_map[content] + 1) if content in content_map else 1
    return content_map

def find_window_size(string, content_to_find, length):
    has_found = {}
    count = 0
    start = 0
    end = 0
    min_window_len = sys.maxint
    min_start = 0
    min_end = 0
    
    for content in string:
        if content not in content_to_find:
            end += 1
            continue
        
        has_found[content] = (has_found[content] + 1) if content in has_found else 1
        count = (count + 1) if ((has_found[content] - 1) < content_to_find[content]) else count	
        end += 1
        
        if (count == length):	
            while (1):
                if (string[start] in content_to_find) and (has_found[string[start]] == content_to_find[string[start]]):
                    break
                elif (string[start] in content_to_find) and (has_found[string[start]] > content_to_find[string[start]]):
                    has_found[string[start]] -= 1
                    start += 1
                elif (string[start] not in content_to_find):
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
    print "Case1: Find minimum window in \"" + main_string + "\" which contains all CHARACTERS from string \"" + sring_to_be_searched + "\""
    len_of_string_to_be_searched = len(sring_to_be_searched)
    chars_to_find = fill_content_in_map(sring_to_be_searched)
    print find_window_size(main_string, chars_to_find, len_of_string_to_be_searched)
    
    main_string = "computer engineering is best"
    sring_to_be_searched = "best engineering"
    print "Case2: Find minimum window in \"" + main_string + "\" which contains all WORDS from string \"" + sring_to_be_searched + "\""	
    main_string = main_string.split()
    sring_to_be_searched = sring_to_be_searched.split()	
    len_of_string_to_be_searched = len(sring_to_be_searched)
    words_to_find = fill_content_in_map(sring_to_be_searched)	
    print find_window_size(main_string, words_to_find, len_of_string_to_be_searched)

if __name__ == "__main__":
    main()
    
