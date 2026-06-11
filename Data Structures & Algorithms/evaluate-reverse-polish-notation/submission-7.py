class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        token_stack = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                token_stack.append(int(token))
            else:
                print(token_stack)
                token2 = token_stack.pop()
                token1 = token_stack.pop()
                
                if token == "+":
                    token3 = token1 + token2
                elif token == "-":
                    token3 = token1 - token2
                elif token == "*":
                    token3 = token1 * token2
                else:
                    token3 = int(token1 / token2)
                token_stack.append(token3)
        return token_stack.pop()
