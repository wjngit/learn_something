# 给链表重新排序，原始链表：L1, L2, L3…Ln，排成L1, Ln, L2, Ln-1，L3, Ln-2....


def func(root):
    mid = get_mid(root)
    mid_next = mid.next
    mid.next = None
    new = reverse(mid_next)
    # root和new合并
    new_head = None
    tail = new_head
    cur_old = root
    cur_new = new
    while cur_new:
        temp_new = cur_new.next
        temp_old = cur_old.next
        tail.next = cur_old
        tail = cur_old
        tail.next = cur_new
        tail = cur_new
        tail.next = None
        cur_new = temp_new
        cur_old = temp_old
    if cur_old:
        tail.next = cur_old
    return new_head.next


def get_mid(head):
    slow = fast = head
    while fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def reverse(head):
    new = None
    cur = head
    while cur:
        temp = cur.next
        cur.next = new
        new = cur
        cur = temp
    return new
