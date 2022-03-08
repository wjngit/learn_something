# 剑指 Offer 22. 链表中倒数第k个节点
#
# 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
# 例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。
#
# 示例：
# 给定一个链表: 1->2->3->4->5, 和 k = 2.
# 返回链表 4->5.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create(data) -> ListNode:
    new_head = ListNode(0)
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
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # fast = head
        # count = 0
        # while fast:
        #     fast = fast.next
        #     count += 1
        #     if count == k:
        #         break
        # if not fast:
        #     return head
        # slow = head
        # while fast:
        #     slow = slow.next
        #     fast = fast.next
        # return slow

        pass


if __name__ == '__main__':
    head1 = [1, 2, 3, 4, 5]
    # head1 = []
    k1 = 2
    h1 = create(head1)

    s = Solution()
    r1 = s.getKthFromEnd(h1, k1)
    print([i for i in travel(r1)])
