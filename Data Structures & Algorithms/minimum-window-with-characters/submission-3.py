class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        goal = {}
        for ch in t:
            goal[ch] = goal.get(ch,0) + 1
        
        track = {}
        shortest = None
        best_length = float('inf')
        while r < len(s):
            track[s[r]] = track.get(s[r], 0) + 1
            
            passes = True
            for ch in goal:
                if track.get(ch,0) < goal[ch]:
                    passes = False
                    break
            if passes:
                while passes:
                    track[s[l]] -= 1
                    l += 1
                    for ch in goal:
                        if track.get(ch,0) < goal[ch]:
                            passes = False
                            break
                l -= 1
                if r - l + 1 < best_length:
                    shortest = (l, r)
                    best_length = r - l + 1

                l += 1
            
            r += 1
        
        if not shortest:
            return ""
        
        
        return s[shortest[0]:shortest[1] + 1]


