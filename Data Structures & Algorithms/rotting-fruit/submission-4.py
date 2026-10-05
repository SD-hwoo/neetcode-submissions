class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_fruits = []
        fresh = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 2:
                    rotten_fruits.append((y,x))
                if grid[y][x] == 1:
                    fresh += 1
        len_x = len(grid[0])
        len_y = len(grid)
        minutes = 0
        if fresh == 0:
            return minutes

        while rotten_fruits:
            minutes += 1
            new_rotten_fruits = []
    
            for fruit in rotten_fruits:
                #check down
                if fruit[0] + 1 < len_y:
                    if grid[fruit[0] + 1][fruit[1]] == 1:
                        new_rotten_fruits.append((fruit[0] + 1, fruit[1]))
                        grid[fruit[0] + 1][fruit[1]] = 2
                
                #check up
                if fruit[0] - 1 >= 0:
                    if grid[fruit[0] - 1][fruit[1]] == 1:
                        new_rotten_fruits.append((fruit[0] - 1, fruit[1]))
                        grid[fruit[0] - 1][fruit[1]] = 2
                
                #check left
                if fruit[1] - 1 >= 0:
                    if grid[fruit[0]][fruit[1] - 1] == 1:
                        new_rotten_fruits.append((fruit[0], fruit[1] - 1))
                        grid[fruit[0]][fruit[1] - 1] = 2

                #check right
                if fruit[1] + 1 < len_x:
                    if grid[fruit[0]][fruit[1] + 1] == 1:
                        new_rotten_fruits.append((fruit[0], fruit[1] + 1))
                        grid[fruit[0]][fruit[1] + 1] = 2
            
            fresh -= len(new_rotten_fruits)
            rotten_fruits = new_rotten_fruits

            if fresh == 0:
                return minutes
        return -1
