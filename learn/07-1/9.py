# 889. 根据前序和后序遍历构造二叉树
#
# 给定两个整数数组，preorder 和 postorder ，其中 preorder 是一个具有 无重复 值的二叉树的前序遍历，
# postorder 是同一棵树的后序遍历，重构并返回二叉树。
# 如果存在多个答案，您可以返回其中 任何 一个。
#
# 示例 1：
# 输入：preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
# 输出：[1,2,3,4,5,6,7]
#
# 示例 2:
# 输入: preorder = [1], postorder = [1]
# 输出: [1]
#
# 提示：
#     1 <= preorder.length <= 30
#     1 <= preorder[i] <= preorder.length
#     preorder 中所有值都 不同
#     postorder.length == preorder.length
#     1 <= postorder[i] <= postorder.length
#     postorder 中所有值都 不同
#     保证 preorder 和 postorder 是同一棵二叉树的前序遍历和后序遍历


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        #     return self.tree(preorder, 0, len(preorder) - 1, postorder, 0, len(postorder) - 1)
        #
        # def tree(self, preorder, i, j, postorder, p, r):
        #     if i > j:
        #         return
        #     root = TreeNode(preorder[i])
        #     if i == j:
        #         return root
        #     q = p
        #     while postorder[q] != preorder[i + 1]:
        #         q += 1
        #     left_size = q - p + 1
        #     left_node = self.tree(preorder, i + 1, i + left_size, postorder, p, q)
        #     right_node = self.tree(preorder, i + left_size + 1, j, postorder, q + 1, r - 1)
        #     root.left = left_node
        #     root.right = right_node
        #     return root

        pass


if __name__ == '__main__':
    pass
