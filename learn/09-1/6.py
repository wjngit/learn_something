# 207. 课程表
#
# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，
# 其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
#
# 示例 1：
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：true
# 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
#
# 示例 2：
# 输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
# 输出：false
# 解释：总共有 2 门课程。学习课程 1 之前，你需要先完成课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
#
# 提示：
# 1 <= numCourses <= 105
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# prerequisites[i] 中的所有课程对 互不相同


from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adj = [set() for _ in range(numCourses)]
        # in_degree = [0] * numCourses
        #
        # for i in range(len(prerequisites)):
        #     adj[prerequisites[i][1]].add(prerequisites[i][0])
        #     in_degree[prerequisites[i][0]] += 1
        #
        # zero_in_degree = set()
        # for i in range(len(in_degree)):
        #     if in_degree[i] == 0:
        #         zero_in_degree.add(i)
        #
        # zero_in_degrees_count = 0
        # while zero_in_degree:
        #     course_i = zero_in_degree.pop()
        #     zero_in_degrees_count += 1
        #     for course_j in adj[course_i]:
        #         in_degree[course_j] -= 1
        #         if in_degree[course_j] == 0:
        #             zero_in_degree.add(course_j)
        # return zero_in_degrees_count == numCourses

        pass


if __name__ == '__main__':
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]

    s1 = Solution()
    s2 = Solution()
    r1 = s1.canFinish(numCourses1, prerequisites1)
    r2 = s2.canFinish(numCourses2, prerequisites2)
    print(r1)
    print(r2)
