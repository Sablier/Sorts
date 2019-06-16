def counting(tlist,tmin,tmax):

    offset = tmin

    # count_list记录每个数出现的次数，这是一个连续的数列，最大值到最小直接每一个整数都有一个位置。
    # 所以，tlist中一个数的值减去offset偏移值就是该数count_list的位置。
    count_list = [0 for i in range(tmax-tmin+1)]
    for each in tlist:
        count_list[each-offset] += 1
    # print('count_list is {}'.format(count_list))

    # sum_list 表示该数之前的数（如果该数在tlist中则包括自己）出现的次数
    sum_list = []
    sum_list.append(count_list[0])
    for i in range(1,len(count_list)):
        sum_list.append(sum_list[i-1] + count_list[i])
    # print('sum_list is {}'.format(sum_list))


    new_list = [0 for i in range(len(tlist))]
    tindex = len(tlist)-1
    while tindex >=0:
        num = tlist[tindex]
        new_index = sum_list[num-offset]-1
        new_list[new_index]=num
        sum_list[num-offset] -= 1
        tindex -= 1

    return new_list

if __name__ == '__main__':
    tlist = [16,19,31,103,19,25,19,25]
    print(counting(tlist,16,103))