class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        ans = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum >= target:
                window_sum -= nums[left]
                ans = min(ans, right - left + 1)
                left += 1
        
        return 0 if ans == float('inf') else ans


