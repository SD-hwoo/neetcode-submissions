class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i in range(0, len(nums)):
            if nums[i] not in seen:
                seen[target - nums[i]] = i
            else:
                return [seen[nums[i]], i]
        