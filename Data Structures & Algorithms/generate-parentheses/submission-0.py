class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n is the number of pairs of brackets we have
        # We could think of each opening bracket as going a level deeper
        # Closing bracket as going back one level up? Or on the same level
        result = []
        path = []

        def backtracking(op, cl):
            if op == cl == n:
                result.append(''.join(path))
            
            if op < n:
                path.append("(")    
                backtracking(op+1, cl)
                path.pop()
            if cl < op:
                path.append(")")
                backtracking(op, cl+1)
                path.pop()
        
        backtracking(0, 0)
        return result
            


        