class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.big, -heapq.heappop(self.small))
        if len(self.big) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.big))
                

    def findMedian(self) -> float:
        if (len(self.small) + len(self.big)) % 2 == 0:
            return (-self.small[0] + self.big[0]) / 2
        else:
            return -self.small[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()