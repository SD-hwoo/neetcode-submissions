class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])

        for y in range(rows):
            for x in range(cols):
                area = 0
                if grid[y][x] == 1:
                    area += 1
                    search = [(y, x)]
                    grid[y][x] = 0
                    while search:
                        cy, cx = search.pop()
                        for ny, nx in ((cy + 1, cx), (cy - 1, cx), (cy, cx - 1), (cy, cx + 1)):
                            if 0 <= ny < rows and 0 <= nx < cols:
                                if grid[ny][nx] == 1:
                                    grid[ny][nx] = 0
                                    search.append((ny, nx))
                                    area += 1
                    if area > max_area:
                        max_area = area
        
        return max_area