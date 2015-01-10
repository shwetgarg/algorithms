'''  2-D matrix is given where each cell represents height of cell. Water can flow from cell with higher height to lower one. A basin is when there is no cell with lower height in the neighbours (left,right,up,down,diagonal). You have to find maximum size basin block '''

from memoize import memoized

class MaxBasinSize:
    def __init__(self, matrix):
        self.matrix = matrix
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.visited = [[0]*self.col for i in range(self.row)]
    
    def get_basin_size(self, i, j):
        if self.visited[i][j] == 1:
            return 0
        
        self.visited[i][j] = 1
        
        if (((i-1 >= 0) and (self.matrix[i-1][j] < self.matrix[i][j]) or
            ((i+1 < self.row) and (self.matrix[i+1][j] < self.matrix[i][j])) or
            ((j-1 >= 0) and (self.matrix[i][j-1] < self.matrix[i][j])) or
            ((j+1 < self.col) and (self.matrix[i][j+1] < self.matrix[i][j])) or 
            ((i-1 >= 0) and (j-1 >= 0) and (self.matrix[i-1][j-1] < self.matrix[i][j])) or 
            ((i-1 >= 0) and (j+1 < self.col) and (self.matrix[i-1][j+1] < self.matrix[i][j])) or
            ((i+1 < self.row) and (j-1 >= 0) and (self.matrix[i+1][j-1] < self.matrix[i][j])) or 
            ((i+1 < self.row) and (j+1 < self.col) and (self.matrix[i+1][j+1] < self.matrix[i][j])))):
            return -1
    
        basin_size = 1
        if i-1 >= 0:
            val = self.get_basin_size(i-1, j)
            if val > 0:
                basin_size += val
        if i+1 < self.row:
            val = self.get_basin_size(i+1, j)
            if val > 0:
                basin_size += val
        if j-1 >= 0:
            val = self.get_basin_size(i, j-1)
            if val > 0:
                basin_size += val
        if j+1 < self.col:
            val = self.get_basin_size(i, j+1)
            if val > 0:
                basin_size += val	
    
        return basin_size

    def get_max_basin_size(self):
        basin_sizes = []
        for i in range(self.row):
            for j in range(self.col):
                if self.visited[i][j] != 1:
                    basin_sizes.append((self.get_basin_size(i, j),i,j))
        print basin_sizes
        print
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
    basin = MaxBasinSize(matrix)
    print basin.get_max_basin_size()
    
if __name__ == "__main__":	
    main()
