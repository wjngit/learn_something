# 给定一棵树的根节点, 在已知该树最大深度的情况下, 求节点数最多的那一层并返回具体的层数。
# 如果最后答案有多层, 输出最浅的那一层，树的深度不会超过100000。

def func(root):
    if not root:
        return 0
    q = [root]
    max_ = 0
    cur_l = 0
    n = 1
    while q:
        count = len(q)
        if count > max_:
            max_ = count
            cur_l = n
        for _ in range(count):
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        n += 1
    return cur_l
