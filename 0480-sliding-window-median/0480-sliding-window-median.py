class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # 堆里存 (值, 下标):下标全局唯一,同值元素从此可区分
        # 死活判定 = 下标是否 < 窗口左界,不再需要死亡名单和 alive 计数
        small, large = [], []            # small 存 (-v, idx) 大顶堆;large 存 (v, idx) 小顶堆

        # 初始化:前 k 个全进 small,再把最大的 ceil(k/2) 个搬去 large
        # 约定:large 持有 ceil(k/2) 个,k 为奇数时中位数在 large 堆顶
        for i in range(k):
            heapq.heappush(small, (-nums[i], i))
        for _ in range((k + 1) // 2):
            v, idx = heapq.heappop(small)
            heapq.heappush(large, (-v, idx))

        def med():
            return float(large[0][0]) if k % 2 else (large[0][0] - small[0][0]) / 2

        ans = [med()]
        for i in range(k, len(nums)):
            x, y = nums[i], nums[i - k]          # x 进窗,y 出窗
            if x >= large[0][0]:                 # x 属大半场
                heapq.heappush(large, (x, i))
                if y <= large[0][0]:             # 而 y 属小半场:一进一出不同侧,补偿过户
                    v, idx = heapq.heappop(large)
                    heapq.heappush(small, (-v, idx))
            else:                                # x 属小半场
                heapq.heappush(small, (-x, i))
                if y >= large[0][0]:             # 而 y 属大半场:反向补偿
                    v, idx = heapq.heappop(small)
                    heapq.heappush(large, (-v, idx))

            lo = i - k + 1                       # 窗口左界
            while small and small[0][1] < lo:    # 清顶:按下标验死,精确到个体
                heapq.heappop(small)
            while large and large[0][1] < lo:
                heapq.heappop(large)

            ans.append(med())
        return ans