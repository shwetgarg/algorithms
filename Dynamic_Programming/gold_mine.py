''' Given a gold mine of n*m dimensions. 
Each field in this mine contains an integer which is amount of gold in tons. 
Initially miner is in first column but could be at any row i. 
He can move only (right ->, right up /, right down \). 
Find out maximum amount of gold he can collect and path followed by him.'''

import collections
import functools

class gold_mine_algo:
    def __init__(self, matrix, initial_row_pos):
        self.matrix = matrix
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.initial_row_pos = initial_row_pos
        
    def get_max_gold(self):
        calc_matrix = [[0]*self.col for i in range(self.row)]
        calc_matrix[self.initial_row_pos][0] = self.matrix[self.initial_row_pos][0]
        
        for c in range(1, self.col):
            start = max(0, self.initial_row_pos - c)
            end = min(self.initial_row_pos + c, self.row - 1)
            for r in range(start, end + 1):
                v1 = calc_matrix[r-1][c-1] if r > 0 else 0
                v2 = calc_matrix[r][c-1]
                v3 = calc_matrix[r+1][c-1] if r < self.row - 1 else 0
                calc_matrix[r][c] = self.matrix[r][c] + max(v1, v2, v3) 
                            
        return reduce(max, [calc_matrix[i][self.col-1] for i in range(self.row)])
                        
def main():
    matrix = [[2,4,1], [9,2,3]]
    initial_row_pos = 1
    gold_mine = gold_mine_algo(matrix, initial_row_pos)
    print "Max gold: ", gold_mine.get_max_gold()
       
if __name__ == "__main__":
    main()
   
