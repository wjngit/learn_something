# 102. 二叉树的层序遍历
#
# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
#
# 示例 1：
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
#
# 示例 2：
# 输入：root = [1]
# 输出：[[1]]
#
# 示例 3：
# 输入：root = []
# 输出：[]
#
# 提示：
# 树中节点数目在范围 [0, 2000] 内
# -1000 <= Node.val <= 1000


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # res = []
        # if not root:
        #     return res
        # q = [root]
        # while q:
        #     temp = []
        #     for _ in range(len(q)):
        #         node = q.pop(0)
        #         temp.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     res.append(temp)
        # return res

        pass


if __name__ == '__main__':
    pass
