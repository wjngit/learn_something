class Node(object):
    def __init__(self, data):
        self.data = data
        self.link = None


if __name__ == '__main__':
    n = Node(100)
    print(n.data)
    n2 = Node(200)
    n.link = n2
    print(n.link.data)
    print(n2.data)
