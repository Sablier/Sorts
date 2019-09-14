class Node(object):
    """节点类"""

    def __init__(self, item):
        self.item = item
        self.next = None
        self.pre = None


class DoubleLinkList(object):
    """链表类"""

    def __init__(self):
        # 记录首节点
        self.__head = None

    def is_empty(self):
        """链表是否为空"""
        # 判断首节点
        return self.__head is None

    def travel(self):
        """遍历链表"""
        # 创建游标
        cur = self.__head
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print()

    def length(self):
        """获取链表的长度"""
        # 创建游标
        cur = self.__head
        # 创建计数器
        count = 0

        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def add(self, item):
        """向链表头部添加数据"""
        # 创建新节点
        node = Node(item)
        if self.is_empty():
            self.__head = node
            return

        # 将新节点的next指向老节点
        node.next = self.__head
        # 让老的头的pre指向新的头
        self.__head.pre = node
        # 让头节点记录新的头
        self.__head = node

    def append(self, item):
        """向链表尾部添加"""
        if self.is_empty():
            self.add(item)
            return
        cur = self.__head
        # 遍历寻找尾节点
        while cur.next is not None:
            cur = cur.next
        node = Node(item)
        # 当我们找到尾节点的时候，将新节点指向原来尾节点的next
        cur.next = node
        # 将新节点的pre指向老节点
        node.pre = cur

    # while循环遍历
    def insert(self, pos, item):
        """向指定位置添加节点"""
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            # 先遍历，找到pos位置的前一个节点
            cur = self.__head
            index = 0
            while index < (pos - 1):
                index += 1
                cur = cur.next
            node = Node(item)
            # 让新节点的next指向pos节点
            node.next = cur.next
            cur.next.pre = node
            # 在让cur节点指向新的节点
            cur.next = node
            node.pre = cur

    # for循环遍历
    def insert_v2(self, pos, item):
        """向指定位置添加节点"""
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            # 先遍历，找到pos位置的前一个节点
            cur = self.__head
            for i in range(pos-1):
                cur = cur.next
            node = Node(item)
            # 让新节点的next指向pos节点
            node.next = cur.next
            cur.next.pre = node
            # 在让cur节点指向新的节点
            cur.next = node
            node.pre = cur

    def remove(self,item):
        """按内容删除元素"""
        # 创建游标
        cur = self.__head
        # 遍历链表，寻找要删除的节点
        while cur is not None:
            # 判断当前节点是否是要删除的节点
            if cur.item == item:
                # 如果pre为空，证明要删除的是首节点
                if cur.pre is None:
                    self.__head = cur.next
                else:
                    # 删除：让当前节点的前一个节点的next指向当前节点的下一个节点
                    cur.pre.next = cur.next
                    if cur.next is None:
                        return
                    cur.next.pre = cur.pre
            cur = cur.next

    def search(self,item):
        """查找元素是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


if __name__ == '__main__':
    sll = DoubleLinkList()
    print(sll.length())
    print(sll.is_empty())
    sll.add(6)
    print(sll.is_empty())
    sll.add(5)
    sll.add(4)
    sll.travel()
    print(sll.length())
    sll.append(7)
    sll.travel()
    sll.insert_v2(3, 8)
    sll.travel()
    sll.remove(8)
    sll.travel()
    print(sll.search(6))
    print(sll.search(8))
