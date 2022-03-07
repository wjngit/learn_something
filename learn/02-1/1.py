# 203. 移除链表元素
#
# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
#
# 示例1：
# 输入：head = [1, 2, 6, 3, 4, 5, 6], val = 6
# 输出：[1, 2, 3, 4, 5]
#
# 示例2：
# 输入：head = [], val = 1
# 输出：[]
#
# 示例3：
# 输入：head = [7, 7, 7, 7], val = 7
# 输出：[]
#
# 提示：
#     列表中的节点数目在范围[0, 104]内
#     1 <= Node.val <= 50
#     0 <= val <= 50


from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # if not head:
        #     return head
        # cur = head
        # while cur.next:
        #     if cur.next.val == val:
        #         cur.next = cur.next.next
        #     else:
        #         cur = cur.next
        #     if head.val == val:
        #         head = head.next
        # return head

        pass

        # cur, pre = head, None
        # while cur:
        #     if cur.val == val:
        #         if cur == head:
        #             head = cur.next
        #         else:
        #             pre.next = cur.next
        #     else:
        #         pre = cur
        #     cur = cur.next
        # return head

        pass

        # new_head = ListNode()
        # tail = new_head
        # cur = head
        # while cur:
        #     tmp = cur.next
        #     if cur.val != val:
        #         tail.next = cur
        #         tail = cur
        #         cur.next = None
        #     cur = tmp
        # return new_head.next

        pass


def create(data: List) -> ListNode:
    new_head = ListNode()
    tail = new_head
    for i in data:
        n = ListNode(val=i)
        tail.next = n
        tail = n
    return new_head.next


def travel(head):
    while head:
        yield head.val
        head = head.next


if __name__ == '__main__':
    head1 = [1, 2, 6, 3, 4, 5, 6]
    val1 = 6
    head2 = []
    val2 = 1
    head3 = [7, 7, 7, 7]
    val3 = 7

    head1 = create(head1)
    head2 = create(head2)
    head3 = create(head3)

    s = Solution()
    r1 = s.removeElements(head1, val1)
    r2 = s.removeElements(head2, val2)
    r3 = s.removeElements(head3, val3)
    print([i for i in travel(r1)])
    print([i for i in travel(r2)])
    print([i for i in travel(r3)])
