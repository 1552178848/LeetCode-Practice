class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        deq = deque()
        s = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            s[i+1] = s[i] + nums[i]
        ans = float('inf')

        for j in range(len(nums) + 1):
            while deq and s[j] - s[deq[0]] >= k:
                ans = min(ans, j - deq.popleft())
            
            while deq and s[deq[-1]] >= s[j]:
                deq.pop()
            deq.append(j)

        return ans if ans != float('inf') else -1