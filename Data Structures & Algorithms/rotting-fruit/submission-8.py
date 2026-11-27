class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        queue = []

        rows = len(grid)
        cols = len(grid[0])

        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 2:
                    queue.append((y,x))
        
        while queue:
            new_queue = []
            while queue:
                y, x = queue.pop()
                for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                    if 0 <= ny < rows and 0 <= nx < cols:
                        if grid[ny][nx] == 1:
                            new_queue.append((ny, nx))
                            grid[ny][nx] = 2
            if not new_queue:
                break
            queue = new_queue
            minutes += 1
        
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 1:
                    return -1
        return minutes
        
