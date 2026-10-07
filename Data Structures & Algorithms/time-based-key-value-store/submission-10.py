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

            for t in self.keys[key][::-1]:
                if t <= timestamp:
                    return self.time[(key, t)]
            
            return ""
        else:
            return self.time[(key, timestamp)]
