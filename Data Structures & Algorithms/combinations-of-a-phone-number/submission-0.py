class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Each string has to be len(digits)
        # Each digit is a layer
        # Each layer we loop through every character
        chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []

        def backtracking(s, pos):
            if len(s) == len(digits):
                result.append(s)
                return
            
            for ch in chars[digits[pos]]:
                backtracking(s + ch, pos + 1)
            
        if digits:
            backtracking('', 0)
        return result
        