# 面试题 16.02. 单词频率
#
# 设计一个方法，找出任意指定单词在一本书中的出现频率。
# 你的实现应该支持如下操作：
#     WordsFrequency(book)构造函数，参数为字符串数组构成的一本书
#     get(word)查询指定单词在书中出现的频率
#
# 示例：
#     WordsFrequency wordsFrequency = new WordsFrequency({"i", "have", "an", "apple", "he", "have", "a", "pen"});
#     wordsFrequency.get("you"); //返回0，"you"没有出现过
#     wordsFrequency.get("have"); //返回2，"have"出现2次
#     wordsFrequency.get("an"); //返回1
#     wordsFrequency.get("apple"); //返回1
#     wordsFrequency.get("pen"); //返回1
#
# 提示：
#     book[i]中只包含小写字母
#     1 <= book.length <= 100000
#     1 <= book[i].length <= 10
#     get函数的调用次数不会超过100000


from typing import List


class WordsFrequency:
    def __init__(self, book: List[str]):
        # self.book = {}
        # for data in book:
        #     if data in self.book:
        #         self.book[data] += 1
        #     else:
        #         self.book[data] = 1

        pass

    def get(self, word: str) -> int:
        # if word not in self.book:
        #     return 0
        # return self.book[word]

        pass


# Your WordsFrequency object will be instantiated and called as such:
# obj = WordsFrequency(book)
# param_1 = obj.get(word)

if __name__ == '__main__':
    # TODO: 还可以排序法解决，相同在一起，利用二分查找开始和结束索引
    # TODO: 暴力解法，列表不处理直接找
    data = ["i", "have", "an", "apple", "he", "have", "a", "pen"]
    t1 = "you"
    t2 = "have"
    t3 = "an"
    t4 = "apple"
    t5 = "pen"

    s = WordsFrequency(data)
    r1 = s.get(t1)
    r2 = s.get(t2)
    r3 = s.get(t3)
    r4 = s.get(t4)
    r5 = s.get(t5)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
