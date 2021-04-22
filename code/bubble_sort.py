# 冒泡排序

def bubble_sort(li):
    n=len(li)
    for j in range(n - 1):
        for i in range(n - 1-j):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]

if __name__ == '__main__':

    li = [54,26,93,17,77,31,44,55,20]
    bubble_sort(li)
    print(li)