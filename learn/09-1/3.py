# 面试题 04.01. 节点间通路
#
# 节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。
#
# 示例1:
#  输入：n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
#  输出：true
#
# 示例2:
#  输入：n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], start = 0, target = 4
#  输出 true
#
# 提示：
# 节点数量n在[0, 1e5]范围内。
# 节点编号大于等于 0 小于 n。
# 图中可能存在自环和平行边。


from typing import List


class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        #     self.visited = [False] * n
        #     self.adj = [set() for _ in range(n)]
        #     for item in graph:
        #         self.adj[item[0]].add(item[1])
        #     self.dfs(start, target)
        #     return self.found
        #
        # def __init__(self):
        #     self.visited = None
        #     self.found = False
        #     self.adj = None
        #
        # def dfs(self, cur, target):
        #     if self.found:
        #         return
        #     if cur == target:
        #         self.found = True
        #         return
        #     self.visited[cur] = True
        #     for next_ in self.adj[cur]:
        #         if not self.visited[next_]:
        #             self.dfs(next_, target)

        pass


if __name__ == '__main__':
    n1 = 3
    graph1 = [[0, 1], [0, 2], [1, 2], [1, 2]]
    start1 = 0
    target1 = 2
    n2 = 5
    graph2 = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]]
    start2 = 0
    target2 = 4

    s1 = Solution()
    s2 = Solution()
    r1 = s1.findWhetherExistsPath(n1, graph1, start1, target1)
    r2 = s2.findWhetherExistsPath(n2, graph2, start2, target2)
    print(r1)
    print(r2)
