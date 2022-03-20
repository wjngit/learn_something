# 147. 对链表进行插入排序
#
# 给定单个链表的头 head ，使用 插入排序 对链表进行排序，并返回 排序后链表的头 。
# 插入排序 算法的步骤:
#     插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
#     每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
#     重复直到所有输入数据插入完为止。
#
# 示例 1：
# 输入: head = [4,2,1,3]
# 输出: [1,2,3,4]
#
# 示例 2：
# 输入: head = [-1,5,3,4,0]
# 输出: [-1,0,3,4,5]
#
# 提示：
#     列表中的节点数在 [1, 5000]范围内
#     -5000 <= Node.val <= 5000


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
    def insertionSortList(self, head: ListNode) -> ListNode:
        # # todo: 冒泡排序
        # p = head
        # count = 0
        # while p:
        #     count += 1
        #     p = p.next
        # for i in range(count - 1):
        #     cur = head
        #     nxt = cur.next
        #     pre = None
        #     while nxt:
        #         if cur.val > nxt.val:
        #             if pre is None:
        #                 pre = cur.next
        #                 nxt = nxt.next
        #                 pre.next = cur
        #                 cur.next = nxt
        #                 head = pre
        #             else:
        #                 temp = nxt
        #                 nxt = nxt.next
        #                 pre.next = cur.next
        #                 pre = temp
        #                 temp.next = cur
        #                 cur.next = nxt
        #         else:
        #             pre = cur
        #             cur = nxt
        #             nxt = nxt.next
        #     i += 1
        # return head

        pass

        # # todo: 插入排序
        # if not head:
        #     return head
        # new = ListNode()
        # cur = head
        # while cur:
        #     temp = cur.next
        #     p = new
        #     while p.next and p.next.val <= cur.val:
        #         p = p.next
        #     cur.next = p.next
        #     p.next = cur
        #     cur = temp
        # return new.next

        pass

        # # todo: 选择排序
        # cur = head
        # while cur:
        #     min_node = cur
        #     p = cur.next
        #     while p:
        #         if min_node.val > p.val:
        #             min_node = p
        #         p = p.next
        #     cur_val = cur.val
        #     cur.val = min_node.val
        #     min_node.val = cur_val
        #     cur = cur.next
        # return head

        pass


if __name__ == '__main__':
    head1 = [4, 2, 1, 3]
    head2 = [-1, 5, 3, 4, 0]
    h1 = create(head1)
    h2 = create(head2)
    s = Solution()
    r1 = s.insertionSortList(h1)
    r2 = s.insertionSortList(h2)
    print([i for i in travel(r1)])
    print([i for i in travel(r2)])
