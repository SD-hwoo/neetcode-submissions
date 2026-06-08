class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        non_zero = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                non_zero *= num
            else:
                zero_count += 1
            total_product *= num
        result = []
        for num in nums:
            if num != 0:
                result.append(total_product // num)
            else:
                result.append(non_zero if zero_count == 1 else 0)
        return result