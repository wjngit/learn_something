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

# # 冒泡排序
# def bubble_sort(data):
#     n = len(data)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if data[j] > data[j + 1]:
#                 data[j + 1], data[j] = data[j], data[j + 1]
#
#
# if __name__ == '__main__':
#     a_list = [17, 20, 26, 31, 44, 54, 55, 77, 77, 77, 93]
#     print(a_list, "*" * 5)
#     a1_list = [54, 26, 77, 93, 17, 77, 31, 44, 55, 20, 77]
#     bubble_sort(a1_list)
#     print(a1_list)

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
# if __name__ == '__main__':
#     a_list = [17, 20, 26, 31, 44, 54, 55, 77, 77, 77, 93]
#     print(a_list, "*" * 5)
#     a1_list = [54, 26, 77, 93, 17, 77, 31, 44, 55, 20, 77]
#     insert_sort(a1_list)
#     print(a1_list)

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
# if __name__ == '__main__':
#     a_list = [17, 20, 26, 31, 44, 54, 55, 77, 77, 77, 93]
#     print(a_list, "*" * 5)
#     a1_list = [54, 26, 77, 93, 17, 77, 31, 44, 55, 20, 77]
#     select_sort(a1_list)
#     print(a1_list)

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
# if __name__ == '__main__':
#     a_list = [17, 20, 26, 31, 44, 54, 55, 77, 77, 77, 93]
#     print(a_list, "*" * 5)
#     a1_list = [54, 26, 77, 93, 17, 77, 31, 44, 55, 20, 77]
#     a1_list = merge_sort(a1_list)
#     print(a1_list)

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
# if __name__ == '__main__':
#     a_list = [17, 20, 26, 31, 44, 54, 55, 77, 77, 77, 93]
#     print(a_list, "*" * 5)
#     a1_list = [54, 26, 77, 93, 17, 77, 31, 44, 55, 20, 77]
#     quick_sort(a1_list, 0, len(a1_list) - 1)
#     print(a1_list)

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
#     s.push(3)
#     s.push(4)
#
#     a1 = s.pop()
#     a2 = s.pop()
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
