# 1306. 跳跃游戏 III
#
# 这里有一个非负整数数组 arr，你最开始位于该数组的起始下标 start 处。当你位于下标 i 处时，你可以跳到 i + arr[i] 或者 i - arr[i]。
# 请你判断自己是否能够跳到对应元素值为 0 的 任一 下标处。
# 注意，不管是什么情况下，你都无法跳到数组之外。
#
# 示例 1：
# 输入：arr = [4,2,3,0,3,1,2], start = 5
# 输出：true
# 解释：
# 到达值为 0 的下标 3 有以下可能方案：
# 下标 5 -> 下标 4 -> 下标 1 -> 下标 3
# 下标 5 -> 下标 6 -> 下标 4 -> 下标 1 -> 下标 3
#
# 示例 2：
# 输入：arr = [4,2,3,0,3,1,2], start = 0
# 输出：true
# 解释：
# 到达值为 0 的下标 3 有以下可能方案：
# 下标 0 -> 下标 4 -> 下标 1 -> 下标 3
#
# 示例 3：
# 输入：arr = [3,0,2,1,2], start = 2
# 输出：false
# 解释：无法到达值为 0 的下标 1 处。
#
# 提示：
# 1 <= arr.length <= 5 * 10^4
# 0 <= arr[i] < arr.length
# 0 <= start < arr.length


from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        #     self.visited = [False] * len(arr)
        #     self.dfs(arr, start)
        #     return self.reached
        #
        # def __init__(self):
        #     self.visited = None
        #     self.reached = False
        #
        # def dfs(self, arr, curi):
        #     if self.reached:
        #         return
        #     if arr[curi] == 0:
        #         self.reached = True
        #         return
        #     self.visited[curi] = True
        #     move2left = curi - arr[curi]
        #     if move2left >= 0 and move2left < len(arr) and self.visited[move2left] == False:
        #         self.dfs(arr, move2left)
        #     move2right = curi + arr[curi]
        #     if move2right >= 0 and move2right < len(arr) and self.visited[move2right] == False:
        #         self.dfs(arr, move2right)

        pass


if __name__ == '__main__':
    arr1 = [4, 2, 3, 0, 3, 1, 2]
    start1 = 5
    arr2 = [4, 2, 3, 0, 3, 1, 2]
    start2 = 0
    arr3 = [3, 0, 2, 1, 2]
    start3 = 2

    s1 = Solution()
    s2 = Solution()
    s3 = Solution()
    r1 = s1.canReach(arr1, start1)
    r2 = s2.canReach(arr2, start2)
    r3 = s3.canReach(arr3, start3)
    print(r1)
    print(r2)
    print(r3)
