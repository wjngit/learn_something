# 剑指 Offer 25. 合并两个排序的链表
#
# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
#
# 示例1：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
# 限制：0 <= 链表长度 <= 1000


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create(data):
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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if not l1 or not l2:
        #     return l1 or l2
        # if l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # l2.next = self.mergeTwoLists(l1, l2.next)
        # return l2

        pass


if __name__ == '__main__':
    head11 = [1, 2, 4]
    head12 = [1, 3, 4]
    h11 = create(head11)
    h12 = create(head12)

    s = Solution()
    r1 = s.mergeTwoLists(h11, h12)
    print([i for i in travel(r1)])
