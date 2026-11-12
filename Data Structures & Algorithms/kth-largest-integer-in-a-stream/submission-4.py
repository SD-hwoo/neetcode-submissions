import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.track = list(nums)
        heapq.heapify(self.track)
        while (len(self.track) > k):
            heapq.heappop(self.track)


    def add(self, val: int) -> int:
        if len(self.track) < self.k:
            heapq.heappush(self.track, val)
        else:
            heapq.heappushpop(self.track, val)
            # print(self.track)
        return self.track[0]
