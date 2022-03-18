# 374. 猜数字大小
#
# 猜数字游戏的规则如下：
#     每轮游戏，我都会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。
#     如果你猜错了，我会告诉你，你猜测的数字比我选出的数字是大了还是小了。
# 你可以通过调用一个预先定义好的接口 int guess(int num) 来获取猜测结果，返回值一共有 3 种可能的情况（-1，1 或 0）：
#     -1：我选出的数字比你猜的数字小 pick < num
#     1：我选出的数字比你猜的数字大 pick > num
#     0：我选出的数字和你猜的数字一样。恭喜！你猜对了！pick == num
# 返回我选出的数字。
#
# 示例 1：
# 输入：n = 10, pick = 6
# 输出：6
#
# 示例 2：
# 输入：n = 1, pick = 1
# 输出：1
#
# 示例 3：
# 输入：n = 2, pick = 1
# 输出：1
#
# 示例 4：
# 输入：n = 2, pick = 2
# 输出：2
#
# 提示：
#     1 <= n <= 2^31 - 1
#     1 <= pick <= n


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int, pick) -> int:
    if num == pick:
        return 0
    if num > pick:
        return -1
    else:
        return 1


class Solution:
    def __init__(self, pick):
        self.pick = pick

    def guessNumber(self, n: int) -> int:
        # left, right = 1, n
        # while left <= right:
        #     mid = left + (right - left) // 2
        #     ret = guess(mid, self.pick)
        #     if ret == 0:
        #         return mid
        #     elif ret == -1:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return -1

        pass


if __name__ == '__main__':
    n1 = 10
    pick1 = 6
    n2 = 1
    pick2 = 1
    n3 = 2
    pick3 = 1
    n4 = 2
    pick4 = 2

    s1 = Solution(pick1)
    s2 = Solution(pick2)
    s3 = Solution(pick3)
    s4 = Solution(pick4)
    r1 = s1.guessNumber(n1)
    r2 = s2.guessNumber(n2)
    r3 = s3.guessNumber(n3)
    r4 = s4.guessNumber(n4)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
