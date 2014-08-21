from llist import dllist
import sys

class LRUCache:
    linked_list = dllist()
    cache_map = {}
    
    def __init__(self, cache_size):
        self.cache_size = cache_size
    
    def get_page(self, page_no):
        if self.cache_map.has_key(page_no):
        	print "Page found in cache (cache hit). So returning page from cache."
        	self.put_page_in_front_in_cache(page_no)  
        else:
        	print "Page NOT found in cache (cache miss). So bringing page from disk."
        	self.add_page_in_cache(page_no)
        
        return self.cache_map[page_no].value       
            
    def add_page_in_cache(self, page_no):
        if (len(self.cache_map) == self.cache_size):
            self.delete_page_from_cache() 
        
        node = self.linked_list.insert(page_no)
        self.cache_map[page_no] = node
        
    def delete_page_from_cache(self):
        page_no = self.linked_list.popleft()
        del self.cache_map[page_no]
        print "Cache was full, so deleted page no ", page_no, " from cache."
    
    def put_page_in_front_in_cache(self, page_no): 
        node = self.cache_map[page_no]
        self.linked_list.remove(node)
        node = self.linked_list.insert(page_no)
        self.cache_map[page_no] = node      
        
def main():
    cache_size = int(raw_input("Enter cache size "))
    cache = LRUCache(cache_size)
    
    while 1:
        page_no = int(raw_input("Enter page no needed "))
        print cache.get_page(page_no)    

if __name__ == "__main__":
    main()
