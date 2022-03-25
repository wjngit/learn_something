# 101. 对称二叉树
#
# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
#
# 示例 1：
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
#
# 示例 2：
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
#
# 提示：
# 树中节点数目在范围 [1, 1000] 内
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #     if not root:
        #         return True
        #     return self.sys(root.left, root.right)
        #
        # def sys(self, left, right):
        #     if not left and not right:
        #         return True
        #     if left and right and left.val == right.val:
        #         return self.sys(left.right, right.left) and self.sys(left.left, right.right)
        #     return False

        pass


if __name__ == '__main__':
    pass
