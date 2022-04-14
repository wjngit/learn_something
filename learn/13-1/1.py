# 1. 三个同样的字母连在一起，一定是拼写错误，去掉一个的就好啦：比如 helllo -> hello
# 2. 两对一样的字母（AABB型）连在一起，一定是拼写错误，去掉第二对的一个字母就好啦：比如 helloo -> hello
# 3. 上面的规则优先“从左到右”匹配，即如果是AABBCC，虽然AABB和BBCC都是错误拼写，应该优先考虑修复AABB，结果为AABCC


def func(s):
    n = len(s)
    if n < 3:
        return s
    res = []
    i = 0
    k = 0
    while i < n:
        if i < 2:
            res.append(s[i])
            k += 1
            i += 1
            continue
        if s[i] == res[k - 1] and s[i] == res[k - 2]:
            i += 1
            continue
        if i >= 3 and s[i] == res[k - 1] and res[k - 2] == res[k - 3]:
            i += 1
            continue
        res.append(s[i])
        i += 1
        k += 1
    return "".join(res)


if __name__ == '__main__':
    a = "helloo"
    b = "wooooooow"
    print(func(a))  # hello
    print(func(b))  # woow
