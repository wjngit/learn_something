def selection_sort(li):
    n = len(li)
    for j in range(n - 1):
        min_index = j
        for i in range(j, n - 1):
            if li[min_index] > li[i + 1]:
                min_index = i + 1
        if min_index != j:
            li[min_index], li[j] = li[j], li[min_index]


def a_test(data):
    n = len(data) - 1
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if data[min_index] > data[j + 1]:
                min_index = j + 1
        if min_index != i:
            data[min_index], data[i] = data[i], data[min_index]


def c_test(data):
    n = len(data) - 1
    for i in range(n):
        min_ = i
        for j in range(i, n):
            if data[min_] > data[j + 1]:
                min_ = j + 1
        if min_ != i:
            data[min_], data[i] = data[i], data[min_]


def d_test(data):
    n = len(data) - 1
    for i in range(n):
        min_ = i
        for j in range(i, n):
            if data[min_] > data[j + 1]:
                min_ = j + 1
        if min_ != i:
            data[min_], data[i] = data[i], data[min_]


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(li)
    print(li)

    a_li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    c_test(a_li)
    print(a_li)
