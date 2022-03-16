# 剑指 Offer 24. 反转链表
#
# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
#
# 示例:
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
# 限制：0 <= 节点个数 <= 5000


from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create(data: List):
    new = ListNode(0)
    tail = new
    for i in data:
        nn = ListNode(i)
        tail.next = nn
        tail = nn
    return new.next


def travel(node: ListNode):
    cur = node
    while cur:
        yield cur.val
        cur = cur.next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # if not head or not head.next:
        #     return head
        # cur = head
        # node = self.reverseList(cur.next)
        # cur.next.next = cur
        # cur.next = None
        # return node

        pass


if __name__ == '__main__':
    head1 = [1, 2, 3, 4, 5]
    h1 = create(head1)

    s = Solution()
    r1 = s.reverseList(h1)
    print([i for i in travel(r1)])
