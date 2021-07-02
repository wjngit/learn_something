# -*- coding:utf-8 -*-
"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

示例 1：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

示例 2：
输入：head = [1,2]
输出：[2,1]

示例 3：
输入：head = []
输出：[]
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head
        while curr is not None:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        return prev


def create_single_link_list(data_list):
    _head, _next = None, None
    for data in data_list:
        n = ListNode(data)
        if _head is None:
            _next = n
            _head = n
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
    _head1 = [1, 2, 3, 4, 5]
    _head2 = [1, 2]
    _head3 = []
    head1 = create_single_link_list(_head1)
    head2 = create_single_link_list(_head2)
    head3 = create_single_link_list(_head3)
    s = Solution()
    h1 = s.reverseList(head1)
    ret1 = [i for i in travel(h1)]
    print(ret1)
    h2 = s.reverseList(head2)
    ret2 = [i for i in travel(h2)]
    print(ret2)
    h3 = s.reverseList(head3)
    ret3 = [i for i in travel(h3)]
    print(ret3)
