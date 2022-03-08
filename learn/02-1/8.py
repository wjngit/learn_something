# 328. 奇偶链表
#
# 给定单链表的头节点 head ，将所有索引为奇数的节点和索引为偶数的节点分别组合在一起，然后返回重新排序的列表。
# 第一个节点的索引被认为是 奇数 ， 第二个节点的索引为 偶数 ，以此类推。
# 请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。
# 你必须在 O(1) 的额外空间复杂度和 O(n) 的时间复杂度下解决这个问题。
#
# 示例 1:
# 输入: head = [1,2,3,4,5]
# 输出: [1,3,5,2,4]
#
# 示例 2:
# 输入: head = [2,1,3,5,6,4,7]
# 输出: [2,3,6,7,1,5,4]
#
# 提示:
#     n ==  链表中的节点数
#     0 <= n <= 104
#     -106 <= Node.val <= 106

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
    def oddEvenList(self, head: ListNode) -> ListNode:
        # count = 1
        # odd_head = ListNode()
        # odd_tail = odd_head
        # even_head = ListNode()
        # even_tail = even_head
        # cur = head
        # while cur:
        #     num = count % 2
        #     tmp = cur.next
        #     if num == 1:
        #         odd_tail.next = cur
        #         odd_tail = cur
        #         odd_tail.next = None
        #     else:
        #         even_tail.next = cur
        #         even_tail = cur
        #         even_tail.next = None
        #     cur = tmp
        #     count += 1
        # odd_tail.next = even_head.next
        # return odd_head.next

        pass


if __name__ == '__main__':
    head1 = [1, 2, 3, 4, 5]
    head2 = [2, 1, 3, 5, 6, 4, 7]
    h1 = create(head1)
    h2 = create(head2)
    s = Solution()
    r1 = s.oddEvenList(h1)
    r2 = s.oddEvenList(h2)
    print([i for i in travel(r1)])
    print([i for i in travel(r2)])
