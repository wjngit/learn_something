# 56. 合并区间
#
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
#
# 示例 1：
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
# 示例 2：
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals = sorted(intervals, key=lambda item: item[0])
        # cur_l, cur_r = intervals[0][0], intervals[0][1]
        # result = []
        # for i in range(1, len(intervals)):
        #     if intervals[i][0] <= cur_r:
        #         if intervals[i][1] > cur_r:
        #             cur_r = intervals[i][1]
        #     else:
        #         result.append([cur_l, cur_r])
        #         cur_l = intervals[i][0]
        #         cur_r = intervals[i][1]
        # result.append([cur_l, cur_r])
        # return result

        pass


if __name__ == '__main__':
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals2 = [[1, 4], [4, 5]]

    s = Solution()
    r1 = s.merge(intervals1)
    r2 = s.merge(intervals2)
    print(r1)
    print(r2)
