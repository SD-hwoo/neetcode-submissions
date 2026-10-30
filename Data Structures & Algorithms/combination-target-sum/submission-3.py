class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        nums.sort()
        def backtrack(current, start):
            if current == target:
                result.append(list(path))    
                return
            if current > target:
                return
            for i in range(start, len(nums)):
                if current + nums[i] > target:
                    break
                path.append(nums[i])
                backtrack(current + nums[i], i)
                path.pop()
        
        backtrack(0, 0)
        return result
