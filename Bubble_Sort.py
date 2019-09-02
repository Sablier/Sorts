def bubble(context):
    print("the old array is %s" % context)

    n = 1
    while n < len(context):
        for i in range(len(context)-1):
            if context[i] > context[i + 1]:
                context[i], context[i + 1] = context[i + 1], context[i]
        n += 1

    print("the new array is %s " % context)


def bubble_sort(alist):
    for j in range(len(alist)-1,0,-1):
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


if __name__ == '__main__':
    context = [18422, 15669, 9854, 12705, 18350, 19424, 9072, 14817, 11030, 16525]
    bubble(context)
    bubble_sort(context)