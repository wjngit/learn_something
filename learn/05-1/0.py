# 二分查找算法
def b_search(data, target):
    n = len(data)
    left, right = 0, n - 1
    while left <= right:
        mid = left + (right - left) // 2

        # # todo: 第一个等于x的元素
        # if data[mid] > target:
        #     right = mid - 1
        # elif data[mid] < target:
        #     left = mid + 1
        # else:
        #     if mid == 0 or data[mid - 1] != target:
        #         return mid
        #     right = mid - 1

        pass

        # # todo: 最后一个等于x的元素
        # if data[mid] == target:
        #     if mid == len(data) - 1 or data[mid + 1] != target:
        #         return mid
        #     left = mid + 1
        # elif data[mid] > target:
        #     right = mid - 1
        # else:
        #     left = mid + 1

        pass

        # # todo: 第一个大于等于x的元素
        # if data[mid] >= target:
        #     if mid == 0 or data[mid - 1] < target:
        #         return mid
        #     right = mid - 1
        # else:
        #     left = mid + 1

        pass

        # # todo: 最后一个小于等于x的元素
        # if data[mid] <= target:
        #     if mid == len(data) - 1 or data[mid + 1] > target:
        #         return mid
        #     left = mid + 1
        # else:
        #     right = mid - 1

        pass

        # todo: 第一个等于x的元素
        # todo: 最后一个等于x的元素
        # todo: 第一个大于等于x的元素
        # todo: 最后一个小于等于x的元素

    return -1


if __name__ == '__main__':
    a_list = [17, 20, 26, 31, 44, 54, 55, 77, 77, 77, 93]
    print(a_list, "*" * 5)
    print(b_search(a_list, 13))
    print(b_search(a_list, 77))
    print(b_search(a_list, 31))
    print(b_search(a_list, 93))
    print('-' * 50)
