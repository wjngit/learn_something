# 1108.IP 地址无效化
#
# 给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。
# 所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。
#
# 示例1：
# 输入：address = "1.1.1.1"
# 输出："1[.]1[.]1[.]1"
#
# 示例2：
# 输入：address = "255.100.50.0"
# 输出："255[.]100[.]50[.]0"
#
# 提示：
# 给出的 address 是一个有效的 IPv4 地址

class Solution:
    def defangIPaddr(self, address: str) -> str:
        # new_str = ""
        # for i in address:
        #     if i != ".":
        #         new_str += i
        #     else:
        #         new_str += "[.]"
        # return new_str

        pass

        # temp = []
        # for i in address:
        #     if i != ".":
        #         temp.append(i)
        #     else:
        #         temp.append("[.]")
        # return "".join(temp)

        pass


if __name__ == '__main__':
    address1 = "1.1.1.1"
    address2 = "255.100.50.0"

    s = Solution()
    r1 = s.defangIPaddr(address1)
    r2 = s.defangIPaddr(address2)
    print(r1)
    print(r2)
