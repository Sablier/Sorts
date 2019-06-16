def insert(tlist):
    pivot = 1

    while pivot < len(tlist):
        n = pivot     # 由于
        for i in range(pivot, 0, -1):
            if tlist[n] < tlist[i - 1]:
                tlist[n], tlist[i - 1] = tlist[i - 1], tlist[n]
                n = i - 1
        pivot += 1

    return tlist

    pass


if __name__ == '__main__':
    tlist = [14966, 11694, 16149, 13938, 16637, 17967, 16121, 8664, 13117, 13351, 13490, 12520, 12447, 14901, 8244,
             16926, 11243, 16378, 17788, 16279]
    print(insert(tlist))
