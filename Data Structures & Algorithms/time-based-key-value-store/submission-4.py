class TimeMap:

    def __init__(self):
        self.key_dict = {}
        self.time_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_dict.keys():
            self.key_dict[key] = [timestamp]
        else:
            self.key_dict[key].append(timestamp)
        if key not in self.time_dict.keys():
            self.time_dict[key] = {}
        self.time_dict[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key in self.time_dict.keys():
            if timestamp in self.time_dict[key].keys():
                return self.time_dict[key][timestamp]
            else:
                for time in self.key_dict[key][::-1]:
                    if time <= timestamp:
                        return self.time_dict[key][time] 
                return ""   
        else:
            return ""
