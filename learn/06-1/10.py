# 513. 找树左下角的值
#
# 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
# 假设二叉树中至少有一个节点。
#
# 示例 1:
# 输入: root = [2,1,3]
# 输出: 1
#
# 示例 2:
# 输入: [1,2,3,4,null,5,6,null,null,7]
# 输出: 7
#
# 提示:
# 二叉树的节点个数的范围是 [1,104]
# -2^31 <= Node.val <= 2^31 - 1


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # res = -1
        # if not root:
        #     return res
        # q = [root]
        # while q:
        #     node = q.pop(0)
        #     res = node.val
        #     if node.right:
        #         q.append(node.right)
        #     if node.left:
        #         q.append(node.left)
        # return res

        pass


if __name__ == '__main__':
    pass
