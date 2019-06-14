def selection_sort(tlist):
    # 共执行n-1轮选择
    n = len(tlist) - 1

    while n > 0:
        # 取出基准
        pivot = tlist.pop(0)
        # 便利列表，如果找到比基准小的值则和基准交换
        for i in range(n):
            if tlist[i] < pivot:
                pivot, tlist[i] = tlist[i], pivot
        # 基准值为最小值，将其添加到最后
        tlist.append(pivot)
        n -= 1
    # 循环完毕后还剩一个值，这是最大值，要添加到列表最后
    tlist.append(tlist.pop(0))
    return tlist


# 逻辑代码11行
if __name__ == '__main__':
    tlist = [17138, 15118, 13561, 14307, 19857, 19439, 12375, 13472, 15055, 18156, 19527, 12162, 9156, 10523, 19680,
             18237, 9967, 15655, 15478, 11036]
    print(selection_sort(tlist))
