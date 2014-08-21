def perform_topological_sort_util(graph, start, visited, stack):
	visited[start] = 1
	
	for vertex in graph[start]:
		if vertex not in visited:
			perform_topological_sort_util(graph, vertex, visited, stack)
	stack.append(start)
			
def perform_topological_sort(graph):				
	no_of_nodes = len(graph)
	visited = {}
	stack = []
	
	for vertex in graph:
		if vertex not in visited:
			perform_topological_sort_util(graph, vertex, visited, stack)	
	
	while stack:
		print stack.pop()

def main():
	graph = {0 : [],
			 1 : [],
			 2 : [3],
			 3 : [1],
			 4 : [0,1],
			 5 : [0,2]}
	perform_topological_sort(graph)
		

if __name__ == "__main__":
	main()
