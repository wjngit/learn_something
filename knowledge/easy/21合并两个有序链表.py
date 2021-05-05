# -*- coding:utf-8 -*-
"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：
输入：l1 = [], l2 = []
输出：[]

示例 3：
输入：l1 = [], l2 = [0]
输出：[0]
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # if l1 is None:
        #     return l2
        # elif l2 is None:
        #     return l1
        # elif l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2
        def initList(self, data):
            # 判空
            if len(data) == 0:
                return
            else:
                # 创建头结点
                self.head = ListNode(data[0])
                r = self.head
                p = self.head
                # 逐个为 data 内的数据创建结点, 建立链表
                for i in data[1:]:
                    node = ListNode(i)
                    p.next = node
                    p = p.next
                return r

        def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
            result_list = []
            cur = l1
            while cur is not None:
                result_list.append(cur.val)
                cur = cur.next
            cur = l2
            while cur is not None:
                result_list.append(cur.val)
                cur = cur.next
            sorted_list = sorted(result_list)
            if len(sorted_list) == 0:
                return
            else:
                node = ListNode(sorted_list[0])
                cur = node
                for i in range(1, len(sorted_list)):
                    cur.next = ListNode(sorted_list[i])
                    cur = cur.next
            # 显示结果用
            cur = node
            display = []
            while cur is not None:
                display.append(cur.val)
                cur = cur.next
            return display


if __name__ == '__main__':
    node = ListNode()
    a = node.val
    b = node.next
    print(a)
    print(b)

    l11, l12 = [1, 2, 4], [1, 3, 4]
    l21, l22 = [], []
    l31, l32 = [], [0]
    s = Solution()
    ret1 = s.mergeTwoLists(l11, l12)
    ret2 = s.mergeTwoLists(l21, l22)
    ret3 = s.mergeTwoLists(l31, l32)
    print(ret1)
    print(ret2)
    print(ret3)
