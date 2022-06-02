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

# diff = ord("a") - ord("A")
# print(diff)
# s = "M"
# res = chr(ord(s) + diff)
# print(res)

"""
给定一个字符串表示IP地址，比如”192.92.4.3“，判断其合法性。合法ip地址规则如下：
a.除了空格、数字和 . 之外，不得包含其他字符；
b.IP地址由四个数字构成，由 . 分隔，每个 . 隔开的数字大小在0~255之间；
c.数字前后可以有空格，但中间不能有空格
d.每个数字不能有前导0，但是可以为0
"""


def check(ip: str):
    if not ip:
        return False
    ip_segments = ip.split('.')
    if len(ip_segments) != 4:
        return False
    for i in range(4):
        if check_segment(ip_segments[i]) is False:
            return False
    return True


def check_segment(ip_segment):
    # 前导空格判断
    n = len(ip_segment)
    i = 0
    while i < n and ip_segment[i] == ' ':
        i += 1
    if i == n:
        return False

    # 转化为数字及条件判断
    num = 0
    front_is_zero, flag = False, False
    while i < n and ip_segment[i] != ' ':
        c = ip_segment[i]
        # 非数字判断
        if c < '0' or c > '9':
            return False

        # 前导0的判断
        if flag is False:
            flag = True
            if c == '0':
                front_is_zero = True
        else:
            if c != '0' and front_is_zero is True:
                return False

        # 大于255判断
        num = num * 10 + int(c)
        if num > 255:
            return False

        i += 1

    # 后置空格处理
    while i < n:
        c = ip_segment[i]
        if c != ' ':
            return False
        i += 1

    return True


if __name__ == '__main__':
    t1 = '123.9.2.000'
    t2 = ' 123. 9 .2 . 0 '
    t3 = ' 12 3. 9 .2 . 0 '
    t4 = ' 123. 999 .2 . 0 '
    t5 = ' 123. 9AB .2 . 0 '
    t6 = ' 123. 9 .2 . 0 .12'
    t7 = ' 123. 9 .2 '
    t8 = ''
    t9 = ' 123. 09 .2 .1'

    r1 = check(t1)
    r2 = check(t2)
    r3 = check(t3)
    r4 = check(t4)
    r5 = check(t5)
    r6 = check(t6)
    r7 = check(t7)
    r8 = check(t8)
    r9 = check(t9)

    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
    print(r6)
    print(r7)
    print(r8)
    print(r9)
