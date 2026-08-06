class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []

        for i in nums:
            if len(h) < k:
                heapq.heappush(h, i)
            else:
                heapq.heappushpop(h, i)
        return h[0]