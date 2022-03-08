# 234. 回文链表
#
# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
#
# 示例1：
# 输入：head = [1, 2, 2, 1]
# 输出：true
#
# 示例2：
# 输入：head = [1, 2]
# 输出：false
#
# 提示：
# 链表中节点数目在范围[1, 105] 内 0 <= Node.val <= 9
#
# 进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

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
    def isPalindrome(self, head: ListNode) -> bool:
        #     mid = self.mid(head)
        #     new = self.reverse(mid.next)
        #     while new:
        #         if new.val != head.val:
        #             return False
        #         new = new.next
        #         head = head.next
        #     return True
        #
        # @staticmethod
        # def mid(head):
        #     slow = fast = head
        #     while fast.next and fast.next.next:
        #         slow = slow.next
        #         fast = fast.next.next
        #     return slow
        #
        # def reverse(self, head):
        #     if not head or not head.next:
        #         return head
        #     cur = head
        #     node = self.reverse(cur.next)
        #     cur.next.next = cur
        #     cur.next = None
        #     return node

        pass


if __name__ == '__main__':
    head1 = [1, 2, 2, 1]
    head2 = [1, 2]
    h1 = create(head1)
    h2 = create(head2)
    s = Solution()
    r1 = s.isPalindrome(h1)
    r2 = s.isPalindrome(h2)
    print(r1)
    print(r2)
