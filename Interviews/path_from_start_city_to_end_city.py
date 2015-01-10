''' Given connecting edges between different cities in random order.
Arrange them in order such that they form path from start city to end city'''

def find_boundary_nodes(input_list):
    dict = {}
    for item in input_list:
        for val in item:
            if val in dict:
                del dict[val]
            else:
                dict[val] = 1

    return dict.keys()[0], dict.keys()[1]

def prepare_map(input_list):
    dict = {}
    for item in input_list:
        dict[item[0]] = item[1]

    return dict

def find_end_node(dict):
    node = dict.keys()[0]
    while dict[node] in dict:
        node = dict[node] 
            
    return dict[node]

def print_path(dict, start_node, end_node):
    print start_node, "->",

    node = start_node 
    while (dict[node] != end_node):
        print dict[node], "->",
        node = dict[node]

    print dict[node]

def main():
    input_list = [('B', 'D'), ('A', 'C'), ('C', 'E'), ('E', 'B')]
    boundary_node_1, boundary_node_2 = find_boundary_nodes(input_list)
    input_dict = prepare_map(input_list)
    end_node = find_end_node(input_dict)
    if boundary_node_1 == end_node:
        start_node = boundary_node_2
    else:
        start_node = boundary_node_1
    print_path(input_dict, start_node, end_node)
    
if __name__ == "__main__":
    main()
