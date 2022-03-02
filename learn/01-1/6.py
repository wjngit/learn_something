# 9.回文数
#
# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 例如，121 是回文，而 123 不是。
#
# 示例1：
# 输入：x = 121
# 输出：true
#
# 示例2：
# 输入：x = -121
# 输出：false
# 解释：从左向右读, 为 - 121 。 从右向左读, 为 121 - 。因此它不是一个回文数。
#
# 示例3：
# 输入：x = 10
# 输出：false
# 解释：从右向左读, 为 01 。因此它不是一个回文数。
#
# 提示：
# -2**31 <= x <= 2**31 - 1
#
# 进阶：你能不将整数转为字符串来解决这个问题吗？

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        #     return False
        # if x % 10 == 0:
        #     return False
        # if str(x)[::-1] == str(x):
        #     return True
        # return False

        # if x < 0:
        #     return False
        # temp = [0] * len(str(2 ** 31))
        # i, j = x, 0
        # while i != 0:
        #     temp[j] = i % 10
        #     i //= 10
        #     j += 1
        # for k in range(j // 2):
        #     if temp[k] != temp[j - k - 1]:
        #         return False
        # return True

        # if x < 0:
        #     return False
        # origin_x = x
        # y = 0
        # while x != 0:
        #     y = y * 10 + x % 10
        #     x //= 10
        # return y == origin_x

        pass


if __name__ == '__main__':
    x1 = 121
    x2 = -121
    x3 = 10
    x4 = 0

    s = Solution()
    r1 = s.isPalindrome(x1)
    r2 = s.isPalindrome(x2)
    r3 = s.isPalindrome(x3)
    r4 = s.isPalindrome(x4)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
