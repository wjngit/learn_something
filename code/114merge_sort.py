def merge_sort(li):
    n = len(li)
    if n == 1:
        return li
    mid = n // 2
    # split
    left_list, right_list = li[:mid], li[mid:]
    # sort
    left_sort, right_sort = merge_sort(left_list), merge_sort(right_list)
    # merge
    left_index, right_index, merge_list = 0, 0, []
    while left_index < len(left_sort) and right_index < len(right_sort):
        if left_sort[left_index] <= right_sort[right_index]:
            merge_list.append(left_sort[left_index])
            left_index += 1
        else:
            merge_list.append(right_sort[right_index])
            right_index += 1
    merge_list.extend(left_sort[left_index:])
    merge_list.extend(right_sort[right_index:])
    return merge_list


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
sorted_alist = merge_sort(alist)
print(sorted_alist)
