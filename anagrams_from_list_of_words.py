'''Given two string str and pat. Find minimum window in str which contains all characters from string pat.'''

from collections import defaultdict
import sys

def get_anagrams_dict(words):
	anagrams_dict = defaultdict(list)
	for word in words:
		word = word.rstrip()
		key = ''.join(sorted(word))
		anagrams_dict[key].append(word)
	return anagrams_dict
		
def get_anagrams_list(anagrams_dict):
	anagrams_list = []	
	for key in anagrams_dict:
		anagrams_list.append(anagrams_dict[key])
	return anagrams_list
		
def get_anagrams(words):
	anagrams_dict = get_anagrams_dict(words)
	return get_anagrams_list(anagrams_dict)

def main():
	words = ['cat', 'tac', 'mat', 'rat', 'tam', 'act']
	anagrams_list = get_anagrams(words)
	print anagrams_list

if __name__ == "__main__":
    main()
