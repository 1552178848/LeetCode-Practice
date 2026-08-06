class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1
        
        h = []
        for num, freq in count.items():
            if len(h) < k:
                heapq.heappush(h, (freq, num))
            else:
                heapq.heappushpop(h, (freq, num))
        return [num for freq, num in h]