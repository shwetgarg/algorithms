from llist import dllist
import sys
from heapq import heappush, heappop

class LFUCache:
    heap = []
    cache_map = {}
    REMOVED = "<removed-task>"
    
    def __init__(self, cache_size):
        self.cache_size = cache_size
    
    def get_page_content(self, page_no):
        if self.cache_map.has_key(page_no):
        	print "Page found in cache (cache hit). So returning page from cache."
        	self.update_frequency_of_page_in_cache(page_no)            
        else:
            print "Page NOT found in cache (cache miss). So bringing page from disk."
            self.add_page_in_cache(page_no)
        
        return self.cache_map[page_no][2]       
            
    def add_page_in_cache(self, page_no):
        if (len(self.cache_map) == self.cache_size):
            self.delete_page_from_cache() 
        
        heap_node = [1, page_no, "content of page " + str(page_no)]
        heappush(self.heap, heap_node)
        self.cache_map[page_no] = heap_node
        
    def delete_page_from_cache(self):
    	while self.heap:
			count, page_no, page_content = heappop(self.heap)
			if page_content is not self.REMOVED:
				del self.cache_map[page_no]
				print "Cache was full, so deleted page no ", page_no, " from cache."
				return
    
    def update_frequency_of_page_in_cache(self, page_no): 
        heap_node = self.cache_map[page_no]
        heap_node[2] = self.REMOVED
        count = heap_node[0]
        
        heap_node = [count+1, page_no, "content of page " + str(page_no)]
        heappush(self.heap, heap_node)
        self.cache_map[page_no] = heap_node
        
def main():
    cache_size = int(raw_input("Enter cache size "))
    cache = LFUCache(cache_size)
    
    while 1:
        page_no = int(raw_input("Enter page no needed "))
        print cache.get_page_content(page_no)
        
if __name__ == "__main__":
    main()
