# 面试题 03.05. 栈排序
#
# 栈排序。 编写程序，对栈进行排序使最小元素位于栈顶。
# 最多只能使用一个其他的临时栈存放数据，但不得将元素复制到别的数据结构（如数组）中。
# 该栈支持如下操作：push、pop、peek 和 isEmpty。当栈为空时，peek 返回 -1。
#
# 示例1:
#     输入：
#     ["SortedStack", "push", "push", "peek", "pop", "peek"]
#     [[], [1], [2], [], [], []]
#     输出：
#     [null,null,null,1,null,2]
#
# 示例2:
#     输入：
#     ["SortedStack", "pop", "pop", "push", "pop", "isEmpty"]
#     [[], [], [], [1], [], []]
#     输出：
#     [null,null,null,null,null,true]
#
# 说明:
#     栈中的元素数目在[0, 5000]范围内。


# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()


class SortedStack:

    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, val: int) -> None:
        # while self.stack and self.stack[-1] < val:
        #     self.temp.append(self.stack.pop())
        # self.stack.append(val)
        # while self.temp:
        #     self.stack.append(self.temp.pop())

        pass

        self.stack.append(val)

    def pop(self) -> None:
        # if self.stack:
        #     return self.stack.pop()

        pass

        if not self.stack:
            return
        min_val = float('inf')
        while self.stack:
            val = self.stack.pop()
            if val < min_val:
                min_val = val
            self.temp.append(val)
        removed = False
        while self.temp:
            val = self.temp.pop()
            if val != min_val or (val == min_val and removed is True):
                self.stack.append(val)
            else:
                removed = True

    def peek(self) -> int:
        # if self.stack:
        #     return self.stack[-1]
        # return -1

        pass

        if not self.stack:
            return -1
        min_val = float('inf')
        while self.stack:
            val = self.stack.pop()
            if val < min_val:
                min_val = val
            self.temp.append(val)
        while self.temp:
            val = self.temp.pop()
            self.stack.append(val)
        return min_val

    def isEmpty(self) -> bool:
        return not self.stack


if __name__ == '__main__':
    pass
