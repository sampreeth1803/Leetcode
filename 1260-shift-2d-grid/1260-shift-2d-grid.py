class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        
        # Optimize shifts if k is larger than the total number of elements
        k %= total_elements
        
        # Initialize an empty result grid with the same dimensions
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                # Find the target 1D index after shifting
                new_1d_index = (i * n + j + k) % total_elements
                
                # Convert back to 2D row and column indices
                new_row = new_1d_index // n
                new_col = new_1d_index % n
                
                result[new_row][new_col] = grid[i][j]
                
        return result
        