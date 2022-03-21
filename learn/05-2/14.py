# 706. 设计哈希映射
#
# 不使用任何内建的哈希表库设计一个哈希映射（HashMap）。
# 实现 MyHashMap 类：
#     MyHashMap() 用空映射初始化对象
#     void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
#     int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
#     void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。
#
# 示例：
# 输入：
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# 输出：
# [null, null, null, 1, -1, null, 1, null, -1]
#
# 解释：
#     MyHashMap myHashMap = new MyHashMap();
#     myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]]
#     myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]]
#     myHashMap.get(1);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
#     myHashMap.get(3);    // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
#     myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
#     myHashMap.get(2);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
#     myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
#     myHashMap.get(2);    // 返回 -1（未找到），myHashMap 现在为 [[1,1]]
#
# 提示：
#     0 <= key, value <= 106
#     最多调用 104 次 put、get 和 remove 方法


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class MyHashMap:

    def __init__(self):
        self.__slot_count = 3535
        self.slots = [None] * self.__slot_count

    def hash(self, key):
        return key % self.__slot_count

    def put(self, key: int, value: int) -> None:
        slot = self.slots[self.hash(key)]
        if slot is None:
            self.slots[self.hash(key)] = []
            slot = self.slots[self.hash(key)]
        for index, node in enumerate(slot):
            if node.key == key:
                slot.pop(index)
                break
        new_pair = Node(key, value)
        slot.append(new_pair)

    def get(self, key: int) -> int:
        slot = self.slots[self.hash(key)]
        if slot is None:
            return -1
        for node in slot:
            if node.key == key:
                return node.value
        return -1

    def remove(self, key: int) -> None:
        slot = self.slots[self.hash(key)]
        if not slot:
            return None
        for index, node in enumerate(slot):
            if node.key == key:
                slot.pop(index)
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


if __name__ == '__main__':
    # ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
    # [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
    # todo: 实现一遍
    h = MyHashMap()
    print(h.put(1, 1))
    print(h.put(2, 2))
    print(h.get(1))
    print(h.get(3))
    print(h.put(2, 1))
    print(h.get(2))
    print(h.remove(2))
    print(h.get(2))
