''' A group of farmers has some elevation data, and we are going to help them understand how rainfall flows over their farmland.
We will represent the land as a two-dimensional array of altitudes and use the following model, based on the idea that water flows downhill.
If a cell's four neighboring cells all have higher altitudes, we call this cell a sink; water collects in sinks.
Otherwise, water will flow to the neighboring cell with the lowest altitude. 
If a cell is not a sink, you may assume it has a unique lowest neighbor and that this neighbor will be lower than the cell.
Cells that drain into the same sink - directly or indirectly - are said to be part of the same basin.
Your challenge is to partition the map into basins. In particular, given a map of elevations, your code should partition the map into basins and output the sizes of the basins, in descending order.'''

import sys

def get_flow_directions(matrix, row, col):
    flow_direction_matrix = []
    sink = []
    for i in range(row):
        row_matrix = []
        for j in range(col):
            current = matrix[i][j]
            up = matrix[i-1][j] if (i-1 >= 0) else sys.maxint
            down = matrix[i+1][j] if (i+1 < row) else sys.maxint
            left = matrix[i][j-1] if (j-1 >= 0) else sys.maxint
            right = matrix[i][j+1] if (j+1 < col) else sys.maxint
            
            min_val = min(current, up, down, right, left)
            
            if min_val == current:
                row_matrix.append("C")
                sink.append((i,j))
            elif min_val == up:
                row_matrix.append("U")
            elif min_val == down:
                row_matrix.append("D")
            elif min_val == left:
                row_matrix.append("L")
            elif min_val == right:
                row_matrix.append("R")				
        flow_direction_matrix.append(row_matrix)
        
    return flow_direction_matrix, sink	
    
def get_basin_size(matrix, i, j, row, col):
    if matrix[i][j] == "V":
        return 0
    up = down = left = right = 0	
    if (i-1 >= 0) and (matrix[i-1][j] == "D"): 
        up = get_basin_size(matrix, i-1, j, row, col)
    if (i+1 < row) and (matrix[i+1][j] == "U"): 
        down = get_basin_size(matrix, i+1, j, row, col)
    if (j-1 >= 0) and (matrix[i][j-1] == "R"): 
        left = get_basin_size(matrix, i, j-1, row, col)
    if (j+1 < col) and (matrix[i][j+1] == "L"): 
        right = get_basin_size(matrix, i, j+1, row, col)
        
    return (1 + up + down + left +right)		

def get_basin_sizes(matrix):
    row = len(matrix)
    col = len(matrix[0])
    
    flow_direction_matrix, sink = get_flow_directions(matrix, row, col)
    
    basin_sizes = []
    for node in sink:
        size = get_basin_size(flow_direction_matrix, node[0], node[1], row, col)
        basin_sizes.append(size)
        
    return sorted(basin_sizes)		
    
def main():
    matrix = [[1, 0, 2, 5, 8],
              [2, 3, 4, 7, 9],
              [3, 5, 7, 8, 9],
              [1, 2, 5, 4, 2],
              [3, 3, 5, 2, 1]]
    print get_basin_sizes(matrix)
    
if __name__ == "__main__":	
    main()
