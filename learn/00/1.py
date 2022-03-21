# # 斐波那契-普通
# def fib1(n):
#     if n <= 2:
#         return 1
#     i, j = 1, 1
#     k = 3
#     temp = 0
#     while k <= n:
#         temp = i + j
#         i, j = j, temp
#         k += 1
#     return temp
#
#
# # 斐波那契-递归
# def fib2(n):
#     if n <= 2:
#         return 1
#     return fib2(n - 2) + fib2(n - 1)
#
#
# if __name__ == '__main__':
#     for i in range(1, 11):
#         print(fib1(i), end=",")
#     print("")
#     for i in range(1, 11):
#         print(fib2(i), end=",")
#     print("")
#     print("-" * 50)

pass

# # 求和-普通
# def sum1(n):
#     temp = 0
#     for i in range(n + 1):
#         temp += i
#     return temp
#
#
# # 求和-递归
# def sum2(n):
#     if n == 1:
#         return 1
#     return n + sum2(n - 1)
#
#
# if __name__ == '__main__':
#     print(sum1(100))
#     print(sum2(100))
#     print("-" * 50)

pass


class NodeData:
    def __init__(self, data=999):
        self.data = data
        self.next = None


def create(data):
    new_head = NodeData()
    tail = new_head
    for i in data:
        nn = NodeData(i)
        tail.next = nn
        tail = nn
    return new_head.next


def travel(head):
    cur = head
    while cur:
        yield cur.data
        cur = cur.next


pass

# # 冒泡排序
# def bubble_sort(data):
#     n = len(data)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if data[j] > data[j + 1]:
#                 data[j + 1], data[j] = data[j], data[j + 1]
#
#
# def bubble_sort_link(head):
#     if not head or not head.next:
#         return head
#     new_head = NodeData()
#     pre = new_head
#     pre.next = head
#     cur = pre.next
#     end = None
#     while cur != end:
#         while cur.next != end:
#             if cur.data > cur.next.data:
#                 temp = cur.next
#                 cur.next = cur.next.next
#                 temp.next = cur
#                 pre.next = temp
#                 pre = temp
#             else:
#                 pre = cur
#                 cur = cur.next
#         end = cur
#         pre = new_head
#         cur = pre.next
#     return new_head.next
#
#
# if __name__ == '__main__':
#     a_list = [17, 20, 26, 31, 44, 54, 55, 77, 77, 77, 93]
#     print(a_list, "*" * 5)
#     a1_list = [54, 26, 77, 93, 17, 77, 31, 44, 55, 20, 77]
#     bubble_sort(a1_list)
#     print(a1_list)
#
#     a2_list = [54, 26, 77, 93, 17, 77, 31, 44, 55, 20, 77]
#     head = create(a2_list)
#     h1 = bubble_sort_link(head)
#     print([i for i in travel(h1)], "^" * 10)

pass

# # 插入排序
# def insert_sort(data):
#     n = len(data)
#     for i in range(1, n):
#         for j in range(i, 0, -1):
#             if data[j] < data[j - 1]:
#                 data[j - 1], data[j] = data[j], data[j - 1]
#             else:
#                 break
#
#
# def insert_sort_link(head):
#     if not head or not head.next:
#         return head
#     new_head = NodeData()
#     cur = head
#     while cur:
#         temp = cur.next
#         pre = new_head
#         while pre.next and pre.next.data < cur.data:
#             pre = pre.next
#         cur.next = pre.next
#         pre.next = cur
#         cur = temp
#     return new_head.next
#
#
# if __name__ == '__main__':
#     a_list = [17, 20, 26, 31, 44, 54, 55, 77, 77, 77, 93]
#     print(a_list, "*" * 5)
#     a1_list = [54, 26, 77, 93, 17, 77, 31, 44, 55, 20, 77]
#     insert_sort(a1_list)
#     print(a1_list)
#
#     a2_list = [54, 26, 77, 93, 17, 77, 31, 44, 55, 20, 77]
#     head = create(a2_list)
#     h1 = insert_sort_link(head)
#     print([i for i in travel(h1)], "^" * 10)

pass

# # 选择排序
# def select_sort(data):
#     n = len(data)
#     for i in range(n - 1):
#         min_ = i
#         for j in range(i, n - 1):
#             if data[min_] > data[j + 1]:
#                 min_ = j + 1
#         if min_ != i:
#             data[min_], data[i] = data[i], data[min_]
#
#
# def select_sort_link(head):
#     if not head or not head.next:
#         return head
#     cur = head
#     while cur:
#         min_node = cur
#         p = cur.next
#         while p:
#             if min_node.data > p.data:
#                 min_node = p
#             p = p.next
#         cur_val = cur.data
#         cur.data = min_node.data
#         min_node.data = cur_val
#         cur = cur.next
#     return head
#
#
# if __name__ == '__main__':
#     a_list = [17, 20, 26, 31, 44, 54, 55, 77, 77, 77, 93]
#     print(a_list, "*" * 5)
#     a1_list = [54, 26, 77, 93, 17, 77, 31, 44, 55, 20, 77]
#     select_sort(a1_list)
#     print(a1_list)
#
#     a2_list = [54, 26, 77, 93, 17, 77, 31, 44, 55, 20, 77]
#     head = create(a2_list)
#     h1 = select_sort_link(head)
#     print([i for i in travel(h1)], "^" * 10)

pass

# # 归并排序
# def merge_sort(data):
#     n = len(data)
#     if n == 1:
#         return data
#     mid = n // 2
#     l_data, r_data = data[:mid], data[mid:]
#     l_sort, r_sort = merge_sort(l_data), merge_sort(r_data)
#     l_index, r_index, temp = 0, 0, []
#     while l_index < len(l_sort) and r_index < len(r_sort):
#         if l_sort[l_index] <= r_sort[r_index]:
#             temp.append(l_sort[l_index])
#             l_index += 1
#         else:
#             temp.append(r_sort[r_index])
#             r_index += 1
#     temp.extend(l_sort[l_index:])
#     temp.extend(r_sort[r_index:])
#     return temp
#
#
# class MergeSort:
#     def merge_sort1(self, data):
#         """递归"""
#         self.merge_sort1_r(data, 0, len(data) - 1)
#
#     def merge_sort1_r(self, data, start, end):
#         if start >= end:
#             return
#         mid = start + (end - start) // 2
#         self.merge_sort_r(data, start, mid)
#         self.merge_sort_r(data, mid + 1, end)
#         self.merge_func(data, start, mid, end)
#
#     @staticmethod
#     def merge_func(data, start, mid, end):
#         i, j = start, mid + 1
#         temp = []
#         while i <= mid and j <= end:
#             if data[i] <= data[j]:
#                 temp.append(data[i])
#                 i += 1
#             else:
#                 temp.append(data[j])
#                 j += 1
#         while i <= mid:
#             temp.append(data[i])
#             i += 1
#         while j <= end:
#             temp.append(data[j])
#             j += 1
#         data[start:end + 1] = temp
#
#     def merge_sort2(self, data):
#         """非递归"""
#         n = len(data)
#         step = 1
#         while step < n:
#             i = 0
#             while i + step < n:
#                 low = i
#                 mid = i + step - 1
#                 high = i + step * 2 - 1
#                 if high > n - 1:
#                     high = n - 1
#                 self.merge_func(data, low, mid, high)
#                 i += step * 2
#             step *= 2
#
#
# class MergeSortLink:
#     def merge_sort1(self, head):
#         """递归"""
#         if not head or not head.next:
#             return head
#         mid_node = self.find_mid_node(head)
#         next_node = mid_node.next
#         mid_node.next = None
#         left_head = self.merge_sort1(head)
#         right_head = self.merge_sort1(next_node)
#         return self.merge_func1(left_head, right_head)
#
#     @staticmethod
#     def merge_func1(left_head, right_head):
#         new_head = NodeData()
#         tail = new_head
#         cur_l, cur_r = left_head, right_head
#         while cur_l and cur_r:
#             if cur_l.data <= cur_r.data:
#                 tail.next = cur_l
#                 tail = cur_l
#                 cur_l = cur_l.next
#             else:
#                 tail.next = cur_r
#                 tail = cur_r
#                 cur_r = cur_r.next
#         if cur_l:
#             tail.next = cur_l
#         if cur_r:
#             tail.next = cur_r
#         return new_head.next
#
#     @staticmethod
#     def find_mid_node(head):
#         slow = fast = head
#         while fast.next and fast.next.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow
#
#     def merge_sort2(self, head):
#         """非递归"""
#         if not head or not head.next:
#             return head
#         n = self.get_len(head)
#         step = 1
#         while step < n:
#             new_head = NodeData()
#             tail = new_head
#             left = head
#             while left:
#                 mid = left
#                 count = 1
#                 while mid and count < step:
#                     mid = mid.next
#                     count += 1
#
#                 if not mid or not mid.next:
#                     tail.next = left
#                     break
#
#                 right = mid.next
#                 count = 1
#                 while right and count < step:
#                     right = right.next
#                     count += 1
#
#                 temp = None
#                 if right:
#                     temp = right.next
#
#                 head_tail = self.merge_func2(left, mid, right)
#                 tail.next = head_tail[0]
#                 tail = head_tail[1]
#
#                 left = temp
#             head = new_head.next
#             step *= 2
#         return head
#
#     @staticmethod
#     def merge_func2(left, mid, right):
#         new_head = NodeData()
#         tail = new_head
#         cur_l, cur_r = left, mid.next
#         mid.next = None
#         if right:
#             right.next = None
#         while cur_l and cur_r:
#             if cur_l.data <= cur_r.data:
#                 tail.next = cur_l
#                 tail = cur_l
#                 cur_l = cur_l.next
#             else:
#                 tail.next = cur_r
#                 tail = cur_r
#                 cur_r = cur_r.next
#         if cur_l:
#             tail.next = cur_l
#             tail = mid
#         if cur_r:
#             tail.next = cur_r
#             tail = right
#         return new_head.next, tail
#
#     @staticmethod
#     def get_len(head):
#         cur = head
#         n = 0
#         while cur:
#             n += 1
#             cur = cur.next
#         return n
#
#
# if __name__ == '__main__':
#     a_list = [17, 20, 26, 31, 44, 54, 55, 77, 77, 77, 93]
#     print(a_list, "*" * 5)
#     a11_list = [54, 26, 77, 93, 17, 77, 31, 44, 55, 20, 77]
#     a12_list = [54, 26, 77, 93, 17, 77, 31, 44, 55, 20, 77]
#     merge_sort = MergeSort()
#     merge_sort.merge_sort1(a11_list)
#     merge_sort.merge_sort2(a12_list)
#     print(a11_list, "111")
#     print(a12_list, "222")
#
#     a21_list = [54, 26, 77, 93, 17, 77, 31, 44, 55, 20, 77]
#     a22_list = [54, 26, 77, 93, 17, 77, 31, 44, 55, 20, 77]
#     head1 = create(a21_list)
#     head2 = create(a22_list)
#     merge_sort_link = MergeSortLink()
#     h1 = merge_sort_link.merge_sort1(head1)
#     h2 = merge_sort_link.merge_sort2(head2)
#     print([i for i in travel(h1)], "^" * 10)
#     print([i for i in travel(h2)], "^" * 10)

pass

# # 快速排序
# def quick_sort(data, start, end):
#     if start >= end:
#         return
#     mid = data[start]
#     low, high = start, end
#     while low < high:
#         if data[high] >= mid:
#             high -= 1
#         data[low] = data[high]
#         if data[low] < mid:
#             low += 1
#         data[high] = data[low]
#     data[low] = mid
#     quick_sort(data, start, low - 1)
#     quick_sort(data, low + 1, end)
#
#
# class QuickSort:
#     stack = []
#
#     def quick_sort1(self, data):
#         """递归"""
#         self.quick_sort1_r(data, 0, len(data) - 1)
#
#     def quick_sort1_r(self, data, start, end):
#         if start >= end:
#             return
#         mid = self.partition(data, start, end)
#         self.quick_sort1_r(data, start, mid - 1)
#         self.quick_sort1_r(data, mid + 1, end)
#
#     def partition(self, data, start, end):
#         i, j = start, end - 1
#         pivot = data[end]
#         while i < j:
#             if data[i] < pivot:
#                 i += 1
#                 continue
#             if data[j] > pivot:
#                 j -= 1
#                 continue
#             self.swap(data, i, j)
#             i += 1
#             j -= 1
#         if data[j] < pivot:
#             j += 1
#         self.swap(data, j, end)
#         return j
#
#     @staticmethod
#     def swap(data, i, j):
#         temp = data[i]
#         data[i], data[j] = data[j], temp
#
#     def quick_sort2(self, data):
#         """非递归"""
#         self.quick_sort2_r(data, 0, len(data) - 1)
#
#     def quick_sort2_r(self, data, start, end):
#         self.stack.append(start)
#         self.stack.append(end)
#         while self.stack:
#             end = self.stack.pop()
#             start = self.stack.pop()
#             mid = self.partition(data, start, end)
#             if start < mid - 1:
#                 self.stack.append(start)
#                 self.stack.append(mid - 1)
#             if mid + 1 < end:
#                 self.stack.append(mid + 1)
#                 self.stack.append(end)
#
#
# class QuickSortLink:
#     stack = []
#
#     def quick_sort1(self, head):
#         """递归"""
#         if not head or not head.next:
#             return head
#         self.quick_sort1_r(head, self.get_end_node(head))
#         return head
#
#     def quick_sort1_r(self, start, end):
#         if not start or not start.next or start == end:
#             return
#         mid1, mid2 = self.partition(start, end)
#         self.quick_sort1_r(start, mid1)
#         self.quick_sort1_r(mid2, end)
#
#     def partition(self, start, end):
#         pivot = start.data
#         pre = start
#         i, j = start.next, start.next
#         while j != end.next:
#             if j.data < pivot:
#                 self.swap(i, j)
#                 pre = i
#                 i = i.next
#             j = j.next
#         self.swap(start, pre)
#         return pre, i
#
#     @staticmethod
#     def swap(node_a, node_b):
#         temp = node_a.data
#         node_a.data, node_b.data = node_b.data, temp
#
#     @staticmethod
#     def get_end_node(head):
#         cur = head
#         while cur.next:
#             cur = cur.next
#         return cur
#
#     def quick_sort2(self, head):
#         """非递归"""
#         if not head or not head.next:
#             return head
#         self.quick_sort2_r(head, self.get_end_node(head))
#         return head
#
#     def quick_sort2_r(self, start, end):
#         self.stack.append(start)
#         self.stack.append(end)
#         while self.stack:
#             end = self.stack.pop()
#             start = self.stack.pop()
#             mid1, mid2 = self.partition(start, end)
#             if start and start != mid1:
#                 self.stack.append(start)
#                 self.stack.append(mid1)
#             if mid2 and mid2 != end:
#                 self.stack.append(mid2)
#                 self.stack.append(end)
#
#
# if __name__ == '__main__':
#     a_list = [17, 20, 26, 31, 44, 54, 55, 77, 77, 77, 93]
#     print(a_list, "*" * 5)
#     a11_list = [54, 26, 77, 93, 17, 77, 31, 44, 55, 20, 77]
#     a12_list = [54, 26, 77, 93, 17, 77, 31, 44, 55, 20, 77]
#     quick_sort = QuickSort()
#     quick_sort.quick_sort1(a11_list)
#     quick_sort.quick_sort2(a12_list)
#     print(a11_list, "111")
#     print(a12_list, "222")
#
#     a21_list = [54, 26, 77, 93, 17, 77, 31, 44, 55, 20, 77]
#     a22_list = [54, 26, 77, 93, 17, 77, 31, 44, 55, 20, 77]
#     head1 = create(a21_list)
#     head2 = create(a22_list)
#     quick_sort_link = QuickSortLink()
#     h1 = quick_sort_link.quick_sort1(head1)
#     h2 = quick_sort_link.quick_sort2(head2)
#     print([i for i in travel(h1)], "^" * 10)
#     print([i for i in travel(h2)], "^" * 10)

pass

# # 二分查找算法
# def b_search(data, target):
#     left, right = 0, len(data) - 1
#     while left <= right:
#         mid = left + (right - left) // 2
#         if data[mid] > target:
#             right = mid - 1
#         elif data[mid] < target:
#             left = mid + 1
#         else:
#             if mid == 0 or data[mid - 1] != target:
#                 return mid
#             right = mid - 1
#     return -1
#
#
# if __name__ == '__main__':
#     a_list = [17, 20, 26, 31, 44, 54, 55, 77, 77, 77, 93]
#     print(a_list, "*" * 5)
#     print(b_search(a_list, 13))
#     print(b_search(a_list, 77))
#     print(b_search(a_list, 31))
#     print(b_search(a_list, 93))
#     print('-' * 50)

pass

# # 二叉树-创建-方法
# # 二叉树-遍历-方法
# # 二叉树-前中后序遍历-方法
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.lchild = None
#         self.rchild = None
#
#
# def create_tree(data):
#     root = None
#     for i in data:
#         nn = TreeNode(i)
#         if root is None:
#             root = nn
#         else:
#             q = [root]
#             while q:
#                 n = q.pop(0)
#                 if n.lchild is None:
#                     n.lchild = nn
#                     q = []
#                     continue
#                 if n.rchild is None:
#                     n.rchild = nn
#                     q = []
#                     continue
#                 q.append(n.lchild)
#                 q.append(n.rchild)
#     return root
#
#
# def travel_tree(root):
#     if root is None:
#         return None
#     q = [root]
#     while q:
#         n = q.pop(0)
#         yield n.data
#         if n.lchild:
#             q.append(n.lchild)
#         if n.rchild:
#             q.append(n.rchild)
#
#
# def order(root):
#     if root is None:
#         return
#     yield root.data
#     yield from order(root.lchild)
#     yield from order(root.rchild)
#
#
# if __name__ == '__main__':
#     a_list = [17, 20, 26, 31, 44, 54, 55, 77, 77, 77, 93]
#     print(a_list, "*" * 5)
#     root1 = create_tree(a_list)
#     print([i for i in travel_tree(root1)])
#     print([i for i in order(root1)])
#     root2 = create_tree([])
#     print([i for i in travel_tree(root2)])
#     print([i for i in order(root2)])
#     print('-' * 50)

pass

# # 二叉树-创建-类
# # 二叉树-遍历-类
# # 二叉树-前中后序遍历-类
# class TreeNode(object):
#     def __init__(self, data):
#         self.data = data
#         self.lchild = None
#         self.rchild = None
#
#
# class Tree(object):
#     def __init__(self):
#         self.root = None
#
#     def create_tree(self, data):
#         nn = TreeNode(data)
#         if self.root is None:
#             self.root = nn
#         else:
#             q = [self.root]
#             while q:
#                 n = q.pop(0)
#                 if n.lchild is None:
#                     n.lchild = nn
#                     return
#                 if n.rchild is None:
#                     n.rchild = nn
#                     return
#                 q.append(n.lchild)
#                 q.append(n.rchild)
#
#     def travel_tree(self):
#         if self.root is None:
#             return
#         q = [self.root]
#         while q:
#             n = q.pop(0)
#             yield n.data
#             if n.lchild:
#                 q.append(n.lchild)
#             if n.rchild:
#                 q.append(n.rchild)
#
#     def order(self, node):
#         if node is None:
#             return
#         yield node.data
#         yield from self.order(node.lchild)
#         yield from self.order(node.rchild)
#
#
# if __name__ == '__main__':
#     a_list = [17, 20, 26, 31, 44, 54, 55, 77, 77, 77, 93]
#     print(a_list, "*" * 5)
#     tree = Tree()
#     for i in a_list:
#         tree.create_tree(i)
#     print([i for i in tree.travel_tree()])
#     print([i for i in tree.order(tree.root)])
#
#     tree2 = Tree()
#     for i in []:
#         tree2.create_tree(i)
#     print([i for i in tree2.travel_tree()])
#     print([i for i in tree2.order(tree2.root)])
#     print('-' * 50)

pass

# # 单链表-前创建-方法
# # 单链表-后创建-方法
# # 单链表-遍历-方法
# # 单链表-反转-方法
# # 单链表-合并-方法
# # 单链表-检查环-方法
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# def create1(data):
#     head = None
#     for i in data:
#         n = Node(i)
#         n.next = head
#         head = n
#     return head
#
#
# def create2(data):
#     head = None
#     for i in data:
#         n = Node(i)
#         if head is None:
#             head = n
#         else:
#             cur = head
#             while cur.next:
#                 cur = cur.next
#             cur.next = n
#     return head
#
#
# def create3(data):
#     head, tail = None, None
#     for i in data:
#         n = Node(i)
#         if head is None:
#             head = tail = n
#         else:
#             tail.next = n
#             tail = n
#     return head
#
#
# def create4(data):
#     new_head = Node(None)
#     tail = new_head
#     for i in data:
#         n = Node(i)
#         tail.next = n
#         tail = n
#     return new_head.next
#
#
# def travel(head):
#     while head:
#         yield head.data
#         head = head.next
#
#
# def merge(h1, h2):
#     if h1 is None:
#         return h2
#     if h2 is None:
#         return h1
#     if h1.data < h2.data:
#         h1.next = merge(h1.next, h2)
#         return h1
#     h2.next = merge(h1, h2.next)
#     return h2
#
#
# def reverse(head):
#     if head is None or head.next is None:
#         return head
#     cur, pre = head, None
#     while cur:
#         next_ = cur.next
#         cur.next = pre
#         pre = cur
#         cur = next_
#     return pre
#
#
# def has_ring(head):
#     slow, fast = head, head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if slow == fast:
#             return True
#     return False
#
#
# if __name__ == '__main__':
#     a_list = [17, 20, 26, 31, 44, 54, 55, 77, 77, 77, 93]
#     print(a_list, "*" * 5)
#     h1 = create1(a_list)
#     print([i for i in travel(h1)])
#     h2 = create2(a_list)
#     print([i for i in travel(h2)])
#     h3 = create3(a_list)
#     print([i for i in travel(h3)])
#     h4 = create4(a_list)
#     print([i for i in travel(h4)])
#
#     h8 = reverse(h1)
#     print([i for i in travel(h8)])
#
#     b_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#     h5 = create3(b_list)
#     print([i for i in travel(h5)])
#     h6 = merge(h5, h2)
#     print([i for i in travel(h6)])
#
#     c_list = [10, 20, 30, 40, 20, 30, 40, 20, 30, 40]
#     h7 = create3(c_list)
#     print([i for i in travel(h7)])
#     print(has_ring(h7))

pass

# # 单链表-前创建-类
# # 单链表-后创建-类
# # 单链表-遍历-类
# # 单链表-查找-类
# # 单链表-插入-类
# # 单链表-删除-类
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class Single:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.new_head = Node(None)
#
#     def add(self, data):
#         n = Node(data)
#         n.next = self.head
#         self.head = n
#
#     def append1(self, data):
#         n = Node(data)
#         if self.head is None:
#             self.head = n
#         else:
#             cur = self.head
#             while cur.next:
#                 cur = cur.next
#             cur.next = n
#
#     def append2(self, data):
#         n = Node(data)
#         if self.head is None:
#             self.head = n
#             self.tail = n
#         else:
#             self.tail.next = n
#             self.tail = n
#
#     def travel(self):
#         cur = self.head
#         while cur:
#             yield cur.data
#             cur = cur.next
#
#     def search(self, data):
#         cur = self.head
#         while cur:
#             if cur.data == data:
#                 return True
#             cur = cur.next
#         return False
#
#     def remove(self, data):
#         cur = self.head
#         pre = None
#         while cur:
#             if cur.data == data:
#                 if cur == self.head:
#                     self.head = cur.next
#                 else:
#                     pre.next = cur.next
#                 return
#             else:
#                 pre = cur
#                 cur = cur.next
#
#     def length(self):
#         count = 0
#         cur = self.head
#         while cur:
#             count += 1
#             cur = cur.next
#         return count
#
#     def insert(self, index, data):
#         if index <= 0:
#             self.add(data)
#         elif index >= self.length():
#             self.append1(data)
#         else:
#             cur = self.head
#             count = 0
#             while count < index - 1:
#                 count += 1
#                 cur = cur.next
#             n = Node(data)
#             n.next = cur.next
#             cur.next = n
#
#
# if __name__ == '__main__':
#     a_list = [17, 20, 26, 31, 44, 54, 55, 77, 77, 77, 93]
#     print(a_list, "*" * 5)
#     h1 = Single()
#     for i in a_list:
#         h1.add(i)
#     print([i for i in h1.travel()])
#     h2 = Single()
#     for i in a_list:
#         h2.append1(i)
#     print([i for i in h2.travel()])
#     h3 = Single()
#     for i in a_list:
#         h3.append2(i)
#     print([i for i in h3.travel()])
#
#     ret = h3.search(93)
#     print(ret)
#     h3.remove(93)
#     print([i for i in h3.travel()])
#     h3.insert(2, 666)
#     print([i for i in h3.travel()])

pass

# # 用两个栈实现队列
# class Q:
#     def __init__(self):
#         self.s1 = []
#         self.s2 = []
#
#     def push(self, data):
#         self.s1.append(data)
#
#     def pop(self):
#         n = len(self.s2)
#         if n == 0:
#             while self.s1:
#                 self.s2.append(self.s1.pop())
#         return self.s2.pop()
#
#
# if __name__ == '__main__':
#     s = Q()
#     s.push(1)
#     s.push(2)
#     a1 = s.pop()
#     s.push(3)
#     a2 = s.pop()
#     s.push(4)
#     a3 = s.pop()
#     print(a1)
#     print(a2)
#     print(a3)

pass

# 双向链表
# 希尔排序

# 字典排序

# 单例模式
# 装饰器
# reduce，partial，map，filter，wraps，functools，collections，-10
