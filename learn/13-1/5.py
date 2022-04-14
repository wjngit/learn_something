# 给定一棵树，返回指定节点到根节点路径。
res_path = []


def func(root, p):
    dfs(root, p, [])
    return res_path


def dfs(cur, p, path):
    if res_path:
        return
    if cur is None:
        return
    path.append(cur.val)
    if cur == p:
        res_path.extend(path[:])
        return
    dfs(cur.left, p, path)
    dfs(cur.right, p, path)
    path.pop()
