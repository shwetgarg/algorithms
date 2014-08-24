''' Correction and modification of code given at http://reterwebber.wordpress.com/2014/01/22/data-structure-in-python-trie/'''


def make_trie(*args):
    """
    Make a trie by given words.
    """
    trie = {}
 
    for word in args:
        if type(word) != str:
            raise TypeError("Trie only works on str!")
        temp_trie = trie
        for letter in word:
            temp_trie = temp_trie.setdefault(letter, {})
        temp_trie = temp_trie.setdefault('_end_', '_end_')
        
    return trie
 
def in_trie(trie, word):
    """
    Detect if word in trie.
    """
    if type(word) != str:
        raise TypeError("Trie only works on str!")
 
    temp_trie = trie
    for letter in word:
        if letter not in temp_trie:
            return False
        temp_trie = temp_trie[letter]
        
    if  "_end_" in temp_trie:
        return True
    else:
        return False
 
def remove_from_trie(trie, word, depth = 0):
    """
    Remove certain word from trie.
    """
    
    if word and word[depth] not in trie:
        return False
 
    if len(word) == depth + 1:
        if '_end_' in trie[word[depth]]:		
            del trie[word[depth]]['_end_']   # baz and barz both are safe
            
        if len(trie[word[depth]]) > 0 and len(trie) > 1:   # baz and barz both are present
            return False
        elif len(trie) > 1 :  # only baz is present
            del trie[word[depth]]
            return False
        elif len(trie[word[depth]]) > 0:   # only barz is present
            return False
        else:
            return True
    else:
        temp_trie = trie 
        # Recursively climb up to delete.
        if remove_from_trie(temp_trie[word[depth]], word, depth + 1):
            if temp_trie:
                del temp_trie[word[depth]]
            return not temp_trie
        else:
            return False
 
 
if __name__ == '__main__':
    trie = make_trie('hello', 'baz', 'bar', 'barz', 'barzing')
    print trie, "\n"
 
    print in_trie(trie, 'hello')
    print in_trie(trie, 'bar')
    print in_trie(trie, 'ba')
    print in_trie(trie, 'barzon')
    print in_trie(trie, 'zzz')
    print
 
    remove_from_trie(trie, 'xyz', 0)        # Case1: Key not present in trie
    print trie, "\n"
    remove_from_trie(trie, 'hello', 0)		# Case2: Key present as unique key (no part of key contains another key (prefix), nor the key itself is prefix of another key in trie). Delete all the nodes.
    print trie, "\n"
    remove_from_trie(trie, 'barz', 0)		# Case3: Key is prefix key of another long key in trie. Unmark the leaf node.
    print trie, "\n"
    remove_from_trie(trie, 'barzing', 0)	# Case4: Key present in trie, having atleast one other key as prefix key. Delete nodes from end of key until first leaf node of longest prefix key.
    print trie, "\n"
    #print in_trie(trie, 1)
