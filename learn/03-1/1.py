# 剑指 Offer 09. 用两个栈实现队列
#
# 用两个栈实现一个队列。
# 队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
# 分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )
#
# 示例 1：
# 输入：
# ["CQueue","appendTail","deleteHead","deleteHead"]
# [[],[3],[],[]]
# 输出：[null,null,3,-1]
#
# 示例 2：
# 输入：
# ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
# [[],[],[5],[2],[],[]]
# 输出：[null,-1,null,null,5,2]
#
# 提示：
#     1 <= values <= 10000
#     最多会对 appendTail、deleteHead 进行 10000 次调用


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()


class CQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def appendTail(self, value: int) -> None:
        # while self.s2:
        #     self.s1.append(self.s2.pop())
        # self.s1.append(value)
        # while self.s1:
        #     self.s2.append(self.s1.pop())

        pass

        # self.s1.append(value)

        pass

    def deleteHead(self) -> int:
        # if not self.s2:
        #     return -1
        # return self.s2.pop()

        pass

        # if not self.s2:
        #     while self.s1:
        #         self.s2.append(self.s1.pop())
        # if not self.s2:
        #     return -1
        # return self.s2.pop()

        pass


if __name__ == '__main__':
    obj = CQueue()
    print(obj.deleteHead())
    obj.appendTail(5)
    obj.appendTail(2)
    print(obj.deleteHead())
    print(obj.deleteHead())
