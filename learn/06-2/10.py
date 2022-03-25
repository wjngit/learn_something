# 面试题 04.06. 后继者
#
# 设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。
# 如果指定节点没有对应的“下一个”节点，则返回null。
#
# 示例 1:
# 输入: root = [2,1,3], p = 1
#   2
#  / \
# 1   3
# 输出: 2
#
# 示例 2:
# 输入: root = [5,3,6,2,4,null,null,1], p = 6
#       5
#      / \
#     3   6
#    / \
#   2   4
#  /
# 1
# 输出: null


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.next = False
        self.node = None

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        #     self.order(root, p)
        #     return self.node
        #
        # def order(self, root, p):
        #     if not root:
        #         return
        #     self.order(root.left, p)
        #     if self.node:
        #         return
        #     if self.next:
        #         self.node = root
        #         self.next = False
        #         return
        #     if root == p:
        #         self.next = True
        #     self.order(root.right, p)

        pass


if __name__ == '__main__':
    pass
