class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first = {0:-1}
        best = 0
        s = 0

        for i, x in enumerate(nums):
            s += 1 if x == 1 else -1
            
            if s in first:
                best = max(best, i - first[s])
            else:
                first[s] = i
        
        return best
