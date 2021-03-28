class Dequeue(object):
    """构造一个双端队列"""

    def __init__(self):
        self.data = []

    def add_front(self,item):
        """添加一个元素到头部"""
        self.data.insert(0,item)

    def add_rear(self,item):
        """添加一个元素到队尾"""
        self.data.append(item)

    def remove_front(self):
        """从队首取出元素"""
        return self.data.pop(0)

    def remove_rear(self):
        """从队尾取出元素"""
        return self.data.pop()

    def is_empty(self):
        """判断队列是否为空"""
        return self.data == []

    def size(self):
        """返回队列的元素个数"""
        return len(self.data)


if __name__ == '__main__':
    queue = Dequeue()
    queue.add_front(1)
    queue.add_front(2)
    queue.add_front(3)
    print(queue.remove_front())
    print(queue.remove_rear())
    print(queue.remove_rear())