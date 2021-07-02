import base64
from Crypto.Cipher import AES
import time
import json
import hashlib
import dis
import re
import pylru
from numpy import iterable
import os
import psutil


class AESCipher():
    """
    Usage:
        c = AESCipher('password').encrypt('message')
        m = AESCipher('password').decrypt(c)
    Tested under Python 3 and PyCrypto 2.6.1.
    """

    def __init__(self, key):
        self.key = hashlib.md5(key.encode('utf8')).hexdigest()

        # Padding for the input string --not
        # related to encryption itself.
        self.BLOCK_SIZE = 32  # Bytes
        self.pad = lambda s: s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) * \
                             chr(self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE)
        self.unpad = lambda s: s[:-ord(s[len(s) - 1:])]

    # 加密
    def encrypt(self, raw):
        raw = self.pad(raw)
        cipher = AES.new(self.key, AES.MODE_ECB)
        return base64.b64encode(cipher.encrypt(raw))

    # 解密，针对微信用此方法即可
    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        print(enc)
        cipher = AES.new(self.key, AES.MODE_ECB)
        print(cipher)
        return self.unpad(cipher.decrypt(enc)).decode('utf8')


class SearchEngineBase(object):
    def __init__(self):
        pass

    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    def process_corpus(self, id, text):
        raise Exception('process_corpus not implemented.')

    def search(self, query):
        raise Exception('search not implemented.')


class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}

    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text

    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results


class BOWEngine(SearchEngineBase):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_words = {}

    def process_corpus(self, id, text):
        self.__id_to_words[id] = self.parse_text_to_words(text)

    def search(self, query):
        query_words = self.parse_text_to_words(query)
        results = []
        for id, words in self.__id_to_words.items():
            if self.query_match(query_words, words):
                results.append(id)
        return results

    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word not in words:
                return False
        return True

    @staticmethod
    def parse_text_to_words(text):
        return set(filter(None, re.sub(r'[^\w ]', ' ', text).lower().split(' ')))


class BOWInvertedIndexEngine(SearchEngineBase):
    def __init__(self):
        super(BOWInvertedIndexEngine, self).__init__()
        self.inverted_index = {}

    def process_corpus(self, id, text):
        words = self.parse_text_to_words(text)
        for word in words:
            if word not in self.inverted_index:
                self.inverted_index[word] = []
            self.inverted_index[word].append(id)

    def search(self, query):
        query_words = list(self.parse_text_to_words(query))
        query_words_index = list()  # 全为0的列表
        for query_word in query_words:
            query_words_index.append(0)

        # 如果某一个查询单词的倒序索引为空，我们就立刻返回
        for query_word in query_words:
            if query_word not in self.inverted_index:
                return []

        result = []
        while True:

            # 首先，获得当前状态下所有倒序索引的 index
            current_ids = []

            for idx, query_word in enumerate(query_words):
                current_index = query_words_index[idx]  # 0
                current_inverted_list = self.inverted_index[query_word]  # 文件id列表

                # 已经遍历到了某一个倒序索引的末尾，结束 search
                if current_index >= len(current_inverted_list):
                    return result

                current_ids.append(current_inverted_list[current_index])

            # 然后，如果 current_ids 的所有元素都一样，那么表明这个单词在这个元素对应的文档中都出现了
            if all(x == current_ids[0] for x in current_ids):
                result.append(current_ids[0])
                query_words_index = [x + 1 for x in query_words_index]
                continue

            # 如果不是，我们就把最小的元素加一
            min_val = min(current_ids)
            min_val_pos = current_ids.index(min_val)
            query_words_index[min_val_pos] += 1

    @staticmethod
    def parse_text_to_words(text):
        return set(filter(None, re.sub(r'[^\w ]', ' ', text).lower().split(' ')))


class LRUCache(object):
    def __init__(self, size=32):
        self.cache = pylru.lrucache(size)

    def has(self, key):
        return key in self.cache

    def get(self, key):
        return self.cache[key]

    def set(self, key, value):
        self.cache[key] = value


class BOWInvertedIndexEngineWithCache(BOWInvertedIndexEngine, LRUCache):
    def __init__(self):
        super(BOWInvertedIndexEngineWithCache, self).__init__()
        LRUCache.__init__(self)

    def search(self, query):
        if self.has(query):
            print('cache hit!')
            return self.get(query)

        result = super(BOWInvertedIndexEngineWithCache, self).search(query)
        self.set(query, result)

        return result


def main(search_engine):
    for file_path in ['1.txt']:
        search_engine.add_corpus(file_path)

    while True:
        query = input()
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)


if __name__ == '__main__':
    # search_engine = BOWInvertedIndexEngine()
    # main(search_engine)
    # search_engine = BOWInvertedIndexEngineWithCache()
    # main(search_engine)
    # query_words = ['1', '2', '3']
    # b = enumerate(query_words)
    # print(b)
    # for i in b:
    #     # print(i)
    #     # print(n)
    #     print(i)

    # 显示当前 python 程序占用的内存大小

    # import asyncio
    # import aiohttp
    # import time
    #
    #
    # async def download_one(url):
    #     async with aiohttp.ClientSession() as session:
    #         async with session.get(url) as resp:
    #             print('Read {} from {}'.format(resp.content_length, url))
    #
    #
    # async def download_all(sites):
    #     tasks = [asyncio.create_task(download_one(site)) for site in sites]
    #     await asyncio.gather(*tasks)
    #
    #
    # def main():
    #     sites = [
    #         'https://en.wikipedia.org/wiki/Portal:Arts',
    #         'https://en.wikipedia.org/wiki/Portal:History',
    #         'https://en.wikipedia.org/wiki/Portal:Society',
    #         'https://en.wikipedia.org/wiki/Portal:Biography',
    #         'https://en.wikipedia.org/wiki/Portal:Mathematics',
    #         'https://en.wikipedia.org/wiki/Portal:Technology',
    #         'https://en.wikipedia.org/wiki/Portal:Geography',
    #         'https://en.wikipedia.org/wiki/Portal:Science',
    #         'https://en.wikipedia.org/wiki/Computer_science',
    #         'https://en.wikipedia.org/wiki/Python_(programming_language)',
    #         'https://en.wikipedia.org/wiki/Java_(programming_language)',
    #         'https://en.wikipedia.org/wiki/PHP',
    #         'https://en.wikipedia.org/wiki/Node.js',
    #         'https://en.wikipedia.org/wiki/The_C_Programming_Language',
    #         'https://en.wikipedia.org/wiki/Go_(programming_language)'
    #     ]
    #     start_time = time.perf_counter()
    #     asyncio.run(download_all(sites))
    #     end_time = time.perf_counter()
    #     print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))
    #
    #
    # if __name__ == '__main__':
    #     main()

    # import objgraph
    #
    # a = [1, 2, 3]
    # b = [4, 5, 6]
    #
    # a.append(b)
    # b.append(a)
    #
    # objgraph.show_refs([a])

    # def solve(a_l, tt):
    #     ret = [i for i in a_l if i ** 2 > tt]
    #     if ret:
    #         # a = sorted(ret)
    #         ret.sort()
    #         # print(a)
    #         return ret[0]
    #     else:
    #         return -1

    # def solve(arr, target):
    #     l, r = 0, len(arr) - 1
    #     ret = -1
    #     while l <= r:
    #         m = (l + r) // 2
    #         if arr[m] * arr[m] > target:
    #             ret = m
    #             r = m - 1
    #         else:
    #             l = m + 1
    #     if ret == -1:
    #         return -1
    #     else:
    #         return arr[ret]
    #
    #
    # print(solve([1, 2, 3, 4, 5, 6], 8))
    # # print(solve([1, 2, 3, 4, 5, 6], 9))
    # # print(solve([1, 2, 3, 4, 5, 6], 0))
    # print(solve([1, 2, 3, 4, 5, 6, 7], 40))
    # # print(84.08 / 12.99)
    # # print(390.25 / 59.99)
    # # print(12.99 * (390.25 / 59.99) * 12)
    # # print(85 * 12)
    # # assert 1 == 2, 'wozhidao'
    # # raise AssertionError('123')
    # # if __debug__:
    # #     print(123)
    #
    # def aaaaa(arr, target):
    #     l, r = 0, len(arr) - 1
    #     ret = -1
    #     while l <= r:
    #         m = (l + r) // 2
    #         if arr[m] ** 2 > target:
    #             r = m - 1
    #             ret = m
    #         else:
    #             l = m + 1

    import unittest


    # # 将要被测试的排序函数
    # def sort(arr):
    #     l = len(arr)
    #     for i in range(0, l):
    #         for j in range(i + 1, l):
    #             if arr[i] >= arr[j]:
    #                 tmp = arr[i]
    #                 arr[i] = arr[j]
    #                 arr[j] = tmp
    #
    #
    # # 编写子类继承unittest.TestCase
    # class TestSort(unittest.TestCase):
    #
    #     # 以test开头的函数将会被测试
    #     def test_sort(self):
    #         arr = [3, 4, 1, 5, 6]
    #         sort(arr)
    #         # assert 结果跟我们期待的一样
    #         self.assertEqual(arr, [1, 3, 4, 5, 6])
    #
    #
    # # if __name__ == '__main__':
    # #     ## 如果在Jupyter下，请用如下方式运行单元测试
    # #     unittest.main(argv=['first-arg-is-ignored'], exit=False)
    # #
    # # 如果是命令行下运行，则：
    # unittest.main()

    # import unittest
    from unittest.mock import MagicMock, patch


    class A(unittest.TestCase):
        def m1(self):
            val = self.m2()
            self.m3(val)

        def m2(self):
            pass

        def m3(self, val):
            pass

        def test_m1(self):
            a = A()
            a.m2 = MagicMock(return_value="custom_val111")
            a.m3 = MagicMock()
            a.m1()
            self.assertTrue(a.m2.called)  # 验证m2被call过
            a.m3.assert_called_with("custom_val111")  # 验证m3被指定参数call过


    # unittest.main()
    import cProfile
    # def fib(n):
    #     if n == 0:
    #         return 0
    #     elif n == 1:
    #         return 1
    #     else:
    #         return fib(n - 1) + fib(n - 2)
    #
    #
    # def fib_seq(n):
    #     res = []
    #     # if n > 0:
    #     #     res.extend(fib_seq(n - 1))
    #     # print(res)
    #     res.append(fib(n))
    #     return res


    def memoize(f):
        memo = {}

        def helper(x):
            if x not in memo:
                memo[x] = f(x)
            return memo[x]

        return helper


    @memoize
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)


    def fib_seq(n):
        res = []
        if n > 0:
            res.extend(fib_seq(n - 1))
        res.append(fib(n))
        return res


    # fib_seq(30)


    # a = fib_seq(30)
    # print(a)
    # cProfile.run('fib_seq(30)')
    # import datetime
    # t = datetime.datetime.now()
    # print(t)
    # t1 = t.timetuple()
    # print(t1)
    # t2 = time.mktime(t1)
    # print(t2)
    # payload_nonce = str(int(t2 * 1000))
    # print(payload_nonce)
    # filepath = os.path.join(os.path.dirname(__file__), '1.txt')
    print(os.path.dirname(__file__))
    print(os.path.abspath(__file__))
    filepath = os.path.join(os.path.dirname(__file__), 'urls.py')
    print(filepath)
    # __CURDIR__ = os.path.dirname(os.path.abspath(__file__))
    # third_party_path = os.path.join(__CURDIR__, 'third_party')
    # sys.path.append(third_party_path)
    """
    before await
    worker_1 start
    worker_2 start
    worker_1 done
    awaited worker_1
    worker_2 done
    awaited worker_2
    
    asyncio.run(main())，程序进入 main() 函数，事件循环开启；
    task1 和 task2 任务被创建，并进入事件循环等待运行；运行到 print，输出 'before await'；
    await task1 执行，用户选择从当前的主任务中切出，事件调度器开始调度 worker_1；
    worker_1 开始运行，运行 print 输出'worker_1 start'，然后运行到 await asyncio.sleep(1)， 从当前任务切出，事件调度器开始调度 worker_2；
    worker_2 开始运行，运行 print 输出 'worker_2 start'，然后运行 await asyncio.sleep(2) 从当前任务切出；
    以上所有事件的运行时间，都应该在 1ms 到 10ms 之间，甚至可能更短，事件调度器从这个时候开始暂停调度；
    一秒钟后，worker_1 的 sleep 完成，事件调度器将控制权重新传给 task_1，输出 'worker_1 done'，task_1 完成任务，从事件循环中退出；
    await task1 完成，事件调度器将控制器传给主任务，输出 'awaited worker_1'，·然后在 await task2 处继续等待；
    两秒钟后，worker_2 的 sleep 完成，事件调度器将控制权重新传给 task_2，输出 'worker_2 done'，task_2 完成任务，从事件循环中退出；
    主任务输出 'awaited worker_2'，协程全任务结束，事件循环结束。
    """

    pass
