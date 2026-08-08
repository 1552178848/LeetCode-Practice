class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ndist_h = []

        for x, y in points:
            ndist = - (x**2 + y**2)
            if len(ndist_h) < k:
                heapq.heappush(ndist_h, (ndist, x, y))
            else:
                heapq.heappushpop(ndist_h, (ndist, x, y))
        return [[x, y] for ndist, x, y in ndist_h]