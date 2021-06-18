# 递归实现二分查找
def binary_search(li, data):
    n = len(li)
    if n <= 0:
        return False
    mid = n // 2
    if li[mid] == data:
        return True
    elif li[mid] > data:
        return binary_search(li[:mid], data)
    else:
        return binary_search(li[mid + 1:], data)


# while 实现二分查找
def binary_search2(li, data):
    start = 0
    end = len(li) - 1
    while start <= end:
        mid = (start + end) // 2
        if li[mid] == data:
            return True
        elif li[mid] > data:
            end = mid - 1
        else:
            start = mid + 1
    return False


def binary_search3(li, data):
    left, right = 0, len(li) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if li[mid] == data:
            return mid
        elif li[mid] > data:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def test(li, data):
    left, right = 0, len(li) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if li[mid] == data:
            return mid
        elif li[mid] > data:
            right = mid - 1
        else:
            left = mid + 1
    return -1


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, 99]
# print(binary_search2(testlist, 3))
# print(binary_search2(testlist, 13))
# print(binary_search3(testlist, 99))
print(test(testlist, 991))
