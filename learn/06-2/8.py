# 剑指 Offer 54. 二叉搜索树的第k大节点
#
# 给定一棵二叉搜索树，请找出其中第 k 大的节点的值。
#
# 示例 1:
# 输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 4
#
# 示例 2:
# 输入: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# 输出: 4
#
# 限制：1 ≤ k ≤ 二叉搜索树元素个数

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.count = 0
        self.result = 0

    def kthLargest(self, root: TreeNode, k: int) -> int:
        #     self.order(root, k)
        #     return self.result
        #
        # def order(self, root, k):
        #     if not root:
        #         return
        #     self.order(root.right, k)
        #     if self.count >= k:
        #         return
        #     self.count += 1
        #     if self.count == k:
        #         self.result = root.val
        #         return
        #     self.order(root.left, k)

        pass


if __name__ == '__main__':
    pass
