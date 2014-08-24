''' Design a stack which holds an integer value such that getMinimum() function should return the minimum element in the stack.
 Implement popMin() function which would pop minimum element from the original stack. O(1) implementation was required.''' 

from llist import dllist 

class SpecialStack:
    def __init__(self):
        self.main_stack = dllist()
        self.min_stack = []
    
    def push(self, data):
        node = self.main_stack.append(data)
        if len(self.min_stack) == 0:
            self.min_stack.append(node)
        elif data < self.min_stack[-1].value:
            self.min_stack.append(node)
            
    def pop(self):
        if self.main_stack:
            data = self.main_stack.pop()
            if data == self.min_stack[-1].value:
                self.min_stack.pop()
            return data
        else:
            return "stack is empty"
            
    def get_minimum(self):
        if self.main_stack:
            return self.min_stack[-1].value
        else:
            return "stack is empty"
        
    ''' Method is not complete
    it does not handle the case when the last min element is deleted'''
    def pop_minimum(self):
        if self.main_stack:
            data = self.main_stack.remove(self.min_stack[-1])
            self.min_stack.pop()
            return data
        else:
            return "stack is empty"
        
    
def main():
    stack = SpecialStack()
    stack.push(5)
    stack.push(8)
    stack.push(3)
    stack.push(2)
    stack.push(6)
    print stack.main_stack, "\t", stack.min_stack, "\n"
    
    print "Popped :", stack.pop(), "\t", stack.main_stack, "\t", stack.min_stack, "\n"
    print "Popped :", stack.pop(), "\t", stack.main_stack, "\t", stack.min_stack, "\n"
    
    print "Min element in stack is:", stack.get_minimum(), "\n"
    
    print "Popped min element in stack:", stack.pop_minimum(), "\t", stack.main_stack, "\t", stack.min_stack, "\n"
    print "Popped min element in stack:", stack.pop_minimum(), "\t", stack.main_stack, "\t", stack.min_stack, "\n"
    
    
if __name__ == "__main__":
    main()
