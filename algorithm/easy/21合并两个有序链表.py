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
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


def create_single_link_list(data_list):
    _head, _next = None, None
    for data in data_list:
        n = ListNode(val=data)
        if _head is None:
            _head = n
            _next = n
        else:
            _next.next = n
            _next = n
    return _head


def travel(_head):
    if _head is None:
        return
    while _head:
        yield _head.val
        _head = _head.next


if __name__ == '__main__':
    l11, l12 = [1, 2, 4], [1, 3, 4]
    l11_h = create_single_link_list(l11)
    l12_h = create_single_link_list(l12)
    l21, l22 = [], []
    l21_h = create_single_link_list(l21)
    l22_h = create_single_link_list(l22)
    l31, l32 = [], [0]
    l31_h = create_single_link_list(l31)
    l32_h = create_single_link_list(l32)
    s = Solution()
    ret1 = s.mergeTwoLists(l11_h, l12_h)
    ret2 = s.mergeTwoLists(l21_h, l22_h)
    ret3 = s.mergeTwoLists(l31_h, l32_h)
    merge1 = [i for i in travel(ret1)]
    merge2 = [i for i in travel(ret2)]
    merge3 = [i for i in travel(ret3)]
    print(merge1)
    print(merge2)
    print(merge3)
