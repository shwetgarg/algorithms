def perform_DFS_util(graph, start, visited):
	visited[start] = 1
	print start
	
	for vertex in graph[start]:
		if (visited[vertex] == 0):
			perform_DFS_util(graph, vertex, visited)
			
def perform_DFS(graph):				
	no_of_nodes = len(graph)
	visited = [0]*no_of_nodes
	
	for vertex in graph:
		if visited[vertex] == 0:
			perform_DFS_util(graph, vertex, visited)	

def main():
	graph = {0 : [1,2],
			 1 : [2],
			 2 : [0,3],
			 3 : [3],
			 4 : []}
	perform_DFS(graph)
		

if __name__ == "__main__":
	main()
