from collections import deque
import time 

def perform_BFS(graph, start):
	no_of_nodes = len(graph)
	visited = [0] * no_of_nodes
	
	queue = deque([start])
	visited[start] = 1
		
	while queue:
		vertex1 = queue.popleft()
		print vertex1
		for vertex2 in graph[vertex1]:
			if (visited[vertex2] == 0):
				queue.append(vertex2) 
				visited[vertex2] = 1		
		
def main():
	graph = {0 : [1,2],
			 1 : [2],
			 2 : [0,3],
			 3 : [3]}
	perform_BFS(graph, 2)
			 
if __name__ == "__main__":
	main()
