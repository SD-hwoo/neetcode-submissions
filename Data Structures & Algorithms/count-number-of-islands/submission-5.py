class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Keep track of identified 1's
        # Each time one is identified, loop to add each 1 attached in the island
        islands = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == '1':
                    islands += 1
                    grid[y][x] = '0'
                    layer = [(y, x)]
                    while layer:
                        cy, cx = layer.pop()    
                        for ny, nx in ((cy-1, cx), (cy+1, cx), (cy, cx-1), (cy, cx+1)):
                            if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]):
                                if grid[ny][nx] == '1':    
                                    grid[ny][nx] = '0'
                                    layer.append((ny, nx))
        return islands
                        
