# 49. 字母异位词分组
#
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
# 字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。
#
# 示例 1:
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# 示例 2:
# 输入: strs = [""]
# 输出: [[""]]
#
# 示例 3:
# 输入: strs = ["a"]
# 输出: [["a"]]
#
# 提示：
#     1 <= strs.length <= 10^4
#     0 <= strs[i].length <= 100
#     strs[i] 仅包含小写字母


from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # temp_dict = {}
        # for i in strs:
        #     str_list = list(i)
        #     str_list.sort()
        #     new_str = "".join(str_list)
        #     if new_str in temp_dict:
        #         temp_dict[new_str].append(i)
        #     else:
        #         temp_dict[new_str] = [i]
        # return list(temp_dict.values())

        pass


if __name__ == '__main__':
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs2 = [""]
    strs3 = ["a"]

    s = Solution()
    r1 = s.groupAnagrams(strs1)
    r2 = s.groupAnagrams(strs2)
    r3 = s.groupAnagrams(strs3)
    print(r1)
    print(r2)
    print(r3)
