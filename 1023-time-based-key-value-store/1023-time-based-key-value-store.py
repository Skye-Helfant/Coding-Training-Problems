from collections import defaultdict
from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.log = defaultdict(list)
        print("TimeMap object created")

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.log:
            self.log[key] = []
        self.log[key].append([value, timestamp])
        print(f"Setting value '{value}' with timestamp {timestamp} for key '{key}'")

    def get(self, key: str, timestamp: int) -> str:
        sol = ""
        values = self.log.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                sol = values[m][0]
                l = m + 1
            else:
                r = m - 1
        print(f"Getting value for key '{key}' with timestamp {timestamp}")
        return sol
