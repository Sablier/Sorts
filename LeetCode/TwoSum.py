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
                if j > i:
                    return i + 1, j + 1
                # else:
                #     return j + 1, i + 1


class Solution(object):
    def twoSum(self, numbers, target):

        for index1, value1 in enumerate(numbers):
            for index2, value2 in enumerate(numbers):
                if index2 > index1 and value1 + value2 == target:
                    return index1 + 1, index2 + 1


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    res = func(numbers, target)
    print(res)
    so = Solution()
    res = so.twoSum(numbers, target)
    print(res)
