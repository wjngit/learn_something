# 252. 会议室
#
# 给一个会议安排时间数组，每个会议时间都包含开始时间和结束时间，判断一个人能否参加所有会议。
#
# 示例1：
# 输入：intervals = [[0,30],[5,10],[15,20]]
# 输出：False
#
# 示例2：
# 输入：intervals = [[7,10],[2,4],[15,20]]
# 输出：True

from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # intervals = sorted(intervals, key=lambda item: item[0])
        # for i in range(1, len(intervals)):
        #     if intervals[i][0] < intervals[i - 1][1]:
        #         return False
        # return True

        pass


if __name__ == '__main__':
    intervals1 = [[0, 30], [5, 10], [15, 20]]
    intervals2 = [[7, 10], [2, 4], [15, 20]]

    s = Solution()
    r1 = s.canAttendMeetings(intervals1)
    r2 = s.canAttendMeetings(intervals2)
    print(r1)
    print(r2)
