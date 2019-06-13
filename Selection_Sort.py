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