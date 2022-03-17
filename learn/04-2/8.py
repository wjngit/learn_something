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
        pass


if __name__ == '__main__':
    # TODO: 用链表实现5个排序算法, 不用递归也实现一下
    pass
