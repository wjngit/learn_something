# -*- coding:utf-8 -*-
"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例 2：
输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def travel(_head):
            while _head:
                yield _head.val
                _head = _head.next

        def create_link_list(sum_num):
            _head, _next = None, None
            for data in str(sum_num):
                n = ListNode(int(data))
                if _head is None:
                    _head = n
                else:
                    n.next = _head
                    _head = n
            return _head

        def get_sum_data(ll):
            sum_ = 0
            for index, data in enumerate([i for i in travel(ll)]):
                sum_ += 10 ** index * data
            return sum_

        # l1只有一个0
        if l1.val == 0 and l1.next is None:
            if l2.val == 0 and l2.next is None:
                return l1
            return create_link_list(get_sum_data(l2))
        # l2只有一个0
        if l2.val == 0 and l2.next is None:
            if l1.val == 0 and l1.next is None:
                return l1
            return create_link_list(get_sum_data(l1))
        return create_link_list(get_sum_data(l1) + get_sum_data(l2))


def create_single_link_list(data_list):
    _head, _next = None, None
    for data in data_list:
        n = ListNode(data)
        if _head is None:
            _head = n
            _next = n
        else:
            _next.next = n
            _next = n
    return _head


def travel_data(_head):
    while _head:
        yield _head.val
        _head = _head.next


if __name__ == '__main__':
    l11, l12 = [2, 4, 3], [5, 6, 4]
    l21, l22 = [0], [0]
    l31, l32 = [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]
    _head11, _head12 = create_single_link_list(l11), create_single_link_list(l12)
    _head21, _head22 = create_single_link_list(l21), create_single_link_list(l22)
    _head31, _head32 = create_single_link_list(l31), create_single_link_list(l32)
    # ret11, ret12 = [i for i in travel_data(_head11)], [i for i in travel_data(_head12)]
    # ret21, ret22 = [i for i in travel_data(_head21)], [i for i in travel_data(_head22)]
    # ret31, ret32 = [i for i in travel_data(_head31)], [i for i in travel_data(_head32)]
    # print(f'第 1 组: {ret11} , {ret12}')
    # print(f'第 2 组: {ret21} , {ret22}')
    # print(f'第 3 组: {ret31} , {ret32}')
    s = Solution()
    ret_h1 = s.addTwoNumbers(_head11, _head12)
    ret1 = [i for i in travel_data(ret_h1)]
    ret_h2 = s.addTwoNumbers(_head21, _head22)
    ret2 = [i for i in travel_data(ret_h2)]
    ret_h3 = s.addTwoNumbers(_head31, _head32)
    ret3 = [i for i in travel_data(ret_h3)]
    print(ret1)
    print(ret2)
    print(ret3)
