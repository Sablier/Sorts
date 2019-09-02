def selection_sort(tlist):
    # 共执行n-1轮选择
    n = len(tlist) - 1

    while n > 0:
        # 取出基准
        pivot = tlist.pop(0)
        # 遍历列表，如果找到比基准小的值则和基准交换
        for i in range(n):
            if tlist[i] < pivot:
                pivot, tlist[i] = tlist[i], pivot
        # 基准值为最小值，将其添加到最后
        tlist.append(pivot)
        n -= 1
    # 循环完毕后还剩一个值，这是最大值，要添加到列表最后
    tlist.append(tlist.pop(0))

    return tlist


def select_sort(li):

    n = len(li)

    # 选择的次数，n-1次，每一次选择一个最小的数，依次放到0~ n-1 位置
    for j in range(n-1):

        # 选择一次，把最小的数放到0位置
        # 认为0位置的数据最小，记录0位置
        min_index = j
        # 那最小的数，跟后面所有的数据进行比较
        for i in range(1+j, n):
            # 拿最小的数跟当前位置的数比较，让min_index 记录最小的数的位置
            if li[i] < li[min_index]:
                min_index = i
        # for循环结束，min_index指向最小的数
        li[min_index], li[j] = li[j], li[min_index]

    return li


# 逻辑代码11行
if __name__ == '__main__':
    tlist = [17138, 15118, 13561, 14307, 19857, 19439, 12375, 13472, 15055, 18156, 19527, 12162, 9156, 10523, 19680,
             18237, 9967, 15655, 15478, 11036]
    print(selection_sort(tlist))
    print(select_sort(tlist))
