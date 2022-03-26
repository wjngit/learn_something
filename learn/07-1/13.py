# 124. 二叉树中的最大路径和
#
# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。
# 该路径 至少包含一个 节点，且不一定经过根节点。
# 路径和 是路径中各节点值的总和。
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。
#
# 示例 1：
# 输入：root = [1,2,3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
#
# 示例 2：
# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
#
# 提示：
# 树中节点数目范围是 [1, 3 * 104]
# -1000 <= Node.val <= 1000


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = -1001

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.order(root)
        return self.result

    def order(self, root):
        if not root:
            return 0
        left = self.order(root.left)
        right = self.order(root.right)
        num = root.val
        if left > 0:
            num += left
        if right > 0:
            num += right
        if num > self.result:
            self.result = num
        ret = root.val
        if ret < left + root.val:
            ret = left + root.val
        if ret < right + root.val:
            ret = right + root.val
        return ret


if __name__ == '__main__':
    pass
