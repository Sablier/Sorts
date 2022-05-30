"""单项循环链表"""


class Node(object):
    """节点类"""

    def __init__(self, content):
        self.content = content
        self.next = None


class SingleCycLinkList(object):
    """链表类"""

    def __init__(self):
        # 记录首节点
        self.__head = None

    def is_empty(self):
        """链表是否为空"""
        # 判断首节点
        return self.__head is None

    def scan(self):
        """遍历链表"""
        if self.is_empty():
            print("None")
            return
        # 创建游标
        cur = self.__head
        print(cur.content, end=" ")
        while cur.next is not self.__head:
            cur = cur.next
            print(cur.content, end=" ")
        print()

    def length(self):
        """获取链表的长度"""
        if self.is_empty():
            return 0
        # 创建游标
        cur = self.__head
        # 创建计数器
        count = 1
        while cur.next is not self.__head:
            count += 1
            cur = cur.next
        return count

    def add(self, content):
        """向链表头部添加数据"""
        # 创建新节点
        node = Node(content)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        # 创建游标
        cur = self.__head
        # 遍历，找到尾节点
        while cur.next is not self.__head:
            cur = cur.next
        # 循环结束，cur指向的是尾节点
        # 将新节点的next指向老节点
        node.next = self.__head
        # 让头节点记录新的头
        self.__head = node
        cur.next = self.__head

    def append(self, content):
        """向链表尾部添加"""
        if self.is_empty():
            self.add(content)
            return
        cur = self.__head
        # 遍历寻找尾节点
        while cur.next is not self.__head:
            cur = cur.next
        # 当我们找到尾节点的时候，将新节点指向原来尾节点的next
        node = Node(content)
        cur.next = node
        # 让新的尾节点指向头节点
        node.next = self.__head

    # while循环遍历
    def insert(self, pos, content):
        """向指定位置添加节点"""
        if pos <= 0:
            self.add(content)
        elif pos >= self.length():
            self.append(content)
        else:
            # 先遍历，找到pos位置的前一个节点
            cur = self.__head
            index = 0
            while index < (pos - 1):
                index += 1
                cur = cur.next
            node = Node(content)
            # 让新节点的next指向pos节点
            node.next = cur.next
            # 在让cur节点指向新的节点
            cur.next = node

    # for循环遍历
    def insert_v2(self, pos, content):
        """向指定位置添加节点"""
        if pos <= 0:
            self.add(content)
        elif pos >= self.length():
            self.append(content)
        else:
            # 先遍历，找到pos位置的前一个节点
            cur = self.__head
            for i in range(pos-1):
                cur = cur.next
            node = Node(content)
            # 让新节点的next指向pos节点
            node.next = cur.next
            # 在让pos前一个节点指向新的节点
            cur.next = node

    def remove(self,content):
        """按内容删除元素"""
        # 创建游标
        cur = self.__head
        # 记录当前节点的前一个节点
        pre = None
        # 遍历链表，寻找要删除的节点
        while cur.next is not self.__head:
            # 判断当前节点是否是要删除的节点
            if cur.content == content:
                # 如果pre为空，证明要删除的是首节点
                if pre is None:
                    self.__head = cur.next
                    # 遍历寻找尾节点，让尾节点指向新的头
                    temp = self.__head
                    while temp.next is not self.__head:
                        temp = temp.next
                    self.__head = cur.next
                    temp.next = self.__head
                else:
                    pre.next = cur.next
            pre = cur
            cur = cur.next
        # while循环遍历不到尾节点
        if cur.content == content:
            if pre is None:  # 链表只有一个节点，删除该节点
                self.__head = None
            else:
                pre.next = self.__head

    def search(self,content):
        """查找元素是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.content == content:
                return True
            cur = cur.next
        return False


if __name__ == '__main__':
    sll = SingleCycLinkList()
    # print(sll.length())
    print(sll.is_empty())
    sll.add(6)
    print(sll.is_empty())
    sll.add(5)
    sll.add(4)
    sll.scan()
    print(sll.length())
    sll.append(7)
    sll.scan()
    sll.insert_v2(-3, 8)
    sll.scan()
    sll.remove(8)
    sll.scan()
    print(sll.search(6))

