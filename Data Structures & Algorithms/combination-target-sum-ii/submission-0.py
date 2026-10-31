class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        candidates.sort()
        def backtracking(current, start):
            if current == target:
                result.append(list(path))
                return
            if current > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtracking(current + candidates[i], i + 1)
                path.pop()

        backtracking(0, 0)
        return result