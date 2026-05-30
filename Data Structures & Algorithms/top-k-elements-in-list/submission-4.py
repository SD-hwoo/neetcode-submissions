class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

        buckets = [[] for _ in range(len(nums))]
        for key in counts:
            buckets[counts[key]-1].append(key)
        result = []
        for ls in buckets[::-1]:
            for key in ls:
                result.append(key)
                if len(result) == k:
                    break
            if len(result) == k:
                    break
        return result
        # grouping = dict()
        # for key in counts:
        #     if counts[key] not in grouping:
        #         grouping[counts[key]] = [key]
        #     else:
        #         grouping[counts[key]].append(key)

        # result = []
        # order = sorted(list(grouping.keys()), reverse=True)
        # for i in order:

        #     for key in grouping[i]:
   
        #         result.append(key)
        #         if len(result) == k:
        #             break
            
        #     if len(result) == k:
        #             break
        # return result

        