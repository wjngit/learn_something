def quick_sort(li,start,end):

    mid=li[start]
    if start>=end:
        return
    left=start
    right=end
    while left<right:
        while left<right and li[right]>=mid:
            right-=1
        li[left]=li[right]
        while left<right and li[left]<mid:
            left+=1
        li[right]=li[left]

    li[left]=mid

    quick_sort(li,start,left-1)
    quick_sort(li,left+1,end)

alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist,0,len(alist)-1)
print(alist)


