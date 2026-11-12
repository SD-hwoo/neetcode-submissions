import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.track = nums
        heapq.heapify(self.track)


    def add(self, val: int) -> int:
        heapq.heappush(self.track, val)
        return heapq.nlargest(self.k, self.track)[-1]
