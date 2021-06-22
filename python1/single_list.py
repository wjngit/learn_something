# -*- coding: utf-8 -*-

"""
@Time    : 2021/6/22 4:28 下午
@Author  : Garner
@File    : single_list.py
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleList:
    def __init__(self):
        self.__head = None
        self.__next = None

    def a_add(self, data):
        n = Node(data)
        if self.__head is None:
            self.__head = n
        else:
            n.next = self.__head
            self.__head = n

    def b_add(self, data):
        n = Node(data)
        if self.__head is None:
            self.__head = n
            self.__next = n
        else:
            self.__next.next = n
            self.__next = n

    def get_head(self):
        return self.__head

    def travel(self):
        cur = self.__head
        while cur:
            yield cur
            cur = cur.next

    def reverse1(self, head):
        if head is None or head.next is None:
            return head
        current, pre = head, None
        while current is not None:
            pre_next = current.next
            current.next = pre
            pre = current
            current = pre_next
        return pre

    def reverse2(self, head):
        if head is None or head.next is None:
            return head
        head_node = self.reverse2(head.next)
        head.next.next = head
        head.next = None
        return head_node


if __name__ == '__main__':
    s1 = SingleList()
    s2 = SingleList()
    # 可更换
    tmp_list = range(10)
    for tmp in tmp_list:
        s1.a_add(tmp)
        s2.b_add(tmp)

    for i in s1.travel():
        print(i.data, end='\t')
    print('\n')

    for j in s2.travel():
        print(j.data, end='\t')
    print('\n')

    # print(s1.get_head().next.data)
    s1_head = s1.reverse1(s1.get_head())
    while s1_head is not None:
        print(s1_head.data)
        s1_head = s1_head.next

    print('-' * 20)

    s2_head = s2.reverse2(s2.get_head())
    while s2_head is not None:
        print(s2_head.data)
        s2_head = s2_head.next
