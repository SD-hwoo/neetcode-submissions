class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_fruits = []
        total_fruits = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] > 0:
                    total_fruits += 1
                if grid[y][x] == 2:
                    rotten_fruits.append((y,x))
        len_x = len(grid[0])
        len_y = len(grid)
        rotten_count = len(rotten_fruits)
        minutes = 0
        if rotten_count == total_fruits:
                return minutes

        while rotten_fruits:
            minutes += 1
            new_rotten_fruits = []
    
            for fruit in rotten_fruits:
                #check up
                if fruit[0] + 1 < len_y:
                    if grid[fruit[0] + 1][fruit[1]] == 1:
                        new_rotten_fruits.append((fruit[0] + 1, fruit[1]))
                        grid[fruit[0] + 1][fruit[1]] = 2
                
                #check down
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
            
            rotten_count += len(new_rotten_fruits)
            rotten_fruits = new_rotten_fruits

            if rotten_count == total_fruits:
                return minutes
        return -1
