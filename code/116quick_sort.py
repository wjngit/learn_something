def remark(li, start, end):
    mid = li[start]
    if start >= end:
        return
    left = start
    right = end
    while left < right:
        while left < right and li[right] >= mid:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] < mid:
            left += 1
        li[right] = li[left]

    li[left] = mid

    remark(li, start, left - 1)
    remark(li, left + 1, end)


def a_test(data, start, end):
    if start >= end:
        return data
    mid = data[start]
    low = start
    high = end
    while low < high:
        if data[high] >= mid:
            high -= 1
        data[low] = data[high]
        if data[low] < mid:
            low += 1
        data[high] = data[low]
    data[low] = mid
    a_test(data, start, low - 1)
    a_test(data, low + 1, end)


def d_test(data, start, end):
    if start >= end:
        return
    mid = data[start]
    low, high = start, end
    while low < high:
        if data[high] >= mid:
            high -= 1
        data[low] = data[high]
        if data[low] < mid:
            low += 1
        data[high] = data[low]
    data[low] = mid
    d_test(data, start, low - 1)
    d_test(data, low + 1, end)


def c_test(data, start, end):
    if start >= end:
        return
    mid = data[start]
    low, high = start, end
    while low < high:
        if data[high] >= mid:
            high -= 1
        data[low] = data[high]
        if data[low] < mid:
            low += 1
        data[high] = data[low]
    data[low] = mid
    c_test(data, start, low - 1)
    c_test(data, low + 1, end)


if __name__ == '__main__':
    # data_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # remark(data_list, 0, len(data_list) - 1)
    # print(data_list)

    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(a_list)
    c_test(a_list, 0, len(a_list) - 1)
    print(a_list)

    # b_list = [54, 26, 93]
    # a_test(b_list, 0, len(b_list) - 1)
    # print(b_list)
    # a = 001
    # b = 010
    # c = 100
    # a = 1
    # b = 2
    # c = 4
    # print(a&c)
    # print(a|c)
    # print(a^c)
    # print(~c)
