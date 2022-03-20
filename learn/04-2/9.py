# 148. 排序链表
#
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
#
# 示例 1：
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#
# 示例 2：
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
#
# 示例 3：
# 输入：head = []
# 输出：[]
#
# 提示：
# 链表中节点的数目在范围 [0, 5 * 104] 内
# -105 <= Node.val <= 105
#
# 进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？


from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create(data):
    new = ListNode(999)
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
    stack = []

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #     # todo: 递归-实现归并排序
        #     if not head or not head.next:
        #         return head
        #     mid_node = self.find_mid_node(head)
        #     next_node = mid_node.next
        #     mid_node.next = None
        #     left_head = self.sortList(head)
        #     right_head = self.sortList(next_node)
        #     return self.merge_list(left_head, right_head)
        #
        # def merge_list(self, left_head, right_head):
        #     new = ListNode(999)
        #     tail = new
        #     cur_l, cur_r = left_head, right_head
        #     while cur_l and cur_r:
        #         if cur_l.val <= cur_r.val:
        #             tail.next = cur_l
        #             tail = cur_l
        #             cur_l = cur_l.next
        #         else:
        #             tail.next = cur_r
        #             tail = cur_r
        #             cur_r = cur_r.next
        #     if cur_l:
        #         tail.next = cur_l
        #     if cur_r:
        #         tail.next = cur_r
        #     return new.next
        #
        # @staticmethod
        # def find_mid_node(head):
        #     slow = fast = head
        #     while fast.next and fast.next.next:
        #         slow = slow.next
        #         fast = fast.next.next
        #     return slow

        pass

        #     # todo: 非递归-实现归并排序
        #     n = self.get_len(head)
        #     step = 1
        #     while step < n:
        #         new = ListNode(999)
        #         tail = new
        #         left = head
        #         while left:
        #             # [left, mid]
        #             mid = left
        #             count = 1
        #             while mid and count < step:
        #                 mid = mid.next
        #                 count += 1
        #             if not mid or not mid.next:
        #                 tail.next = left
        #                 break
        #             # [mid+1, right]
        #             right = mid.next
        #             count = 1
        #             while right and count < step:
        #                 right = right.next
        #                 count += 1
        #             temp = None
        #             if right:
        #                 temp = right.next
        #             # 合并
        #             head_tail = self.merge(left, mid, right)
        #             tail.next = head_tail[0]
        #             tail = head_tail[1]
        #             left = temp
        #         head = new.next
        #         step *= 2
        #     return head
        #
        # def merge(self, left, mid, right):
        #     new = ListNode(999)
        #     tail = new
        #     cur_l = left
        #     cur_r = mid.next
        #     mid.next = None
        #     if right:
        #         right.next = None
        #     while cur_l and cur_r:
        #         if cur_l.val <= cur_r.val:
        #             tail.next = cur_l
        #             tail = cur_l
        #             cur_l = cur_l.next
        #         else:
        #             tail.next = cur_r
        #             tail = cur_r
        #             cur_r = cur_r.next
        #     if cur_l:
        #         tail.next = cur_l
        #         tail = mid
        #     if cur_r:
        #         tail.next = cur_r
        #         tail = right
        #     return new.next, tail
        #
        # @staticmethod
        # def get_len(head):
        #     count = 0
        #     cur = head
        #     while cur:
        #         count += 1
        #         cur = cur.next
        #     return count

        pass

        #     # todo: 递归-实现快速排序
        #     if not head or not head.next:
        #         return head
        #     end = self.get_end(head)
        #     self.quick_sort(head, end)
        #     return head
        #
        # def quick_sort(self, start, end):
        #     if start is None or start == end or start.next is None:
        #         return
        #
        #     pivot = start.val
        #     pre = start
        #     i, j = start.next, start.next
        #     while j != end.next:
        #         if j.val < pivot:
        #             self.swap(i, j)
        #             pre = i
        #             i = i.next
        #         j = j.next
        #     self.swap(start, pre)
        #
        #     self.quick_sort(start, pre)
        #     self.quick_sort(i, end)
        #
        # @staticmethod
        # def swap(a, b):
        #     temp = a.val
        #     a.val, b.val = b.val, temp
        #
        # @staticmethod
        # def get_end(head):
        #     cur = head
        #     while cur.next:
        #         cur = cur.next
        #     return cur

        pass

        #     # todo: 非递归-实现快速排序
        #     if not head or not head.next:
        #         return head
        #     end = self.get_end(head)
        #     self.quick_sort_r(head, end)
        #     return head
        #
        # def quick_sort_r(self, start, end):
        #     self.stack.append(start)
        #     self.stack.append(end)
        #     while self.stack:
        #         end = self.stack.pop()
        #         start = self.stack.pop()
        #
        #         pivot = start.val
        #         pre = start
        #         i, j = start.next, start.next
        #         while j != end.next:
        #             if j.val < pivot:
        #                 self.swap(i, j)
        #                 pre = i
        #                 i = i.next
        #             j = j.next
        #         self.swap(start, pre)
        #
        #         if start and start != pre:
        #             self.stack.append(start)
        #             self.stack.append(pre)
        #         if i and i != end:
        #             self.stack.append(i)
        #             self.stack.append(end)
        #
        # @staticmethod
        # def swap(a, b):
        #     temp = a.val
        #     a.val, b.val = b.val, temp
        #
        # @staticmethod
        # def get_end(head):
        #     end = head
        #     while end.next:
        #         end = end.next
        #     return end

        pass


if __name__ == '__main__':
    head1 = [2, 1, 5, 4, 3, 7, 6]
    head2 = [-1, 5, 3, 4, 0]
    head3 = []
    h1 = create(head1)
    h2 = create(head2)
    h3 = create(head3)
    s = Solution()
    r1 = s.sortList(h1)
    r2 = s.sortList(h2)
    r3 = s.sortList(h3)
    print([i for i in travel(r1)])
    print([i for i in travel(r2)])
    print([i for i in travel(r3)])
