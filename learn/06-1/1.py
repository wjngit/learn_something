# 144. 二叉树的前序遍历
# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
#
# 示例 1：
# 输入：root = [1,null,2,3]
# 输出：[1,2,3]
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
# 输出：[1,2]
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


# class SFrame:
#     def __init__(self, status=1, node=None):
#         """
#         1: 左右都未处理，需要处理左边
#         2: 左边处理完，需要处理右边
#         3: 右边处理完，需要处理下一个
#         """
#         self.status = status
#         self.node = node


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #     res = []
        #     self.pre_order(root, res)
        #     return res
        #
        # def pre_order(self, root, res):
        #     if not root:
        #         return
        #     res.append(root.val)
        #     self.pre_order(root.left, res)
        #     self.pre_order(root.right, res)

        pass

        # result = []
        # if not root:
        #     return []
        # stack = [SFrame(1, root)]
        # while stack:
        #     if stack[-1].status == 1:
        #         result.append(stack[-1].node.val)
        #         # 把状态置为2
        #         stack[-1].status = 2
        #         if stack[-1].node.left:
        #             stack.append(SFrame(1, stack[-1].node.left))
        #             continue
        #     if stack[-1].status == 2:
        #         # 把状态置为3
        #         stack[-1].status = 3
        #         if stack[-1].node.right:
        #             stack.append(SFrame(1, stack[-1].node.right))
        #         continue
        #     if stack[-1].status == 3:
        #         stack.pop()
        # return result

        pass

        # res = []
        # if not root:
        #     return res
        # stack = [{"status": 1, "node": root}]
        # while stack:
        #     status, node = stack[-1]["status"], stack[-1]["node"]
        #     if status == 1:
        #         res.append(node.val)
        #         stack[-1]["status"] = 2
        #         if node.left:
        #             stack.append({"status": 1, "node": node.left})
        #             continue
        #     if status == 2:
        #         stack[-1]["status"] = 3
        #         if node.right:
        #             stack.append({"status": 1, "node": node.right})
        #             continue
        #     if status == 3:
        #         stack.pop()
        # return res

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
    r1 = s.preorderTraversal(r1)
    r2 = s.preorderTraversal(r2)
    r3 = s.preorderTraversal(r3)
    r4 = s.preorderTraversal(r4)
    r5 = s.preorderTraversal(r5)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
