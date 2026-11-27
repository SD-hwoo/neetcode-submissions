class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        results = []
        pacific = set()
        atlantic = set()
        
        pac_q = []
        atl_q = []
        rows = len(heights)
        cols = len(heights[0])

        def search(stack, visited):
            while stack:
                r, c = stack.pop()
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if (nr, nc) not in visited:
                            if heights[nr][nc] >= heights[r][c]:
                                visited.add((nr, nc))
                                stack.append((nr, nc))
                                search(stack, visited)

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pac_q.append((r,c))
                    pacific.add((r,c))
                if r == rows - 1 or c == cols - 1:
                    atl_q.append((r,c))
                    atlantic.add((r,c))
        search(pac_q, pacific)
        search(atl_q, atlantic)
        for r, c in (pacific & atlantic):
            results.append([r,c])
        return results

            


        




