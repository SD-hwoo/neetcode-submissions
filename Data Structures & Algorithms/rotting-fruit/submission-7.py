class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS
        fresh = 0
        rotten = []
        rounds = 0
        # first scan
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    fresh += 1
                elif grid[y][x] == 2:
                    rotten.append((y,x))
        if fresh == 0:
            return 0
        while rotten:
            new_rotten = []
            rounds += 1
            for rot_fruit in rotten:
                y = rot_fruit[0]
                x = rot_fruit[1]

                # check up
                if y - 1 >= 0:
                    if grid[y - 1][x] == 1:
                        new_rotten.append((y - 1, x))
                        grid[y - 1][x] = 2
                        fresh -= 1

                # check down
                if y + 1 < len(grid):
                    if grid[y + 1][x] == 1:
                        new_rotten.append((y + 1, x))
                        grid[y + 1][x] = 2
                        fresh -= 1

                # check left
                if x - 1 >= 0:
                    if grid[y][x - 1] == 1:
                        new_rotten.append((y, x - 1))
                        grid[y][x - 1] = 2
                        fresh -= 1

                #check right 
                if x + 1 < len(grid[y]):
                    if grid[y][x + 1] == 1:
                        new_rotten.append((y, x + 1))
                        grid[y][x + 1] = 2
                        fresh -= 1

            if fresh == 0:
                return rounds
                


            rotten = new_rotten

        return -1


