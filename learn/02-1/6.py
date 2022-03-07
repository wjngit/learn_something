# 206. 反转链表
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
#
# 示例1：
# 输入：head = [1, 2, 3, 4, 5]
# 输出：[5, 4, 3, 2, 1]
#
# 示例2：
# 输入：head = [1, 2]
# 输出：[2, 1]
#
# 示例3：
# 输入：head = []
# 输出：[]
#
# 提示：
#     链表中节点的数目范围是[0, 5000]
#     -5000 <= Node.val <= 5000
#
# 进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # new_head = None
        # cur = head
        # while cur:
        #     tmp = cur.next
        #     cur.next = new_head
        #     new_head = cur
        #     cur = tmp
        # return new_head

        pass

        # # 递归
        # if not head or not head.next:
        #     return head
        # cur = head
        # node = self.reverseList(cur.next)
        # cur.next.next = cur
        # cur.next = None
        # return node

        pass


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


if __name__ == '__main__':
    head1 = [1, 2, 3, 4, 5]
    head2 = [1, 2]
    head3 = []

    h1 = create(head1)
    h2 = create(head2)
    h3 = create(head3)

    s = Solution()
    r1 = s.reverseList(h1)
    r2 = s.reverseList(h2)
    r3 = s.reverseList(h3)
    print([i for i in travel(r1)])
    print([i for i in travel(r2)])
    print([i for i in travel(r3)])
