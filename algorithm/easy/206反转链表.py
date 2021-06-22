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


if __name__ == '__main__':
    head1 = [1, 2, 3, 4, 5]
    head2 = [1, 2]
    head3 = []


    def create_link_list(data_list):
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


    head1 = create_link_list(head1)
    head2 = create_link_list(head2)
    head3 = create_link_list(head3)
    s = Solution()
    h1 = s.reverseList(head1)
    while h1:
        print(h1.val)
        h1 = h1.next
    print('*' * 20)

    h2 = s.reverseList(head2)
    while h2:
        print(h2.val)
        h2 = h2.next
    print('*' * 20)

    h3 = s.reverseList(head3)
    while h3:
        print(h3.val)
        h3 = h3.next
