class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # if len(s) < 2:
        #     return len(s)
        count = {}
        longest = 0
        l = 0
        # count[s[l]] = 1
        r = 0
        while r < len(s):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1
            
            highest = 0
            for letter in count:
                highest = max(count[letter], highest)
            distance = r - l + 1
            switches = distance - highest
            while switches > k:
                count[s[l]] -= 1
                l += 1
                highest = 0
                for letter in count:
                    highest = max(count[letter], highest)
                distance = r - l + 1
                switches = distance - highest
                
            longest = max(r - l + 1, longest)
            r += 1
        return longest
