class Stack():

    # 创建一个新的空栈
    def __init__(self):
        self.data=[]

    # 添加一个新的元素data到栈顶
    def push(self,data):
        self.data.append(data)

    # 弹出栈顶元素
    def pop(self):
        self.data.pop()

    # 返回栈顶元素
    def peek(self):
        return self.data[len(self.data)-1]

    # 判断栈是否为空
    def is_empty(self):
        return len(self.data)==0

    #返回栈的元素个数
    def size(self):
        return len(self.data)