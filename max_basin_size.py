'''  2-D matrix is given where each cell represents height of cell. Water can flow from cell with higher height to lower one. A basin is when there is no cell with lower height in the neighbours (left,right,up,down,diagonal). You have to find maximum size basin block '''

def get_basin_size(matrix, visited, i, j, row, col):
    if visited[i][j] == 1:
        return 0
        
    visited[i][j] = 1
        
    if (((i-1 >= 0) and (matrix[i-1][j] < matrix[i][j]) or
        ((i+1 < row) and (matrix[i+1][j] < matrix[i][j])) or
        ((j-1 >= 0) and (matrix[i][j-1] < matrix[i][j])) or
        ((j+1 < col) and (matrix[i][j+1] < matrix[i][j])) or 
        ((i-1 >= 0) and (j-1 >= 0) and (matrix[i-1][j-1] < matrix[i][j])) or 
        ((i-1 >= 0) and (j+1 < col) and (matrix[i-1][j+1] < matrix[i][j])) or
        ((i+1 < row) and (j-1 >= 0) and (matrix[i+1][j-1] < matrix[i][j])) or 
        ((i+1 < row) and (j+1 < col) and (matrix[i+1][j+1] < matrix[i][j])))):
        return -1
    
    basin_size = 1
    if i-1 >= 0:
        val = get_basin_size(matrix, visited, i-1, j, row, col)
        if val > 0:
            basin_size += val
    if i+1 < row:
        val = get_basin_size(matrix, visited, i+1, j, row, col)
        if val > 0:
            basin_size += val
    if j-1 >= 0:
        val = get_basin_size(matrix, visited, i, j-1, row, col)
        if val > 0:
            basin_size += val
    if j+1 < col:
        val = get_basin_size(matrix, visited, i, j+1, row, col)
        if val > 0:
            basin_size += val	
    
    return basin_size

def get_max_basin_size(matrix):
    row = len(matrix)
    col = len(matrix[0])
    basin_sizes = []
    visited = [[0]*col for i in range(row)]
    for i in range(row):
        for j in range(col):
            if visited[i][j] != 1:
                basin_sizes.append(get_basin_size(matrix, visited, i, j, row, col))
    print basin_sizes
    return max(basin_sizes)
    
def main():
    matrix = [[9, 9, 9, 8, 7, 7],
              [8, 8, 7, 7, 7, 8],
              [8, 8, 8, 7, 7, 7],
              [8, 8, 8, 9, 9, 9],
              [8, 8, 8, 7, 7, 7],
              [4, 4, 5, 5, 5, 5],
              [5, 5, 5, 6, 6, 7],
              [5, 5, 5, 8, 8, 6]]
    print get_max_basin_size(matrix)
    
if __name__ == "__main__":	
    main()
