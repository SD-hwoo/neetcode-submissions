class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        entries = self.store.get(key, [])
        best = ""
        lo, hi = 0, len(entries) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if entries[mid][0] <= timestamp:
                best = entries[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
        return best

        
