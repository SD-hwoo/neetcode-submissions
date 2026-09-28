class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = (-1, float('inf'))
        # sell = (-1, -1)
        profit = 0
        for i in range(len(prices)):
            if prices[i] < buy[1]:
                buy = (i, prices[i])
            profit = max(prices[i] - buy[1], profit)
            # elif prices[i] > sell[1] and i > buy[0]:
            #     sell = (i, prices[i])
        return profit
        
