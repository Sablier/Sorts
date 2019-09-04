class Node(object):
    """节点类"""

    def __init__(self, item, lchild=None, rchild=None):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """完全二叉树"""

    def __init__(self):
        self.__root = None

    def add(self, item):
        """添加子节点"""

        node = Node(item)

        if self.__root is None:
            self.__root = node
            return

        # 广度优先遍历（层次遍历）找到最后一个节点，在其后面添加新节点
        # 添加新节点应该从上到下，从左到右
        queue = []
        queue.append(self.__root)

        while queue:
            tnode = queue.pop(0)
            if tnode.lchild is None:
                tnode.lchild = node
                return
            if tnode.rchild is None:
                tnode.rchild = node
                return
            queue.append(tnode.lchild)
            queue.append(tnode.rchild)

    def breath_travel(self):
        """广度优先遍历，层次遍历"""

        if self.__root is None:
            return

        queue = []
        queue.append(self.__root)

        node = queue.pop(0)
        print(node.item)

        if node.lchild is not None:
            queue.append(node.lchild)
        if node.rchild is not None:
            queue.append(node.rchild)

    def depth_travel(self):
        """深度优先遍历，用递归调用子节点"""
        # self.pre_order(self.__root)
        # self.in_order(self.__root)
        self.post_order(self.__root)
        print()

    def pre_order(self, node):
        """先序 根 左 右"""
        if node is None:
            return
        print(node.item, end=" ")
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)

    def in_order(self, node):
        """中序 左 根 右"""
        if node is None:
            return
        self.in_order(node.lchild)
        print(node.item, end=" ")
        self.in_order(node.rchild)

    def post_order(self, node):
        """后序 左  右 根"""
        if node is None:
            return
        self.post_order(node.lchild)
        self.post_order(node.rchild)
        print(node.item,end=" ")

if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    # tree.breath_travel()
    tree.depth_travel()
