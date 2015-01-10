
from collections import deque

class SnakeLadder():
    def __init__(self, M, N, s_l):
        self.M = M
        self.N = N
        self.s_l = s_l
        
    def prepare_graph(self):
        size = self.M*self.N
        graph = {}
        
        for i in range(1, size+1):
            graph[i] = [i + 1]
            for j in range(2, 7):
                if i+j <= size:
                    graph[i].append(i + j)
                
        
        for key in self.s_l:
            if key not in graph:
                print "val not in board"
            else:
                graph[key].append(self.s_l[key])			
        print graph	
        return graph
    
    def BFS(self, graph, start):
        size = self.M*self.N
        count = 0
        
        no_of_nodes = len(graph)+2
        visited = [0] * no_of_nodes
    
        queue = deque([start])
        visited[start] = 1
        queue.append("end") 
        
        while queue:
            vertex1 = queue.popleft()
            print queue, vertex1, count
            
            if (vertex1 == "end"):		
                count += 1
                queue.append("end") 
                continue
            
            if (vertex1 == size):
                return count
            
            for vertex2 in graph[vertex1]:
                if (visited[vertex2] == 0):
                    queue.append(vertex2) 
                    visited[vertex2] = 1
                    
def main():
    '''M = 3
    N = 4
    s_l = {2:7, 11:3}	
    snake_ladder = SnakeLadder(M, N, s_l)
    graph = snake_ladder.prepare_graph()
    print snake_ladder.BFS(graph, 1)
    
    M = 10
    N = 10
    s_l = {4:14, 9:31, 17:7, 20:38, 28:84, 40:59, 93:73, 95:75, 99:78}	
    snake_ladder = SnakeLadder(M, N, s_l)
    graph = snake_ladder.prepare_graph()
    print snake_ladder.BFS(graph, 1)'''
    
    M = 5
    N = 6
    s_l = {3:22, 5:8, 11:26, 17:4, 19:7, 20:29, 21:9, 27:1}	
    snake_ladder = SnakeLadder(M, N, s_l)
    graph = snake_ladder.prepare_graph()
    print snake_ladder.BFS(graph, 1)
    
    
    
    
if __name__ == "__main__":
    main()
