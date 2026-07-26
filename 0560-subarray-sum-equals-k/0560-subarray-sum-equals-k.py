class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0 : 1}
        ans = s = 0

        for num in nums:
            s += num
            ans += seen.get(s-k, 0)
            seen[s] = seen.get(s, 0) + 1
        return ans