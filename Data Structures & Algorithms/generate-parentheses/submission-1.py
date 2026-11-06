class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n is the number of pairs of brackets we have
        # We could think of each opening bracket as going a level deeper
        # Closing bracket as going back one level up? Or on the same level
        result = []

        def backtracking(s, op, cl):
            if op == cl == n:
                result.append(s)
            
            if op < n:
                backtracking(s + "(", op+1, cl)
            if cl < op:
                backtracking(s + ")", op, cl+1)
        
        backtracking("", 0, 0)
        return result
            


        