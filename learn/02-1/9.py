# 25. K 个一组翻转链表
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
# k 是一个正整数，它的值小于或等于链表的长度。
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
# 进阶：
#     你可以设计一个只使用常数额外空间的算法来解决此问题吗？
#     你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
#
#
# 示例 1：
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
#
# 示例 2：
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
#
# 示例 3：
# 输入：head = [1,2,3,4,5], k = 1
# 输出：[1,2,3,4,5]
#
# 示例 4：
# 输入：head = [1], k = 1
# 输出：[1]
#
# 提示：
#     列表中节点的数量在范围 sz 内
#     1 <= sz <= 5000
#     0 <= Node.val <= 1000
#     1 <= k <= sz

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create(data) -> ListNode:
    new_head = ListNode()
    tail = new_head
    for i in data:
        n = ListNode(i)
        tail.next = n
        tail = n
    return new_head.next


def travel(head):
    while head:
        yield head.val
        head = head.next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #     new_head = ListNode()
        #     new_tail = new_head
        #     cur = head
        #     while cur:
        #         count = 0
        #         cur_cur = cur
        #         while cur_cur:
        #             count += 1
        #             if count == k:
        #                 break
        #             cur_cur = cur_cur.next
        #
        #         if not cur_cur:
        #             new_tail.next = cur
        #             return new_head.next
        #
        #         tmp = cur_cur.next
        #         tmp_head, tmp_tail = self.reverse(cur, cur_cur)
        #         new_tail.next = tmp_head
        #         new_tail = tmp_tail
        #         cur = tmp
        #     return new_head.next
        #
        # @staticmethod
        # def reverse(head, tail):
        #     new = None
        #     cur = head
        #     while cur != tail:
        #         tmp = cur.next
        #         cur.next = new
        #         new = cur
        #         cur = tmp
        #     tail.next = new
        #     return tail, head

        pass


if __name__ == '__main__':
    head1 = [1, 2, 3, 4, 5]
    k1 = 2
    head2 = [1, 2, 3, 4, 5]
    k2 = 3
    head3 = [1, 2, 3, 4, 5]
    k3 = 1
    head4 = [1]
    k4 = 1
    h1 = create(head1)
    h2 = create(head2)
    h3 = create(head3)
    h4 = create(head4)

    s = Solution()
    r1 = s.reverseKGroup(h1, k1)
    r2 = s.reverseKGroup(h2, k2)
    r3 = s.reverseKGroup(h3, k3)
    r4 = s.reverseKGroup(h4, k4)
    print([i for i in travel(r1)])
    print([i for i in travel(r2)])
    print([i for i in travel(r3)])
    print([i for i in travel(r4)])
