# 160. 相交链表
#
# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。
# 如果两个链表不存在相交节点，返回 null 。
# 题目数据 保证 整个链式结构中不存在环。
# 注意，函数返回结果后，链表必须 保持其原始结构 。
# 自定义评测：
# 评测系统 的输入如下（你设计的程序 不适用 此输入）：
#     intersectVal - 相交的起始节点的值。如果不存在相交节点，这一值为 0
#     listA - 第一个链表
#     listB - 第二个链表
#     skipA - 在 listA 中（从头节点开始）跳到交叉节点的节点数
#     skipB - 在 listB 中（从头节点开始）跳到交叉节点的节点数
# 评测系统将根据这些输入创建链式数据结构，并将两个头节点 headA 和 headB 传递给你的程序。
# 如果程序能够正确返回相交节点，那么你的解决方案将被 视作正确答案 。
#
# 示例 1：
# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# 输出：Intersected at '8'
# 解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
# 从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,6,1,8,4,5]。
# 在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
#
# 示例 2：
# 输入：intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# 输出：Intersected at '2'
# 解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
# 从各自的表头开始算起，链表 A 为 [1,9,1,2,4]，链表 B 为 [3,2,4]。
# 在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
#
# 示例 3：
# 输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# 输出：null
# 解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
# 由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
# 这两个链表不相交，因此返回 null 。
#
# 提示：
#     listA 中节点数目为 m
#     listB 中节点数目为 n
#     1 <= m, n <= 3 * 104
#     1 <= Node.val <= 105
#     0 <= skipA <= m
#     0 <= skipB <= n
#     如果 listA 和 listB 没有交点，intersectVal 为 0
#     如果 listA 和 listB 有交点，intersectVal == listA[skipA] == listB[skipB]
#
# 进阶：你能否设计一个时间复杂度 O(m + n) 、仅用 O(1) 内存的解决方案？

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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # cur1 = headA
        # temp_set = set()
        # while cur1:
        #     temp_set.add(cur1)
        #     cur1 = cur1.next
        # cur2 = headB
        # while cur2:
        #     if cur2 in temp_set:
        #         return cur2
        #     cur2 = cur2.next
        # return None

        pass


if __name__ == '__main__':
    listA1 = [4, 1, 8, 4, 5]
    listB1 = [5, 6, 1, 8, 4, 5]
    listA2 = [1, 9, 1, 2, 4]
    listB2 = [3, 2, 4]
    listA3 = [2, 6, 4]
    listB3 = [1, 5]
    hA1 = create(listA1)
    hB1 = create(listB1)
    hA2 = create(listA2)
    hB2 = create(listB2)
    hA3 = create(listA3)
    hB3 = create(listB3)

    s = Solution()
    r1 = s.getIntersectionNode(hA1, hB1)
    r2 = s.getIntersectionNode(hA2, hB2)
    r3 = s.getIntersectionNode(hA3, hB3)
    print([i for i in travel(r1)])
    print([i for i in travel(r2)])
    print([i for i in travel(r3)])
