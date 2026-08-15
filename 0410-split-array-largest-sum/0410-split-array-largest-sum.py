class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(arr_num):
            s = 0
            sub_num = 1
            for num in nums:
                if s + num > arr_num:
                    sub_num += 1
                    s = num
                else:
                     s += num
            return sub_num <= k
        lo = max(nums)
        hi = sum(nums)

        while lo <= hi:
            mid = (hi - lo) // 2 + lo
            if check(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo