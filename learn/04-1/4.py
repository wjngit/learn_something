# 剑指 Offer 06. 从尾到头打印链表
#
# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
#
# 示例 1：
# 输入：head = [1,3,2]
# 输出：[2,3,1]
#
# 限制：0 <= 链表长度 <= 10000


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
    # def __init__(self):
    #     self.result = []

    def reversePrint(self, head: ListNode) -> List[int]:
        #     self.aaa(head)
        #     return self.result
        #
        # def aaa(self, head):
        #     if not head:
        #         return
        #     self.aaa(head.next)
        #     self.result.append(head.val)

        pass


if __name__ == '__main__':
    head1 = [1, 3, 2]
    head2 = []
    h1 = create(head1)
    h2 = create(head2)

    s1 = Solution()
    s2 = Solution()
    r1 = s1.reversePrint(h1)
    r2 = s2.reversePrint(h2)
    print(r1)
    print(r2)
