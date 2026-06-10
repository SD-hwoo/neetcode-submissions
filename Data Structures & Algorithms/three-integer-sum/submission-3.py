class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            current = [nums[i]]
            seen = set()
            goal = -(nums[i])
            for j in range(i + 1, len(nums)):
                if goal - nums[j] in seen:
                    current.append(nums[j]) 
                    current.append((goal - nums[j]))
                    result.append(current)
                    current = [nums[i]]
                else:
                    seen.add(nums[j])
        answer = []
        seen = set()
        for sublist in result:
            current = frozenset(sublist)
            if current not in seen:
                seen.add(current)
                answer.append(sublist)
        return answer
