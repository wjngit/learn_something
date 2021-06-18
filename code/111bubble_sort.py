def bubble_sort(li):
    n = len(li)
    for j in range(n - 1):
        for i in range(n - 1 - j):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]


def b_test(data):
    index = len(data) - 1
    for j in range(index):
        for i in range(index - j):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]


def d_test(data):
    n = len(data) - 1
    for j in range(n):
        for i in range(n - j):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
    pass


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(li)
    print(li)
    a_li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    d_test(a_li)
    print(a_li)
