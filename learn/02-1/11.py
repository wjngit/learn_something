# 19. 删除链表的倒数第 N 个结点
#
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
#
# 示例 1：
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
#
# 示例 2：
# 输入：head = [1], n = 1
# 输出：[]
#
# 示例 3：
# 输入：head = [1,2], n = 1
# 输出：[1]
#
# 提示：
#     链表中结点的数目为 sz
#     1 <= sz <= 30
#     0 <= Node.val <= 100
#     1 <= n <= sz
#
# 进阶：你能尝试使用一趟扫描实现吗？

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # count = 0
        # fast = head
        # while fast:
        #     count += 1
        #     if count == n:
        #         break
        #     fast = fast.next
        # if not fast:
        #     return head
        #
        # slow = head
        # pre = None
        # while fast.next:
        #     pre = slow
        #     slow = slow.next
        #     fast = fast.next
        # if not pre:
        #     head = head.next
        # else:
        #     pre.next = slow.next
        # return head

        pass


if __name__ == '__main__':
    head1 = [1, 2, 3, 4, 5]
    n1 = 2
    head2 = [1]
    n2 = 1
    head3 = [1, 2]
    n3 = 1
    h1 = create(head1)
    h2 = create(head2)
    h3 = create(head3)

    s = Solution()
    r1 = s.removeNthFromEnd(h1, n1)
    r2 = s.removeNthFromEnd(h2, n2)
    r3 = s.removeNthFromEnd(h3, n3)
    print([i for i in travel(r1)])
    print([i for i in travel(r2)])
    print([i for i in travel(r3)])
