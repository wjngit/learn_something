# 125.验证回文串
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例1:
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 解释："amanaplanacanalpanama" 是回文串
#
# 示例2:
# 输入: "race a car"
# 输出: false
# 解释："raceacar" 不是回文串
#
# 提示：
# 1 <= s.length <= 2 * 105
# 字符串 s 由 ASCII 字符组成
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #     i, j = 0, len(s) - 1
        #     while i < j:
        #         if not self.is_alpha(s[i]):
        #             i += 1
        #             continue
        #         if not self.is_alpha(s[j]):
        #             j -= 1
        #             continue
        #         if s[i].lower() != s[j].lower():
        #             return False
        #         i += 1
        #         j -= 1
        #     return True
        #
        # @staticmethod
        # def is_alpha(s):
        #     if "a" <= s <= "z" or "A" <= s <= "Z" or "0" <= s <= "9":
        #         return True
        #     return False

        pass


if __name__ == '__main__':
    s1 = "A man, a plan, a canal: Panama"
    s2 = "race a car"
    s3 = "0P"

    s = Solution()
    r1 = s.isPalindrome(s1)
    r2 = s.isPalindrome(s2)
    r3 = s.isPalindrome(s3)
    print(r1)
    print(r2)
    print(r3)
