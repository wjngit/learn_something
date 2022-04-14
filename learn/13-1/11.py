# 1094. 拼车
#
# 车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向）
# 给定整数 capacity 和一个数组 trips ,  trip[i] = [numPassengersi, fromi, toi] 表示第 i 次旅行有 numPassengersi 乘客，
# 接他们和放他们的位置分别是 fromi 和 toi 。这些位置是从汽车的初始位置向东的公里数。
# 当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。
#
# 示例 1：
# 输入：trips = [[2,1,5],[3,3,7]], capacity = 4
# 输出：false
#
# 示例 2：
# 输入：trips = [[2,1,5],[3,3,7]], capacity = 5
# 输出：true
#
# 提示：
# 1 <= trips.length <= 1000
# trips[i].length == 3
# 1 <= numPassengersi <= 100
# 0 <= fromi < toi <= 1000
# 1 <= capacity <= 105

from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = [0] * 1001
        for trip in trips:
            cap = trip[0]
            from_ = trip[1]
            to_ = trip[2]
            for i in range(from_, to_):
                n[i] += cap
        for i in range(1001):
            if n[i] > capacity:
                return False
        return True


if __name__ == '__main__':
    trips1 = [[2, 1, 5], [3, 5, 7]]
    capacity1 = 3
    trips2 = [[2, 1, 5], [3, 3, 7]]
    capacity2 = 5

    s = Solution()
    r1 = s.carPooling(trips1, capacity1)
    r2 = s.carPooling(trips2, capacity2)
    print(r1)
    print(r2)
