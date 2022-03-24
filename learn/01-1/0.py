# ip地址无效化 复杂的
# 1、空判断
# 2、切分，长度为4判断
# 3、4个循环判断
# 3-1、前导空格判断，全为空格不行
# 3-2、数字判断，大于255不行
# 3-3、后面空格判断，后面不全为空格不行

# 第一个小于n的2的平方数
# m = 1
# while m < n:
#     m *= 2
# 复杂度logn

diff = ord("a") - ord("A")
print(diff)
s = "M"
res = chr(ord(s) + diff)
print(res)
