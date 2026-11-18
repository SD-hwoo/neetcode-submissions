import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = dict()
        for task in tasks:
            if task not in count:
                count[task] = 1
            else:
                count[task] += 1
        tracker = []
        for task in count:
            tracker.append(count[task])
        heapq.heapify_max(tracker)
        tasks_complete = 0
        cycles = 0
        recent = [None] * n
        while tasks_complete != len(tasks):
            current = None
            if tracker:
                current = heapq.heappop_max(tracker)
                current -= 1
                tasks_complete += 1
        
            recent.append(current)
            out = recent.pop(0)
            if out:
                if out > 0:
                    heapq.heappush_max(tracker, out)
            cycles += 1

        return cycles
        