class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        goal = {}
        for ch in t:
            if ch not in goal:
                goal[ch] = 1
            else:
                goal[ch] += 1
        
        have = 0
        track = {}
        shortest = None
        dist = float('inf')
        while r < len(s):
            track[s[r]] = track.get(s[r], 0) + 1
            
            if s[r] in goal:
                if track[s[r]] <= goal[s[r]]:
                    have += 1
            
            while have == len(t):
                if r - l + 1 < dist:
                    dist = r - l + 1
                    shortest = (l, r)

                track[s[l]] -= 1

                if track[s[l]] < goal.get(s[l], 0):
                    have -= 1
                l += 1
            
            r += 1

        if not shortest:
            return ""
        return s[shortest[0]:shortest[1] + 1]
            
