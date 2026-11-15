import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        track = dict()

        for point in points:
            dist = math.sqrt(pow(point[0], 2) + pow(point[1], 2))
            if dist not in track:
                track[dist] = [point]
            else:
                track[dist].append(point)
        
        order = list(track)
        heapq.heapify(order)

        result = []
        while len(result) < k:
            if len(track[order[0]]) > 0:
                result.append(track[order[0]].pop())
            else:
                heapq.heappop(order)
        return result