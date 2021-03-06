# 752. 打开转盘锁
#
# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。
# 每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
# 字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。
#
# 示例 1:
# 输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# 输出：6
# 解释：
# 可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
# 注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
# 因为当拨动到 "0102" 时这个锁就会被锁定。
#
# 示例 2:
# 输入: deadends = ["8888"], target = "0009"
# 输出：1
# 解释：把最后一位反向旋转一次即可 "0000" -> "0009"。
#
# 示例 3:
# 输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
# 输出：-1
# 解释：无法旋转到目标数字且不被锁定。
#
# 提示：
# 1 <= deadends.length <= 500
# deadends[i].length == 4
# target.length == 4
# target 不在 deadends 之中
# target 和 deadends[i] 仅由若干位数字组成


from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #     dead_set = set()
        #     for data in deadends:
        #         dead_set.add(data)
        #     if "0000" in dead_set:
        #         return -1
        #     visited = {"0000"}
        #     q = ["0000"]
        #     depth = 0
        #     while q:
        #         size = len(q)
        #         k = 0
        #         while k < size:
        #             node = q.pop(0)
        #             k += 1
        #             if node == target:
        #                 return depth
        #             new_nodes = self.get_new_node(node)
        #             for new_node in new_nodes:
        #                 if new_node in visited or new_node in dead_set:
        #                     continue
        #                 q.append(new_node)
        #                 visited.add(new_node)
        #         depth += 1
        #     return -1
        #
        # @staticmethod
        # def get_new_node(node):
        #     new_nodes = []
        #     change = [-1, 1]
        #     for i in range(4):
        #         for j in range(2):
        #             new_node = [""] * 4
        #             for k in range(i):
        #                 new_node[k] = node[k]
        #             for m in range(i + 1, 4):
        #                 new_node[m] = node[m]
        #             new_node[i] = str((int(node[i]) + change[j] + 10) % 10)
        #             new_nodes.append("".join(new_node))
        #     return new_nodes

        pass


if __name__ == '__main__':
    deadends1 = ["0201", "0101", "0102", "1212", "2002"]
    target1 = "0202"
    deadends2 = ["8888"]
    target2 = "0009"
    deadends3 = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    target3 = "8888"

    s1 = Solution()
    s2 = Solution()
    s3 = Solution()
    r1 = s1.openLock(deadends1, target1)
    r2 = s2.openLock(deadends2, target2)
    r3 = s3.openLock(deadends3, target3)
    print(r1)
    print(r2)
    print(r3)
