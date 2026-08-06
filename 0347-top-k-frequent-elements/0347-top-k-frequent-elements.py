class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        h = []
        for num, freq in count.items():
            if len(h) < k:
                heapq.heappush(h, (freq, num))
            else:
                heapq.heappushpop(h, (freq, num))
        return [num for freq, num in h]