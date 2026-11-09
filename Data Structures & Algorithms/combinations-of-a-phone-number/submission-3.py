class Solution:
    def __init__(self):
        self.chars = {
                '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'
            }

    def letterCombinations(self, digits: str) -> List[str]:
        # Each string has to be len(digits)
        # Each digit is a layer
        # Each layer we loop through every character
        result = []
        path = []

        def backtracking(pos):
            if len(path) == len(digits):
                result.append(''.join(path))
                return
            
            for ch in self.chars[digits[pos]]:
                path.append(ch)
                backtracking(pos + 1)
                path.pop()
            
        if digits:
            backtracking(0)
        return result
        