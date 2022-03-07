# 2. 两数相加
#
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头
#
# 示例1：
# 输入：l1 = [2, 4, 3], l2 = [5, 6, 4]
# 输出：[7, 0, 8]
# 解释：342 + 465 = 807.
#
# 示例2：
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#
# 示例3：
# 输入：l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
# 输出：[8, 9, 9, 9, 0, 0, 0, 1]
#
# 提示：
#     每个链表中的节点数在范围[1, 100] 内
#     0 <= Node.val <= 9
#     题目数据保证列表表示的数字不含前导零

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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # new_head = ListNode()
        # tail = new_head
        # carry = 0
        # while l1 or l2:
        #     tmp = 0
        #     if l1:
        #         tmp += l1.val
        #         l1 = l1.next
        #     if l2:
        #         tmp += l2.val
        #         l2 = l2.next
        #     tmp += carry
        #     nn = ListNode(tmp % 10)
        #     tail.next = nn
        #     tail = nn
        #     carry = tmp // 10
        # if carry:
        #     tail.next = ListNode(carry)
        # return new_head.next

        pass


if __name__ == '__main__':
    l11 = [2, 4, 3]
    l12 = [5, 6, 4]
    l21 = [0]
    l22 = [0]
    l31 = [9, 9, 9, 9, 9, 9, 9]
    l32 = [9, 9, 9, 9]

    h11 = create(l11)
    h12 = create(l12)
    h21 = create(l21)
    h22 = create(l22)
    h31 = create(l31)
    h32 = create(l32)

    s = Solution()
    r1 = s.addTwoNumbers(h11, h12)
    r2 = s.addTwoNumbers(h21, h22)
    r3 = s.addTwoNumbers(h31, h32)
    print([i for i in travel(r1)])
    print([i for i in travel(r2)])
    print([i for i in travel(r3)])
