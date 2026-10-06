class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        goal = {}
        for ch in t:
            goal[ch] = goal.get(ch,0) + 1
        
        have = 0
        track = {}
        shortest = None
        best_length = float('inf')
        while r < len(s):
            track[s[r]] = track.get(s[r], 0) + 1
            
            if s[r] in goal:
                if track[s[r]] <= goal[s[r]]:
                    have += 1

            while have >= len(t):
                if r - l + 1 < best_length:
                    shortest = (l, r)
                    best_length = r - l + 1

                track[s[l]] -= 1
                if s[l] in goal:
                    if track[s[l]] < goal[s[l]]:
                        have -= 1
                l += 1
            r += 1
        
        if not shortest:
            return ""
        
        
        return s[shortest[0]:shortest[1] + 1]


