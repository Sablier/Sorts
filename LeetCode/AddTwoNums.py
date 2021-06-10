"""
原题：
定义这样的一个链表，链表的每个节点都存有一个0-9的数字，把链表当成数字， 表头为高位，表尾为低位。如1->2->3表示321，现在要对两个这样的链表求和。

注意点：
数字的高低位，应该从从低位向高位进位 有多种情况要考虑，如链表长度是否相等、是否进位等

例子：
输入: (2 -> 4 -> 3) + (5 -> 6 -> 4)
输出: 7 -> 0 -> 8
"""


class Node(object):
    """节点类"""

    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    """链表类"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def travel(self):
        """遍历链表"""
        cur = self.head
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next

    def add(self, item):
        """向链表头部添加数据"""
        node = Node(item)
        node.next = self.head
        self.head = node

    def append(self, item):
        """向链表尾部添加"""
        if self.is_empty():
            self.add(item)
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        node = Node(item)
        cur.next = node


def add_links(a, b):
    a_list = []
    a_node = a.head
    while a_node is not None:
        a_list.append(a_node.item)
        a_node = a_node.next

    b_list = []
    b_node = b.head
    while b_node is not None:
        b_list.append(b_node.item)
        b_node = b_node.next

    longer = 'a' if len(a_list) > len(b_list) else 'b'
    diff_len = abs(len(a_list) - len(b_list))

    while diff_len:
        if longer == 'a':
            a_list.insert(0, 0)
        else:
            b_list.insert(0, 0)
        diff_len = abs(len(a_list) - len(b_list))

    carry = 0
    sum_list = []
    for digit in range(len(a_list)-1, -1, -1):
        digit_sum = a_list[digit] + b_list[digit]
        digit_sum += carry
        carry = 0
        if digit_sum >= 10:
            carry = 1
            digit_sum -= 10
        sum_list.insert(0, digit_sum)
    if carry:
        sum_list.insert(0, 1)

    sum_link = SingleLinkList()
    for digit in range(len(sum_list)):
        sum_link.append(sum_list[digit])

    return sum_link


if __name__ == '__main__':
    a = SingleLinkList()
    a.append(4)
    a.append(4)
    a.append(2)

    b = SingleLinkList()
    b.append(5)
    b.append(6)
    b.append(5)

    res = add_links(a, b)
    res.travel()