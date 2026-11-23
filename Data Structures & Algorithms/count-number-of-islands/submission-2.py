class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Keep track of identified 1's
        # Each time one is identified, loop to add each 1 attached in the island
        seen = set()
        islands = 0

        def explore(y, x):
            if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
                if grid[y][x] == '1':    
                    grid[y][x] = '0'

                    explore(y - 1, x)
                    explore(y + 1, x)
                    explore(y, x + 1)
                    explore(y, x - 1)


        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == '1':
                    islands += 1
                    explore(y, x)
        return islands
                        
