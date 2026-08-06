class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        heapq.heapify(h)

        for i in nums:
            if len(h) < k:
                heapq.heappush(h, i)
            else:
                if i <= h[0]:
                    continue
                else:
                    heapq.heappushpop(h, i)
        return h[0]