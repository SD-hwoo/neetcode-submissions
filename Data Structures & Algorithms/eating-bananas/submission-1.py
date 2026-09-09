class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        rates = []

        while r != l:
            hours = 0
            mid = (l + r) // 2
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours > h:
                l = mid + 1
            else:
                rates.append(mid)
                r = mid  
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / r)
        if hours <= h:
            rates.append(r)
        return min(rates)
