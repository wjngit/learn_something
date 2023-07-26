# 225. 用队列实现栈
#
# 请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。
# 实现 MyStack 类：
#     void push(int x) 将元素 x 压入栈顶。
#     int pop() 移除并返回栈顶元素。
#     int top() 返回栈顶元素。
#     boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。
# 注意：
#     你只能使用队列的基本操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。
#     你所使用的语言也许不支持队列。你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
#
# 示例：
# 输入：
#     ["MyStack", "push", "push", "top", "pop", "empty"]
#     [[], [1], [2], [], [], []]
# 输出：
#     [null, null, null, 2, 2, false]
#
# 解释：
#     MyStack myStack = new MyStack();
#     myStack.push(1);
#     myStack.push(2);
#     myStack.top(); // 返回 2
#     myStack.pop(); // 返回 2
#     myStack.empty(); // 返回 False
#
# 提示：
#     1 <= x <= 9
#     最多调用100 次 push、pop、top 和 empty
#     每次调用 pop 和 top 都保证栈不为空
#
# 进阶：你能否仅用一个队列来实现栈。


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

import collections


class MyStack:
    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()
        self.q = collections.deque()

    def push(self, x: int) -> None:
        # self.q1.append(x)
        pass
        n = len(self.q)
        self.q.append(x)
        for i in range(n):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # if not self.q1:
        #     return -1
        # for i in range(len(self.q1) - 1):
        #     self.q2.append(self.q1.popleft())
        # result = self.q1.popleft()
        # for i in range(len(self.q2)):
        #     self.q1.append(self.q2.popleft())
        # return result
        pass
        if not self.q:
            return -1
        return self.q.popleft()

    def top(self) -> int:
        # if not self.q1:
        #     return -1
        # for i in range(len(self.q1) - 1):
        #     self.q2.append(self.q1.popleft())
        # result = self.q1.popleft()
        # for i in range(len(self.q2)):
        #     self.q1.append(self.q2.popleft())
        # self.q1.append(result)
        # return result
        pass
        if not self.q:
            return -1
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q1) == 0


if __name__ == '__main__':
    s = MyStack()
    print(s.top())
    print(s.pop())
    print(s.push(1))
    print(s.push(2))
    print(s.push(3))
    print(s.push(4))
    print(s.top())  # 返回 2
    print(s.pop())  # 返回 2
    print(s.empty())  # 返回 False
