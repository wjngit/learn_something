def shell_sort(li):

    n=len(li)
    gap=n//2

    while gap>0:

        # for i in range(gap, n):
        #     for j in range(i, 0, -gap):
        #         if li[j] < li[j - gap]:
        #             li[j], li[j - gap] = li[j - gap], li[j]
        #         elif j-gap<0:
        #             break
        #         else:
        #             break

        for i in range(gap,n):
            while i>=gap and li[i] < li[i - gap]:
                li[i], li[i - gap] = li[i - gap], li[i]
                i-=gap
        gap=gap//2
alist = [54,26,93,17,77,31,44,55,20]
shell_sort(alist)
print(alist)