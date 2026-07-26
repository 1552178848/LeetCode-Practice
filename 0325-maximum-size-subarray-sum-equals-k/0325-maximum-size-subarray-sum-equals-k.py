class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        first = {0:-1}
        s = best = 0

        for i, x in enumerate(nums):
            s += x
            if s-k in first:
                best = max(best, i - first[s-k])
            if s not in first:
                first[s] = i
        return best