class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        stack.append(0)
        result = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            if stack and temperatures[i] < temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and (temperatures[i] > temperatures[stack[-1]]):
                    j = stack.pop()
                    result[j] = i - j
                stack.append(i)
        return result