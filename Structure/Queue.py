class Queue(object):
    """构造一个队列"""

    def __init__(self):
        self.data = []

    def enqueue(self, content):
        """添加一个元素"""
        self.data.insert(0, content)

    def dequeue(self):
        """取出一个元素"""
        return self.data.pop()

    def is_empty(self):
        """判断栈是否为空"""
        return self.data == []

    def size(self):
        """返回栈的元素个数"""
        return len(self.data)


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
