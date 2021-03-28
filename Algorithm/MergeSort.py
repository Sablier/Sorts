def merge_sort(list):

    # 确定中间数，进行分组
    mid_pos = len(list) // 2

    sub_1 = list[:mid_pos]
    sub_2 = list[mid_pos:]

    # 进入分组递归
    if len(sub_1) > 2:
        sub_1 = merge_sort(sub_1)
    elif len(sub_1) == 2:
        if sub_1[0] > sub_1[1]:
            sub_1[0], sub_1[1] = sub_1[1], sub_1[0]

    if len(sub_2) > 2:
        sub_2 = merge_sort(sub_2)
    elif len(sub_2) == 2:
        if sub_2[0] > sub_2[1]:
            sub_2[0], sub_2[1] = sub_2[1], sub_2[0]

    # 开始合并
    # 每次抽出两组的第一个数，将较小的那一个放入新的队列中
    new_list = []
    for i in range(len(sub_2) + len(sub_2)):
        if sub_1 == []:
            new_list += sub_2
            break
        if sub_2 == []:
            new_list += sub_1
            break
        if sub_1[0] < sub_2[0]:
            item = sub_1.pop(0)
            new_list.append(item)
        else:
            item = sub_2.pop(0)
            new_list.append(item)

    return new_list


# 代码逻辑共29行
if __name__ == '__main__':
    list = [19088, 13300, 17130, 19114, 11742, 18950, 17451, 16169, 18972, 8042, 15652, 16305, 14199, 9146, 14849,
            17600, 14101, 17036, 10981, 8979]
    print(merge_sort(list))
