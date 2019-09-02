def quick_sort(tlist, start, end):
    # 0. 规定递归的跳出条件
    if start >= end:
        return

    # 1. 初始化，确定基准pivot
    leftPointer = start
    rightPointer = end
    pivot = tlist[start]

    # 2. 分区操作（partition）
    while leftPointer < rightPointer:
        # 首先右侧指针从右往左移动，若指针位置的值比基准pivot大则继续向左移动
        while leftPointer < rightPointer and tlist[rightPointer] >= pivot:
            rightPointer -= 1
        # 如果指针元素比基准小，则将指针元素移动到左侧指针的位置（第一次则移动到基准元素的位置上）
        tlist[leftPointer] = tlist[rightPointer]

        # 然后左侧指针从左往右移动，若指针位置的值比基准pivot小则继续向右移动
        while leftPointer < rightPointer and tlist[leftPointer] < pivot:
            leftPointer += 1
        # 如果指针元素比基准大，则将指针元素移动到左侧指针的位置
        tlist[rightPointer] = tlist[leftPointer]

        # 如果左侧指针位置依然比右侧小则进入下一个循环

    # 当左右游标重合后不再满足while条件，跳出循环，将基准元素放置在重合的指针位置。
    tlist[rightPointer] = pivot

    # 对于元素移动为什么不会覆盖原有元素的说明：
    # 在判断与基准元素的相对大小并移动元素时，将要被覆盖的元素是对面指针停留的位置，这个位置上的元素在上一轮移动元素的刚刚被移到了列表的另一端。
    # 而第一次被右边指针覆盖的元素是列表的基准值pivot，它已经被提前保存了。所以经过一系列移动，元素并不会减少，也不存在漏判断的问题。

    # 3. 递归排序
    quick_sort(tlist, 0, rightPointer - 1)
    quick_sort(tlist, rightPointer + 1, end)

    return tlist


if __name__ == '__main__':
    tlist = [7850, 76892, 49169, 44721, 51861, 66149, 18273, 94882, 63497, 8427, 65300, 20822, 15745, 12270, 31608,
             38276, 36210, 21632, 33084, 61789]
    print(quick_sort(tlist, 0, len(tlist) - 1))
