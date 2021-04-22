class Node():
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None

class Tree():

    def __init__(self):
        self.root=None

    def add(self,data):
        node=Node(data)

        if self.root==None:
            self.root=node

        else:
            queue=[]
            queue.append(self.root)
            while queue:
                n=queue.pop(0)
                if n.lchild==None:
                    n.lchild=node
                    return
                elif n.rchild==None:
                    n.rchild=node
                    return
                else:
                    queue.append(n.lchild)
                    queue.append(n.rchild)

    def travle(self):
        if self.root==None:
            print('')
            return
        else:
            queue=[]
            queue.append(self.root)
            while queue:
                n=queue.pop(0)
                print(n.data,end=' ')

                if n.lchild:
                    queue.append(n.lchild)
                if n.rchild:
                    queue.append(n.rchild)

        print('')
    def preorder(self,root):
        if root==None:
            return
        print(root.data,end=' ')
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self,root):
        if root==None:
            return

        self.inorder(root.lchild)
        print(root.data, end=' ')
        self.inorder(root.rchild)


t=Tree()
for i in range(10):
    t.add(i)
t.travle()
# t.preorder(t.root)
t.inorder(t.root)
