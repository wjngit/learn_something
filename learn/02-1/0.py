# 手撕单链表
class Node(object):
    def __init__(self, data='default'):
        self.value = data
        self.relate = None


class SingleList(object):
    def __init__(self, data):
        self.data = data

        temp_node = Node()
        temp_tail = temp_node
        for item in self.data:
            new_node = Node(item)
            temp_tail.relate = new_node
            temp_tail = new_node
        self.head = temp_node.relate

    def travel(self, head=Node()):
        if head and head.value == 'default':
            cursor = self.head
        else:
            cursor = head
        while cursor:
            yield cursor.value
            cursor = cursor.relate

    def find_and_travel(self, value):
        cursor = self.head
        return_head = None
        while cursor:
            if cursor.value == value:
                return_head = cursor
                break
            cursor = cursor.relate
        return self.travel(return_head)

    def find(self, value):
        cursor = self.head
        return_head = None
        while cursor:
            if cursor.value == value:
                return_head = cursor
                break
            cursor = cursor.relate
        return return_head

    def head_insert(self, data):
        new_node = Node(data)
        new_node.relate = self.head
        self.head = new_node
        return self.travel(self.head)

    def tail_insert(self, data):
        new_node = Node(data)
        if self.head:
            cursor = self.head
            while cursor.relate:
                cursor = cursor.relate
            cursor.relate = new_node
        else:
            self.head = new_node
        return self.travel(self.head)

    def node_insert(self, value, data):
        new_node = Node(data)
        if self.head:
            cursor = self.head
            while cursor.relate:
                if cursor.value == value:
                    new_node.relate = cursor.relate
                    cursor.relate = new_node
                    break
                cursor = cursor.relate
            cursor.relate = new_node
        else:
            self.head = new_node
        return self.travel(self.head)

    def remove(self, node):
        if node:
            temp_node = Node()
            temp_node.relate = self.head
            cursor = self.head
            pre = temp_node
            while cursor:
                if cursor.value == node.value:
                    pre.relate = cursor.relate
                    break
                pre = cursor
                cursor = cursor.relate
            self.head = temp_node.relate
        return self.travel(self.head)

    def remove_relate(self, node):
        if node and node.relate:
            cursor = self.head
            while cursor.relate:
                if cursor.value == node.value:
                    cursor.relate = cursor.relate.relate
                    break
                cursor = cursor.relate
        return self.travel(self.head)


if __name__ == '__main__':
    data_list = [1, 2, 3, 4, 5, 6, 7]
    # data_list = []
    single_list = SingleList(data_list)
    print([i for i in single_list.travel()])
    print([i for i in single_list.find_and_travel(8)])
    print([i for i in single_list.head_insert(8)])
    print([i for i in single_list.tail_insert(9)])
    find_node = single_list.find(8)
    print([i for i in single_list.travel(find_node)])
    print([i for i in single_list.node_insert(find_node.value, 10)])
    print([i for i in single_list.remove(find_node)])
    find_node = single_list.find(None)
    print([i for i in single_list.remove_relate(find_node)])
    pass
