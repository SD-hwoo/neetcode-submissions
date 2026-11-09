class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            if len(s) < 2:
                return True

            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True
        
        result = []
        path = []
        
        def backtracking(start):
            if start == len(s):
                result.append(list(path))

            for i in range(start, len(s)):
                new_sub = s[start:i + 1]
                if is_palindrome(new_sub):
                    path.append(new_sub)
                    backtracking(i + 1)
                    path.pop()

        backtracking(0)
        return result