# 面试题 08.01. 三步问题
#
# 三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。
# 实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。
#
# 示例1:
# 输入：n = 3
# 输出：4
# 说明: 有四种走法
#
# 示例2:
# 输入：n = 5
# 输出：13
#
# 提示:n范围在[1, 1000000]之间


class Solution:
    # mod = 1000000007
    # memo = {}
    #
    # def waysToStep(self, n: int) -> int:
    #     return self.waysToStep_r(n)
    #
    # def waysToStep_r(self, n):
    #     if n == 1:
    #         return 1
    #     if n == 2:
    #         return 2
    #     if n == 3:
    #         return 4
    #     if n in self.memo:
    #         return self.memo[n]
    #     data = ((self.waysToStep_r(n - 1) + self.waysToStep_r(n - 2)) % self.mod + self.waysToStep_r(n - 3)) % self.mod
    #     self.memo[n] = data
    #     return data

    pass

    def waysToStep(self, n: int) -> int:
        # mod = 1000000007
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # if n == 3:
        #     return 4
        # x, y, z = 1, 2, 4
        # temp, k = 0, 4
        # while k <= n:
        #     temp = ((x + y) % mod + z) % mod
        #     x = y
        #     y = z
        #     z = temp
        #     k += 1
        # return temp

        pass


if __name__ == '__main__':
    n1 = 900750
    n2 = 3
    n3 = 5

    s = Solution()
    r1 = s.waysToStep(n1)
    r2 = s.waysToStep(n2)
    r3 = s.waysToStep(n3)
    print(r1)
    print(r2)
    print(r3)
