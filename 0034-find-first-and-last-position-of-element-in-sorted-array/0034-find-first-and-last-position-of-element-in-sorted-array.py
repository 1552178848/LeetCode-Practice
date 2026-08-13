class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(nums) - 1
        ans = []

        def searchInsert(nums: List[int], target: int) -> int:
            lo = 0
            hi = len(nums) - 1
            while lo <= hi:
                mid = (hi - lo) //2 + lo
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return lo

        left = searchInsert(nums, target)
        right = searchInsert(nums, target + 1) - 1

        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        return [left, right]    

                