# 295. 数据流的中位数
#
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
# 例如，[2,3,4] 的中位数是 3
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
# 设计一个支持以下两种操作的数据结构：
#     void addNum(int num) - 从数据流中添加一个整数到数据结构中。
#     double findMedian() - 返回目前所有元素的中位数。
#
# 示例：
#     addNum(1)
#     addNum(2)
#     findMedian() -> 1.5
#     addNum(3)
#     findMedian() -> 2
#
# 进阶:
#     如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
#     如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


import heapq


class MedianFinder:

    def __init__(self):
        self.min_q = []
        self.max_q = []

    def addNum(self, num: int) -> None:
        if not self.max_q or num <= -self.max_q[0]:
            heapq.heappush(self.max_q, -num)
        else:
            heapq.heappush(self.min_q, num)
        while len(self.max_q) < len(self.min_q):
            e = heapq.heappop(self.min_q)
            heapq.heappush(self.max_q, -e)
        while len(self.min_q) < len(self.max_q) - 1:
            e = heapq.heappop(self.max_q)
            heapq.heappush(self.min_q, -e)

    def findMedian(self) -> float:
        if len(self.max_q) > len(self.min_q):
            return -self.max_q[0]
        else:
            return (-self.max_q[0] + self.min_q[0]) / 2.0
