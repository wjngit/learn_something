# 选择排序
def selection_sort(li):
    n=len(li)
    for j in range(n - 1):
        min_index = j
        for i in range(j,n - 1):
            if li[min_index] > li[i+1]:
                min_index = i+1
        if min_index !=j:

            li[min_index], li[j] = li[j], li[min_index]
if __name__ == '__main__':

    li = [54,26,93,17,77,31,44,55,20]
    selection_sort(li)
    print(li)