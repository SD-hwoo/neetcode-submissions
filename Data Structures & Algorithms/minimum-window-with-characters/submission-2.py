class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        goal = {}
        for ch in t:
            goal[ch] = goal.get(ch,0) + 1
        
        track = {}
        shortest = s + t
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
                if r - l + 1 < len(shortest):
                    shortest = s[l:r + 1]
                l += 1
            
            r += 1
        
        if shortest == s + t:
            return ""
        
        
        return shortest


