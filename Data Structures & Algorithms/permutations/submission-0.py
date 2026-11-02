class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
       # Backtracking but cicular this time
        result = []
        path = []

        def backtracking(start):
            if len(path) == len(nums):
                result.append(list(path))
                return

            for i in range(start, start + len(nums)):
                if nums[(i % len(nums))] in path:
                    continue
                path.append(nums[(i % len(nums))])
                backtracking((i+1))
                path.pop()
        
        backtracking(0)
        return result