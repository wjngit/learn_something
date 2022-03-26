# 105. 从前序与中序遍历序列构造二叉树
#
# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
#
# 示例 1:
# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]
#
# 示例 2:
# 输入: preorder = [-1], inorder = [-1]
# 输出: [-1]
#
# 提示:
#     1 <= preorder.length <= 3000
#     inorder.length == preorder.length
#     -3000 <= preorder[i], inorder[i] <= 3000
#     preorder 和 inorder 均 无重复 元素
#     inorder 均出现在 preorder
#     preorder 保证 为二叉树的前序遍历序列
#     inorder 保证 为二叉树的中序遍历序列


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        #     return self.tree(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
        #
        # def tree(self, preorder, i, j, inorder, p, r):
        #     if i > j:
        #         return
        #     root = TreeNode(preorder[i])
        #     q = p
        #     while inorder[q] != preorder[i]:
        #         q += 1
        #     left_size = q - p
        #     left_node = self.tree(preorder, i + 1, i + left_size, inorder, p, q - 1)
        #     right_node = self.tree(preorder, i + left_size + 1, j, inorder, q + 1, r)
        #     root.left = left_node
        #     root.right = right_node
        #     return root

        pass


if __name__ == '__main__':
    pass
