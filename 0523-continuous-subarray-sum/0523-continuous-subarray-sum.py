class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0:-1}
        s = 0
        mod = 0

        for i, x in enumerate(nums):
            s += x
            mod = s%k

            if mod in seen:
                if i - seen[mod] >= 2:
                    return True
            else:
                seen[mod] = i
        return False