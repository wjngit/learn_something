# 437. 路径总和 III
#
# https://leetcode-cn.com/problems/path-sum-iii/
#
# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
#
# 示例 1：
# 输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# 输出：3
# 解释：和等于 8 的路径有 3 条，如图所示。
#
# 示例 2：
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：3
#
# 提示:
# 二叉树的节点个数的范围是 [0,1000]
# -109 <= Node.val <= 109
# -1000 <= targetSum <= 1000


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        #     self.dfs(root, targetSum)
        #     return self.count
        #
        # def __init__(self):
        #     self.count = 0
        #
        # def dfs(self, root, target):
        #     if not root:
        #         return {}
        #     left = self.dfs(root.left, target)
        #     right = self.dfs(root.right, target)
        #     root_value = {root.val: 1}
        #     for key, value in left.items():
        #         key += root.val
        #         if key in root_value:
        #             value += root_value[key]
        #         root_value[key] = value
        #     for key, value in right.items():
        #         key += root.val
        #         if key in root_value:
        #             value += root_value[key]
        #         root_value[key] = value
        #     for key, value in root_value.items():
        #         if key == target:
        #             self.count += value
        #     return root_value

        pass

        #     self.dfs(root, [], targetSum)
        #     return self.count
        #
        # def __init__(self):
        #     self.count = 0
        #
        # def dfs(self, root, path, targetSum):
        #     if not root:
        #         return
        #     path.append(root.val)
        #     curSum = 0
        #     for i in range(len(path) - 1, -1, -1):
        #         curSum += path[i]
        #         if curSum == targetSum:
        #             self.count += 1
        #     self.dfs(root.left, path, targetSum)
        #     self.dfs(root.right, path, targetSum)
        #     path.pop()

        pass


if __name__ == '__main__':
    pass
