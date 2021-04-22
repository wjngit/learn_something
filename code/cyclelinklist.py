# 创建节点
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_link = None


# 单向链表
class CycleleLinkList(object):
    def __init__(self):
        self.__head = None

    # 链表是否为空
    def is_empty(self):
        return self.__head == None

    # 链表长度
    def lenght(self):
        cur=self.__head #none
        if self.is_empty():
            return 0
        else:
            count=1
            while cur.next_link!=self.__head:
                count+=1
                cur=cur.next_link
            return count

    # 遍历整个链表
    def travle(self):
        cur = self.__head
        while cur.next_link!=self.__head:
            print(cur.data,end=' ')
            cur = cur.next_link
        # 退出循环后打印最后一个数据
        print(cur.data)
    print('')

    # 链表头部添加元素
    def add(self,data):
        node=Node(data)
        if self.is_empty():
            self.__head=node
            node.next_link=self.__head
        else:
            cur=self.__head
            while cur.next_link != self.__head:
                cur = cur.next_link
            node.next_link=self.__head
            self.__head=node
            cur.next_link=node

    # 链表尾部添加元素
    def append(self,data):
        node = Node(data)
        if self.is_empty():
            self.__head=node
            node.next_link = self.__head
        else:
            cur = self.__head
            while cur.next_link != self.__head:
                cur = cur.next_link
            cur.next_link=node
            node.next_link=self.__head

    # 指定位置添加元素
    def insert(self,index,data):
        count=0
        node = Node(data)
        if index<=0:
            self.add(data)
        elif index>=self.lenght():
            self.append(data)
        else:
            cur=self.__head
            while count<index-1:
                count+=1
                cur=cur.next_link
            node.next_link=cur.next_link
            cur.next_link=node

    # 删除
    def remove(self,data):
        cur=self.__head
        pre=None
        if cur==None:
            return
        while cur.next_link != self.__head:
            if cur.data==data:
                if cur==self.__head:

                    cur_next=self.__head

                    while cur_next.next_link != self.__head:
                        cur_next = cur_next.next_link
                    cur_next.next_link=cur.next_link
                    self.__head = cur.next_link

                else:
                    pre.next_link=cur.next_link
                return
            else:
                pre=cur
                cur=cur.next_link

    # 查询
    def search(self,data):
        cur=self.__head
        if self.is_empty():
            return
        while cur.next_link != self.__head:
            if cur.data==data:

                return True
            else:
                cur=cur.next_link
        # 推出循环之后对最后一个数据判断
        if cur.data==data:
            return True
        return False

if __name__ == '__main__':
    sll=CycleleLinkList()
    sll.add(100)
    sll.add(200)
    sll.add(300)
    sll.add(400)
    sll.add(500)
    sll.append(333)
    sll.insert(1,666)
    sll.insert(-1,888)
    sll.insert(10,999)
    sll.remove(666)
    sll.remove(888)
    print(sll.search(100))
    # print(sll.is_empty())
    print(sll.lenght())
    sll.travle()