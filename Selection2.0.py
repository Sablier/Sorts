def selection_sort1(alist):
    n = len(alist)
    # 需要进行n-1次选择操作
    for i in range(n - 1):
        # 记录最小位置
        min_index = i
        # 从i+1位置到末尾选择出最小数据
        for j in range(i + 1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        # 如果选择出的数据不在正确位置，进行交换
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]


alist = [17138, 15118, 13561, 14307, 19857, 19439, 12375, 13472, 15055, 18156, 19527, 12162, 9156, 10523, 19680,
         18237, 9967, 15655, 15478, 11036]
selection_sort1(alist)
print(alist)


#-------------------------------------------------------------

def selection_sort(tlist):
    n = len(tlist) - 1
    while n > 0:
        pivot = tlist.pop(0)
        for i in range(n):
            if tlist[i] < pivot:
                pivot, tlist[i] = tlist[i], pivot
        tlist.append(pivot)
        n -= 1
    tlist.append(tlist.pop(0))
    return tlist


# 逻辑代码11行
if __name__ == '__main__':
    tlist = [17138, 15118, 13561, 14307, 19857, 19439, 12375, 13472, 15055, 18156, 19527, 12162, 9156, 10523, 19680,
             18237, 9967, 15655, 15478, 11036]
    print(selection_sort(tlist))
