# 剑指 Offer 31. 栈的压入、弹出序列
#
# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
# 假设压入栈的所有数字均不相等。
# 例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，
# 但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。
#
# 示例 1：
# 输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# 输出：true
# 解释：我们可以按以下顺序执行：
#     push(1), push(2), push(3), push(4), pop() -> 4,
#     push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
#
# 示例 2：
# 输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# 输出：false
# 解释：1 不能在 2 之前弹出。
#
# 提示：
#     0 <= pushed.length == popped.length <= 1000
#     0 <= pushed[i], popped[i] < 1000
#     pushed 是 popped 的排列。


from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # stack = []
        # count = 0
        # for data in popped:
        #     if stack and stack[-1] == data:
        #         stack.pop()
        #     else:
        #         while count < len(pushed):
        #             data_in = pushed[count]
        #             if data_in != data:
        #                 stack.append(data_in)
        #                 count += 1
        #             else:
        #                 break
        #         if count == len(pushed):
        #             return False
        #         count += 1
        # return True

        pass


if __name__ == '__main__':
    pushed1 = [1, 2, 3, 4, 5]
    popped1 = [4, 5, 3, 2, 1]
    pushed2 = [1, 2, 3, 4, 5]
    popped2 = [4, 3, 5, 1, 2]
    s = Solution()
    r1 = s.validateStackSequences(pushed1, popped1)
    r2 = s.validateStackSequences(pushed2, popped2)
    print(r1)
    print(r2)
