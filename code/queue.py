class Queue():

    def __init__(self):
        self.data=[]


    # 往队列中添加一个item元素
    def enqueue(self,data):
        self.data.insert(0,data)

    # 从队列头部删除一个元素
    def dequeue(self):
        self.data.pop()


    # 判断一个队列是否为空
    def is_empty(self):
        return len(self.data) == 0

    # 返回队列的大小
    def size(self):
        return len(self.data)