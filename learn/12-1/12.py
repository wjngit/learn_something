# 面试题 05.03. 翻转数位
#
# 给定一个32位整数 num，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。
#
# 示例 1：
# 输入: num = 1775(110111011112)
# 输出: 8
#
# 示例 2：
# 输入: num = 7(01112)
# 输出: 4


class Solution:
    def reverseBits(self, num: int) -> int:
        # if num == 0:
        #     return 1
        # nums = [None] * 32
        # for i in range(32):
        #     nums[i] = num & 1
        #     num >>= 1
        #
        # left_counts = [0] * 32
        # count = 0
        # for i in range(32):
        #     left_counts[i] = count
        #     if nums[i] == 1:
        #         count += 1
        #     else:
        #         count = 0
        #
        # right_counts = [0] * 32
        # count = 0
        # for i in range(31, -1, -1):
        #     right_counts[i] = count
        #     if nums[i] == 1:
        #         count += 1
        #     else:
        #         count = 0
        #
        # ret = 0
        # for i in range(32):
        #     if ret < left_counts[i] + right_counts[i] + 1:
        #         ret = left_counts[i] + right_counts[i] + 1
        # return ret

        pass


if __name__ == '__main__':
    # (110111011112)
    num1 = 1775
    # (01112)
    num2 = 7

    s = Solution()
    r1 = s.reverseBits(num1)
    r2 = s.reverseBits(num2)
    print(r1)
    print(r2)
