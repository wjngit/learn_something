# 剑指 Offer 33. 二叉搜索树的后序遍历序列
#
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
# 如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
# 参考以下这颗二叉搜索树：
#      5
#     / \
#    2   6
#   / \
#  1   3
#
# 示例 1：
# 输入: [1,6,3,2,5]
# 输出: false
#
# 示例 2：
# 输入: [1,3,2,6,5]
# 输出: true
#
# 提示：数组长度 <= 1000


from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        #     return self.verify(postorder, 0, len(postorder) - 1)
        #
        # def verify(self, postorder, i, j):
        #     if i >= j:
        #         return True
        #     k = i
        #     while k < j and postorder[k] < postorder[j]:
        #         k += 1
        #     p = k
        #     while p < j:
        #         if postorder[j] > postorder[p]:
        #             return False
        #         p += 1
        #     left_valid = self.verify(postorder, i, k - 1)
        #     if not left_valid:
        #         return False
        #     right_valid = self.verify(postorder, k, j - 1)
        #     return right_valid

        pass


if __name__ == '__main__':
    pass
