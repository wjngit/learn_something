# 146. LRU 缓存
#
# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：
#     LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
#     int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
#     void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；
#         如果不存在，则向缓存中插入该组 key-value 。
#         如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
#
# 示例：
#     输入：
#         ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
#         [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
#     输出：
#         [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# 解释：
#     LRUCache lRUCache = new LRUCache(2);
#     lRUCache.put(1, 1); // 缓存是 {1=1}
#     lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
#     lRUCache.get(1);    // 返回 1
#     lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
#     lRUCache.get(2);    // 返回 -1 (未找到)
#     lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
#     lRUCache.get(1);    // 返回 -1 (未找到)
#     lRUCache.get(3);    // 返回 3
#     lRUCache.get(4);    // 返回 4
#
# 提示：
#     1 <= capacity <= 3000
#     0 <= key <= 10000
#     0 <= value <= 10^5
#     最多调用 2 * 10^5 次 get 和 put


class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.hash_table = dict()
        self.head = Node()
        self.tail = Node()
        self.head.pre = None
        self.head.next = self.tail
        self.tail.pre = self.head
        self.tail.next = None

    def get(self, key: int) -> int:
        if self.size == 0:
            return -1
        node = self.hash_table.get(key)
        if not node:
            return -1
        self.remove_node(node)
        self.add_node_at_head(node)
        return node.value

    def remove(self, key):
        node = self.hash_table.get(key)
        if node:
            self.remove_node(node)
            self.hash_table.pop(node)
        return

    @staticmethod
    def remove_node(node):
        node.next.pre = node.pre
        node.pre.next = node.next

    def add_node_at_head(self, node):
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node
        node.pre = self.head

    def put(self, key: int, value: int) -> None:
        node = self.hash_table.get(key)
        if node:
            node.value = value
            self.remove_node(node)
            self.add_node_at_head(node)
            return
        if self.size == self.capacity:
            self.hash_table.pop(self.tail.pre.key)
            self.remove_node(self.tail.pre)
            self.size -= 1
        new_node = Node(key, value)
        self.add_node_at_head(new_node)
        self.hash_table[key] = new_node
        self.size += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    # ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    # [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    lru = LRUCache(2)
    print(lru.put(1, 1))
    print(lru.put(2, 2))
    print(lru.get(1))
    print(lru.put(3, 3))
    print(lru.get(2))
    print(lru.put(4, 4))
    print(lru.get(1))
    print(lru.get(3))
    print(lru.get(4))
