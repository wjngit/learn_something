# 367. 有效的完全平方数
#
# 给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
#
# 进阶：不要 使用任何内置的库函数，如  sqrt 。
#
# 示例 1：
# 输入：num = 16
# 输出：true
#
# 示例 2：
# 输入：num = 14
# 输出：false
#
# 提示：1 <= num <= 2^31 - 1

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # low, high = 1, num
        # while low <= high:
        #     mid = low + (high - low) // 2
        #     new = mid * mid
        #     if new == num:
        #         return True
        #     if new > num:
        #         high = mid - 1
        #     else:
        #         low = mid + 1
        # return False

        pass


if __name__ == '__main__':
    num1 = 16
    num2 = 14

    s = Solution()
    r1 = s.isPerfectSquare(num1)
    r2 = s.isPerfectSquare(num2)
    print(r1)
    print(r2)
