class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
       # Backtracking but cicular this time
        result = []
        path = []
        used = [False] * len(nums)

        def backtracking(start):
            if len(path) == len(nums):
                result.append(list(path))
                return

            for i in range(start, start + len(nums)):
                if used[(i % len(nums))]:
                    continue
                path.append(nums[(i % len(nums))])
                used[(i % len(nums))] = True
                backtracking((i+1))
                path.pop()
                used[(i % len(nums))] = False
        
        backtracking(0)
        return result