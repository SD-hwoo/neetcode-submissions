class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        seen = set()
        l = 0
        seen.add(s[l])
        longest = 1
        r = 1
        while r < len(s):
            if s[r] in seen:
                if len(seen) > longest:
                    longest = len(seen)
                while s[r] in seen and l != r:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
            else:
                seen.add(s[r])
            r += 1
        if len(seen) > longest:
            longest = len(seen)
        return longest