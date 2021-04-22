
# 插入排序
def insert_sort(li):
    n=len(li)
    for i in range(1,n):
        for j in range(i,0,-1):
            if li[j] <li[j-1]:
               li[j],li[j - 1]=li[j-1],li[j]
            else:
                break

alist = [54,26,93,17,77,31,44,55,20]
insert_sort(alist)
print(alist)