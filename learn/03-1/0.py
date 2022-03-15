# 三消

def aaa(s: str):
    stack = []
    for i in s:
        if not stack:
            stack.append((i, 1))
        else:
            data, count = stack[-1]
            if data != i:
                stack.append((i, 1))
            else:
                if count == 2:
                    stack.pop()
                else:
                    stack[-1] = (i, 2)
    print(stack)


if __name__ == '__main__':
    s1 = "abbbaac"
    s2 = "abbbc"
    print(aaa(s1))
    print(aaa(s2))
