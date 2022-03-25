# 94. 二叉树的中序遍历
# 给你二叉树的根节点 root ，返回它节点值的 中序 遍历。
#
# 示例 1：
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
#
# 示例 2：
# 输入：root = []
# 输出：[]
#
# 示例 3：
# 输入：root = [1]
# 输出：[1]
#
# 示例 4：
# 输入：root = [1,2]
# 输出：[2,1]
#
# 示例 5：
# 输入：root = [1,null,2]
# 输出：[1,2]
#
# 提示：
#     树中节点数目在范围 [0, 100] 内
#     -100 <= Node.val <= 100
#
# 进阶：递归算法很简单，你可以通过迭代算法完成吗？


from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create(data):
    root = None
    for i in data:
        nn = TreeNode(i)
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
                if n.left.val is not None:
                    q.append(n.left)
                if n.right.val is not None:
                    q.append(n.right)
    return root


def travel(root):
    if root is None:
        return
    q = [root]
    while q:
        n = q.pop(0)
        yield n.val
        # if n.left:
        if n.left and n.left.val is not None:
            q.append(n.left)
        # if n.right:
        if n.right and n.right.val is not None:
            q.append(n.right)


class Temp:
    def __init__(self, status=1, node=None):
        self.status = status
        self.node = node


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #     res = []
        #     self.in_order(root, res)
        #     return res
        #
        # def in_order(self, root, res):
        #     if not root:
        #         return
        #     self.in_order(root.left, res)
        #     res.append(root.val)
        #     self.in_order(root.right, res)

        pass

        # result = []
        # if not root:
        #     return result
        #
        # stack = [Temp(1, root)]
        # while stack:
        #     if stack[-1].status == 1:
        #         stack[-1].status = 2
        #         if stack[-1].node.left:
        #             stack.append(Temp(1, stack[-1].node.left))
        #             continue
        #     if stack[-1].status == 2:
        #         result.append(stack[-1].node.val)
        #         stack[-1].status = 3
        #         if stack[-1].node.right:
        #             stack.append(Temp(1, stack[-1].node.right))
        #             continue
        #     if stack[-1].status == 3:
        #         stack.pop()
        # return result

        pass


if __name__ == '__main__':
    root1 = [1, None, 2, 3]
    root2 = []
    root3 = [1]
    root4 = [1, 2]
    root5 = [1, None, 2]
    r1 = create(root1)
    r2 = create(root2)
    r3 = create(root3)
    r4 = create(root4)
    r5 = create(root5)
    # print([i for i in travel(r1)])
    # print([i for i in travel(r2)])
    # print([i for i in travel(r3)])
    # print([i for i in travel(r4)])
    # print([i for i in travel(r5)])

    s = Solution()
    r1 = s.inorderTraversal(r1)
    r2 = s.inorderTraversal(r2)
    r3 = s.inorderTraversal(r3)
    r4 = s.inorderTraversal(r4)
    r5 = s.inorderTraversal(r5)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
