# 面试题 02.01. 移除重复节点
#
# 编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。
#
# 示例1:
#  输入：[1, 2, 3, 3, 2, 1]
#  输出：[1, 2, 3]
#
# 示例2:
#
#  输入：[1, 1, 1, 1, 2]
#  输出：[1, 2]
#
# 提示：
#     链表长度在[0, 20000]范围内。
#     链表元素在[0, 20000]范围内。
#
# 进阶：如果不得使用临时缓冲区，该怎么解决？


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create(data) -> ListNode:
    new_head = ListNode(999)
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
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        # temp = set()
        # cur = head
        # new = ListNode(999)
        # tail = new
        # while cur:
        #     tmp = cur.next
        #     if cur.val not in temp:
        #         temp.add(cur.val)
        #         tail.next = cur
        #         tail = cur
        #         tail.next = None
        #     cur = tmp
        # return new.next

        pass

        # cur = head
        # while cur:
        #     p = cur
        #     while p.next:
        #         if p.next.val == cur.val:
        #             p.next = p.next.next
        #         else:
        #             p = p.next
        #     cur = cur.next
        # return head

        pass


if __name__ == '__main__':
    list1 = [1, 2, 3, 3, 2, 1]
    list2 = [1, 1, 1, 1, 2]
    h1 = create(list1)
    h2 = create(list2)

    s = Solution()
    r1 = s.removeDuplicateNodes(h1)
    r2 = s.removeDuplicateNodes(h2)
    print([i for i in travel(r1)])
    print([i for i in travel(r2)])
