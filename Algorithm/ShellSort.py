def shell(tlist):
    gap = len(tlist) // 2

    # 让步长由大变小，最后变为1
    while gap >= 1:

        # 从步长位置，向后遍历
        for i in range(gap, len(tlist)):
            while i - gap >= 0:
                if tlist[i] < tlist[i - gap]:
                    tlist[i], tlist[i - gap] = tlist[i - gap], tlist[i]
                i -= gap

        gap = gap // 2

    return tlist


if __name__ == '__main__':
    tlist = [135131, 174808, 160466, 90196, 164039, 85764, 150413, 170484, 13931, 52800]
    print(shell(tlist))
