# -*- coding:utf-8 -*-
"""
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1：
输入：p = [1,2,3], q = [1,2,3]
输出：true

示例 2：
输入：p = [1,2], q = [1,null,2]
输出：false

示例 3：
输入：p = [1,2,1], q = [1,1,2]
输出：false
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        # def travel_tree_data(root):
        #     if root is None:
        #         return
        #     q = [root]
        #     while q:
        #         n = q.pop(0)
        #         yield n.val
        #         if n.left:
        #             q.append(n.left)
        #         if n.right:
        #             q.append(n.right)
        #
        # return True if [i for i in travel_tree_data(p)] == [i for i in travel_tree_data(q)] else False

        if not p and not q:
            return True
        if p and q:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False


def create_tree(data_list):
    root = None
    for data in data_list:
        nn = TreeNode(data)
        if root is None:
            root = nn
        else:
            q = [root]
            while q:
                n = q.pop(0)
                if n.left is None:
                    n.left = nn
                    q = []
                    continue
                if n.right is None:
                    n.right = nn
                    q = []
                    continue
                q.append(n.left)
                q.append(n.right)
    return root


# def travel_tree(root):
#     if root is None:
#         return
#     q = [root]
#     while q:
#         n = q.pop(0)
#         yield n.val
#         if n.left:
#             q.append(n.left)
#         if n.right:
#             q.append(n.right)


if __name__ == '__main__':
    p1, q1 = [1, 2, 3], [1, 2, 3]
    p2, q2 = [1, 2], [1, None, 2]
    p3, q3 = [1, 2, 1], [1, 1, 2]
    p1_root, q1_root = create_tree(p1), create_tree(q1)
    # p1_list = [i for i in travel_tree(p1_root)]
    # print(p1_list)
    p2_root, q2_root = create_tree(p2), create_tree(q2)
    p3_root, q3_root = create_tree(p3), create_tree(q3)
    s = Solution()
    ret1 = s.isSameTree(p1_root, q1_root)
    ret2 = s.isSameTree(p2_root, q2_root)
    ret3 = s.isSameTree(p3_root, q3_root)
    print(ret1)
    print(ret2)
    print(ret3)
