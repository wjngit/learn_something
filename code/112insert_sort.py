def insert_sort(li):
    n = len(li)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if li[j] < li[j - 1]:
                li[j], li[j - 1] = li[j - 1], li[j]
            else:
                break


def a_test(data):
    n = len(data)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]
            else:
                break


def b_test(data):
    for j in range(len(data)):
        for i in range(j, 0, -1):
            if data[i] < data[i - 1]:
                data[i], data[i - 1] = data[i - 1], data[i]
            else:
                break


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insert_sort(alist)
    print(alist)
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    b_test(a_list)
    print(a_list)
