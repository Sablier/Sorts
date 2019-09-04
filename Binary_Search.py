def binary(tlist, item):
    if len(tlist) == 0:
        return None

    mid_index = len(tlist) // 2

    if item == tlist[mid_index]:
        return True

    elif item > tlist[mid_index]:
        return binary(tlist[mid_index + 1:], item)

    else:
        return binary(tlist[:mid_index], item)


def binary_search(tlist, item):
    left = 0
    right = len(tlist) - 1

    while left <= right:

        mid_index = (left + right) // 2

        if tlist[mid_index] == item:
            return mid_index

        elif item < tlist[mid_index]:
            right = mid_index - 1

        else:
            left = mid_index + 1


if __name__ == '__main__':
    tlist = [1, 2, 3, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 20]
    target = 11
    print(binary(tlist, target))
    print(binary_search(tlist, target))
