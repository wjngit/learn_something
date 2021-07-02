# -*- coding:utf-8 -*-
"""
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。
返回同样按升序排列的结果链表。

示例 1：
输入：head = [1,1,2]
输出：[1,2]

示例 2：
输入：head = [1,1,2,3,3]
输出：[1,2,3]
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def create_single_list(data_list):
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

        def travel(_head):
            while _head:
                yield _head.val
                _head = _head.next

        return create_single_list(sorted(list(set([i for i in travel(head)]))))


def create_list(data_list):
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
    head1 = [1, 1, 2]
    head2 = [1, 1, 2, 3, 3]
    head3 = [-1, 0, 0, 0, 0, 3, 3]
    _head1 = create_list(head1)
    _head2 = create_list(head2)
    _head3 = create_list(head3)
    s = Solution()
    ret_h1 = s.deleteDuplicates(_head1)
    ret1 = [i for i in travel_data(ret_h1)]
    ret_h2 = s.deleteDuplicates(_head2)
    ret2 = [i for i in travel_data(ret_h2)]
    ret_h3 = s.deleteDuplicates(_head3)
    ret3 = [i for i in travel_data(ret_h3)]
    print(ret1)
    print(ret2)
    print(ret3)
