import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for n1 in nums:
            new_batch = []
            for s in result:
                new_s = copy.copy(s)
                new_s.append(n1)
                new_batch.append(new_s)
            result += new_batch

        return(result)
            
