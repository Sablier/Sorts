"""
原题：

给一个int型数组，要求找出其中两个和为特定值的数的坐标。

注意点：

返回的坐标一要比坐标二小 最小的坐标是1，不是0

例子：

输入:	numbers={2,	7,	11,	15},	target=9

输出:	index1=1,	index2=2
"""


def func(numbers, target):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] + numbers[j] == int(target):
                if i > j:
                    return j + 1, i + 1
                else:
                    return i + 1, j + 1


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    res = func(numbers, target)
    print(res)
