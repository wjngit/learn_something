# 创建节点
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_link = None
        self.pre=None


# 双向链表
class DoubleLinkList(object):
    def __init__(self):
        self.__head = None

    # 链表是否为空
    def is_empty(self):
        return self.__head == None

    # 链表长度
    def lenght(self):
        cur=self.__head
        count=0
        while cur!=None:
            count+=1
            cur=cur.next_link
        return count

    # 遍历整个链表
    def travle(self):
        cur = self.__head
        while cur != None:
            print(cur.data,end=' ')
            cur = cur.next_link
    print('')

    # 链表头部添加元素
    def add(self,data):
        node=Node(data)
        if self.is_empty():
            self.__head=node
        else:
            node.next_link=self.__head
            self.__head.pre=node
            self.__head=node

    # 链表尾部添加元素
    def append(self,data):
        node = Node(data)
        if self.is_empty():
            self.__head=node
        else:
            cur = self.__head
            while cur.next_link != None:
                cur = cur.next_link
            cur.next_link=node
            node.pre=cur

    # 指定位置添加元素
    def insert(self,index,data):
        count=0
        node = Node(data)
        if index<=0:
            self.add(data)
        elif index>self.lenght():
            self.append(data)
        else:
            cur=self.__head
            while count<index:
                count+=1
                cur=cur.next_link

            node.next_link=cur
            cur.pre.next_link=node
            node.pre=cur.pre
            cur.pre=node

    # 删除
    def remove(self,data):
        cur=self.__head

        while cur!=None:
            if cur.data==data:
                if cur==self.__head:
                    # self.__head=cur.next_link
                    # if cur.next_link:
                    #     cur.next_link.pre=None
                    if cur.next_link:
                        self.__head=cur.next_link
                        cur.next_link.pre=None
                    else:
                        self.__head=cur.next_link
                else:
                    cur.pre.next_link=cur.next_link

                return
            else:

                cur=cur.next_link

    # 查询
    def search(self,data):
        cur=self.__head

        while cur!=None:
            if cur.data==data:

                return True
            else:
                cur=cur.next_link
        return False

if __name__ == '__main__':
    sll=DoubleLinkList()
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
    sll.remove(999)
    sll.remove(10000)
    print(sll.search(100))
    # print(sll.is_empty())
    print(sll.lenght())
    sll.travle()