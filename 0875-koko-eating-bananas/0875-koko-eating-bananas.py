class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
           hour = (sum(math.ceil(p / k) for p in piles))
           return hour <= h
        lo = 1
        hi = max(piles)

        while lo <= hi:
            mid = (hi - lo) // 2 + lo
            if check(mid):
                hi = mid - 1
            else:
                lo = mid + 1

        return lo