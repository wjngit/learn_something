# 面试题 04.03. 特定深度节点链表
#
# 给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。
# 返回一个包含所有深度的链表的数组。
#
# 示例：
# 输入：[1,2,3,4,5,null,7,8]
#
#         1
#        /  \
#       2    3
#      / \    \
#     4   5    7
#    /
#   8
# 输出：[[1],[2,3],[4,5,7],[8]]


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        res = []
        if not tree:
            return res
        q = [tree]
        while q:
            new_head = ListNode(999)
            tail = new_head
            for _ in range(len(q)):
                node = q.pop(0)
                tail.next = ListNode(node.val)
                tail = tail.next
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(new_head.next)
        return res


if __name__ == '__main__':
    pass
