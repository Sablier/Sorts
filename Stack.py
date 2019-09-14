class Stack(object):
    """构造一个栈"""

    def __init__(self):
        self.data = []

    def push(self,item):
        """添加一个元素（到栈顶）"""
        self.data.append(item)

    def pop(self):
        """弹出栈顶的元素"""
        return self.data.pop()

    def peek(self):
        """查看栈顶的元素"""
        return self.data[-1]

    def is_empty(self):
        """判断栈是否为空"""
        return self.data == []

    def size(self):
        """返回栈的元素个数"""
        return len(self.data)


if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    stack.push("h")
    stack.push("e")
    stack.push("l")
    stack.push("l")
    stack.push("o")
    print(stack.peek())
    print(stack.is_empty())
    print(stack.pop())
    print(stack.pop())
    print(stack.peek())