# 求二叉树的最小深度。深度：根节点到叶子节点的路径包含的结点个数。

def func(root):
    if not root:
        return 0
    left = func(root.left)
    right = func(root.right)
    if left == 0:
        return right + 1
    if right == 0:
        return left + 1
    return min(left, right) + 1
