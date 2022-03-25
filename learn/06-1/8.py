# 剑指 Offer 32 - III. 从上到下打印二叉树 III
#
# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，
# 第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
#
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#
# 提示：节点总数 <= 1000


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # res = []
        # if not root:
        #     return res
        # stack = [[root], []]
        # turn = 0
        # while stack[turn]:
        #     temp = []
        #     while stack[turn]:
        #         node = stack[turn].pop()
        #         temp.append(node.val)
        #         if turn == 0:
        #             if node.left:
        #                 stack[1].append(node.left)
        #             if node.right:
        #                 stack[1].append(node.right)
        #         else:
        #             if node.right:
        #                 stack[0].append(node.right)
        #             if node.left:
        #                 stack[0].append(node.left)
        #     res.append(temp)
        #     turn = (turn + 1) % 2
        # return res

        pass


if __name__ == '__main__':
    pass
