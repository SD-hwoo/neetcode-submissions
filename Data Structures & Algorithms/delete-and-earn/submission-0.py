class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # We can keep removing until the list is empty
        tracker = {}

        for num in nums:
            tracker[num] = tracker.get(num, 0) + 1
        
        value = {}
        for num in range(max(tracker) + 1):
            value[num] = num * (tracker.get(num, 0))
        print(value)

        score = 0

        prev1, prev2 = 0, 0
        for v in value:
            best = max(prev1, prev2 + value[v])
            prev2, prev1 = prev1, best
        return prev1
