class Node(object):
    def __init__(self, data):
        self.data = data
        self.l_child = None
        self.r_child = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, data):
        node = Node(data)

        if self.root is None:
            self.root = node
        else:
            queue = [self.root]
            while queue:
                n = queue.pop(0)
                if n.l_child is None:
                    n.l_child = node
                    return
                elif n.r_child is None:
                    n.r_child = node
                    return
                else:
                    queue.append(n.l_child)
                    queue.append(n.r_child)

    def travel(self):
        if self.root is None:
            return
        else:
            queue = [self.root]
            while queue:
                n = queue.pop(0)
                print(n.data, end=' ')
                if n.l_child:
                    queue.append(n.l_child)
                if n.r_child:
                    queue.append(n.r_child)

    def travel1(self):
        if self.root is None:
            return
        q = [self.root]
        while q:
            n = q.pop(0)
            print(n.data, end=' ')
            if n.l_child:
                q.append(n.l_child)
            if n.r_child:
                q.append(n.r_child)

    def pre_order(self, node):
        if node is None:
            return
        self.pre_order(node.l_child)
        self.pre_order(node.r_child)
        print(node.data, end=' ')

    def preorder(self, root):
        if root is None:
            return
        print(root.data, end=' ')
        self.preorder(root.l_child)
        self.preorder(root.r_child)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.l_child)
        print(root.data, end=' ')
        self.inorder(root.r_child)


if __name__ == '__main__':
    t = Tree()
    for i in range(10):
        t.add(i)
    # t.travel1()
    t.pre_order(t.root)
    print('\n')
    t.inorder(t.root)
