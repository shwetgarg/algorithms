''' Given a dictionary of unknown language and characters. Find out order between characters.'''

import sys
sys.path.append('Graphs')
from topological_sort import perform_topological_sort

def prepare_graph(dictionary):
    graph = {}
    for string in dictionary:
        for i in range(len(string)-1):
            if string[i] in graph:
                graph[string[i]].append(string[i+1])
            else:
                graph[string[i]] = [string[i+1]]	
        if string[-1] not in graph:
            graph[string[-1]] = [] 		
    return graph


def main():
    dictionary = ["ab", "bcd", "ce", "de"]
    graph = prepare_graph(dictionary)
    perform_topological_sort(graph)
    
if __name__ == "__main__":
    main()
