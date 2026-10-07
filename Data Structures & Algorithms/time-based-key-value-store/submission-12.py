class TimeMap:

    def __init__(self):
        self.keys = {}
        self.time = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key] = self.keys.get(key, []) + [timestamp]
        self.time[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        if timestamp not in self.keys[key]:
            
            # binary search
            timestamps = self.keys[key]
            l = 0
            r = len(timestamps) - 1
            while l < r:
                m = (l + r) // 2 + 1
                if timestamps[m] <= timestamp:
                    l = m
                else:
                    r = m - 1
            
            if timestamps[l] <= timestamp:
                return self.time[(key, timestamps[l])]
            return ""
        else:
            return self.time[(key, timestamp)]
