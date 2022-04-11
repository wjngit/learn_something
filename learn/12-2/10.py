# 231. 2 的幂
#
# 给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
# 如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。
#
# 示例 1：
# 输入：n = 1
# 输出：true
# 解释：20 = 1
#
# 示例 2：
# 输入：n = 16
# 输出：true
# 解释：24 = 16
#
# 示例 3：
# 输入：n = 3
# 输出：false
#
# 示例 4：
# 输入：n = 4
# 输出：true
#
# 示例 5：
# 输入：n = 5
# 输出：false
#
# 提示：-2^31 <= n <= 2^31 - 1
#
# 进阶：你能够不使用循环/递归解决此问题吗？


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n != 0:
            if (n & 1) == 1:
                if (n >> 1) == 0:
                    return True
                else:
                    return False
            n >>= 1
        return False


if __name__ == '__main__':
    n1 = 1
    n2 = 16
    n3 = 3
    n4 = 4
    n5 = 5

    s = Solution()
    r1 = s.isPowerOfTwo(n1)
    r2 = s.isPowerOfTwo(n2)
    r3 = s.isPowerOfTwo(n3)
    r4 = s.isPowerOfTwo(n4)
    r5 = s.isPowerOfTwo(n5)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
