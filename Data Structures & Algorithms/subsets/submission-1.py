class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []


        def backtracking(i):
            result.append(list(path))

            for j in range(i, len(nums)):
                path.append(nums[j])
                backtracking(j+1)
                path.pop()
        backtracking(0)
        return result
