# x瓶酒，3个瓶换一瓶，7个盖换一瓶
class Solution:
    def a(self, x):
        # count = k1 = k2 = x
        # while k1 >= 3 or k2 >= 7:
        #     while k1 >= 3:
        #         change1 = k1 // 3
        #         count += change1
        #         k1 %= 3
        #         k1 += change1
        #         k2 += change1
        #
        #     while k2 >= 7:
        #         change2 = k2 // 7
        #         count += change2
        #         k2 %= 7
        #         k1 += change2
        #         k2 += change2
        # return count

        pass


if __name__ == '__main__':
    n = 10  # 17
    s = Solution()
    ret = s.a(10)
    print(ret)
