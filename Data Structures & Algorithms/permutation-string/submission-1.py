class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        s1_track = {}
        for letter in s1:
            s1_track[letter] = s1_track.get(letter, 0) + 1
        s2_track = {}

        while r < len(s2):
            s2_track[s2[r]] = s2_track.get(s2[r], 0) + 1
            print(s2_track)
            passes = True
            for key in s2_track:
                if s2_track[key] != s1_track.get(key, 0):
                    passes = False
                    break
            if passes:
                for key in s1_track:
                    if s1_track[key] != s2_track.get(key, 0):
                        passes = False
                        break
            if passes:
                return True
            distance = r - l + 1
            if distance == len(s1):
                s2_track[s2[l]] -= 1
                l += 1
            r += 1
        return False