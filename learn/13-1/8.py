# 判断一个字符串是否可以通过删除一个字母变成回文串

def func(s):
    n = len(s)
    i, j = 0, n - 1
    while i < j:
        if s[i] != s[j]:
            return check(s, i + 1, j) or check(s, i, j - 1)
        i += 1
        j -= 1
    return True


def check(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
