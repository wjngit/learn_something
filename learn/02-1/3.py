# 83. 删除排序链表中的重复元素
#
# 给定一个已排序的链表的头 head ，删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
#
# 示例1：
# 输入：head = [1, 1, 2]
# 输出：[1, 2]
#
# 示例2：
# 输入：head = [1, 1, 2, 3, 3]
# 输出：[1, 2, 3]
#
# 提示：
# 链表中节点数目在范围[0, 300] 内
# -100 <= Node.val <= 100
# 题目数据保证链表已经按升序 排列

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create(data) -> ListNode:
    new_head = ListNode(val=-1)
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # if not head:
        #     return head
        # cur = head
        # while cur.next:
        #     if cur.val == cur.next.val:
        #         cur.next = cur.next.next
        #     else:
        #         cur = cur.next
        # return head

        pass

        # new_head = ListNode(999)
        # tail = new_head
        # cur = head
        # while cur:
        #     tmp = cur.next
        #     if cur.val != tail.val:
        #         tail.next = cur
        #         tail = cur
        #         tail.next = None
        #     cur = tmp
        # return new_head.next

        pass


if __name__ == '__main__':
    head1 = [1, 1, 2]
    head2 = [1, 1, 2, 3, 3]
    head3 = [0, 0, 0, 0, 0]
    h1 = create(head1)
    h2 = create(head2)
    h3 = create(head3)

    s = Solution()
    r1 = s.deleteDuplicates(h1)
    r2 = s.deleteDuplicates(h2)
    r3 = s.deleteDuplicates(h3)
    print([i for i in travel(r1)])
    print([i for i in travel(r2)])
    print([i for i in travel(r3)])
