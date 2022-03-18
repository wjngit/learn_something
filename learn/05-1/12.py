# 69. x 的平方根
#
# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
#
# 示例 1：
# 输入：x = 4
# 输出：2
#
# 示例 2：
# 输入：x = 8
# 输出：2
# 解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
#
# 提示：0 <= x <= 2^31 - 1

class Solution:
    def mySqrt(self, x: int) -> int:
        # if x == 0:
        #     return 0
        # low, high = 1, x
        # while low <= high:
        #     mid = low + (high - low) // 2
        #     num = mid * mid
        #     if num == x:
        #         return mid
        #     if num < x:
        #         num2 = (mid + 1) * (mid + 1)
        #         if num2 > x:
        #             return mid
        #         low = mid + 1
        #     else:
        #         high = mid - 1

        pass

        #     # todo: 保留6位小数的方法
        #     if x == 0:
        #         return 0
        #     low, high = 1, x
        #     front = 0
        #     while low <= high:
        #         mid = low + (high - low) // 2
        #         k = mid * mid
        #         if k == x:
        #             front = mid
        #         if k > x:
        #             high = mid - 1
        #         else:
        #             kk = (mid + 1) * (mid + 1)
        #             if kk > x:
        #                 front = mid
        #             low = mid + 1
        #
        #     if front * front == x:
        #         return front
        #     new_front = front
        #     for i in range(1, 7):
        #         b = 10 ** (-i)
        #         temp = [new_front + b * j for j in range(10)]
        #         temp_front = self.get_num(temp, x)
        #         if temp_front != new_front:
        #             new_front = temp_front
        #
        #     return new_front
        #
        # @staticmethod
        # def get_num(data, x):
        #     for m in range(1, 10):
        #         if data[m] * data[m] > x > data[m - 1] * data[m - 1]:
        #             return data[m - 1]
        #     return data[-1]

        pass


if __name__ == '__main__':
    x1 = 1
    x2 = 8
    x3 = 34

    s = Solution()
    r3 = s.mySqrt(x3)
    r1 = s.mySqrt(x1)
    r2 = s.mySqrt(x2)
    print(r1)
    print(r2)
    print(r3)
