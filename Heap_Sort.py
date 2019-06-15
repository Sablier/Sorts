def adjust_heap(tlist, n):
    """最后一个非叶子节点和其子节点的一次调整"""

    # 如果子节点存在两个，则取出较小值；如果只有左边的子节点，则取出左边的值
    child_left = 2 * n + 1
    if 2 * n + 2 <= len(tlist) - 1:  # 判断最后一个非叶子节点的右子节点是否存在
        child_right = 2 * n + 2
        if tlist[child_left] < tlist[child_right]:  # 取出两个子节点中较小的
            child = child_left
        else:
            child = child_right
    else:
        child = child_left

    if tlist[n] > tlist[child]:  # 如果最后一个非叶子节点比他的子节点要打，则需要变换位置
        tlist[n], tlist[child] = tlist[child], tlist[n]

        # 非叶子节点变换位置（下沉）以后，需要判断它时候下沉到了叶子节点上，如果没有，则需要再做一次判断
        # 只有进入if说明原来的非叶子节点发生了下沉，需要判断其是否下沉到了低端
        pivot_pos = child
    else:
        # 如果pivt的位置没有发生改变，则说明pivot已经位于合适的位置，不需要再调整
        pivot_pos = None

    return (tlist, pivot_pos)


def build_min_heap(tlist):
    """构建小顶堆"""

    if len(tlist) == 1:
        return tlist

    last_unleaf_pos = (len(tlist) - 2) // 2  # 最后一个非叶子节点在列表中的下标为(len-2)/2

    n = last_unleaf_pos
    while n >= 0:  # 从最后一个非叶子节点开始，判断每一个非叶子节点与其子节点的大小。下沉非叶子节点。
        pivot_pos = n
        while pivot_pos is not None and pivot_pos <= last_unleaf_pos:  # 利用pos的值来判断最后一个非叶子节点时候下沉到叶子节点上
            tlist, pivot_pos = adjust_heap(tlist, n)
        n -= 1

    return tlist


def heap_sort(tlist):
    """利用小顶堆构建有序序列"""

    new_list = []

    for i in range(len(tlist)): # 每次只取出一个元素，所以有多少个元素就要构建多少次小顶堆
        tlist = build_min_heap(tlist)
        tlist[0], tlist[-1] = tlist[-1], tlist[0] # 交换小顶堆中顶元素和底元素的位置，避免取出元素时破坏顶推的结构
        new_list.append(tlist.pop(-1))

    return new_list


if __name__ == '__main__':
    tlist = [46945, 94637, 70787, 97814, 29324, 97355, 66297, 8293, 22482, 52567, 6468, 78604, 88364, 59805, 50225,
             4951, 41458, 91457, 64805, 58332]
    print(heap_sort(tlist))


    # 编码耗时约为2小时, 逻辑代码共34行
