def insert(tlist):
    pivot = 1

    while pivot < len(tlist):
        n = pivot  # 如果基准元素与有序列表元素比对交换了位置，那么基准元素的下标也要跟着改变。所以需要一个临时变量暂时储存
        for i in range(pivot, 0, -1):
            if tlist[n] < tlist[i - 1]:
                tlist[n], tlist[i - 1] = tlist[i - 1], tlist[n]
                n = i - 1  # 交换值同时也要改变临时基准的下标（这里直接减少基准也可以，但这样会从新的基准位置开始便利，重复排序）
        pivot += 1

    return tlist

    pass


if __name__ == '__main__':
    tlist = [14966, 11694, 16149, 13938, 16637, 17967, 16121, 8664, 13117, 13351, 13490, 12520, 12447, 14901, 8244,
             16926, 11243, 16378, 17788, 16279]
    print(insert(tlist))
