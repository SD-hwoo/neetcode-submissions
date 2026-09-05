class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        pairs.sort()
        pairs = pairs[::-1]
        stack = []
        for i in range(len(position)):
            pos = pairs[i][0]
            sp = pairs[i][1]

            time = (target - pos) / sp

            if not stack or time > stack[-1]:
                stack.append(time)
        return(len(stack))