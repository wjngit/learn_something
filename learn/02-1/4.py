# 剑指 Offer 25. 合并两个排序的链表
#
# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
#
# 示例1：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
# 限制：
# 0 <= 链表长度 <= 1000

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create(data) -> ListNode:
    new_head = ListNode(None)
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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if not l1 or not l2:
        #     return l1 or l2
        # new_head = ListNode(None)
        # tail = new_head
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         tail.next = l1
        #         tail = l1
        #         l1 = l1.next
        #     else:
        #         tail.next = l2
        #         tail = l2
        #         l2 = l2.next
        # if l1 or l2:
        #     tail.next = l1 or l2
        # return new_head.next

        pass

        # if not l1 or not l2:
        #     return l1 or l2
        # if l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # l2.next = self.mergeTwoLists(l1, l2.next)
        # return l2

        pass


if __name__ == '__main__':
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    h1 = create(l1)
    h2 = create(l2)

    s = Solution()
    r = s.mergeTwoLists(h1, h2)
    print([i for i in travel(r)])
