# -*- coding: utf-8 -*-

"""
@Time    : 2021/5/21 8:22 下午
@Author  : Garner
@File    : test_5.py
"""
import time
import hmac
import base64
import hashlib
import requests


def send_ding_ding():
    ding_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/cb674e03-ceda-4e54-81ce-fde83d2fd661'
    timestamp = str(round(time.time()))
    secret = "02T6THmyutiomvb6MCeiyg"

    key = f'{timestamp}\n{secret}'
    key_enc = key.encode('utf-8')
    msg = ""
    msg_enc = msg.encode('utf-8')
    hmac_code = hmac.new(key_enc, msg_enc, digestmod=hashlib.sha256).digest()
    sign = base64.b64encode(hmac_code).decode('utf-8')
    data = {
        "msg_type": "text",
        "content": {"text": "测试\n<at user_id='ou_29fce947c16d494a69415c8dab3fcac5'></at>"},
        'timestamp': timestamp,
        'sign': sign,
    }

    headers = {"Content-Type": "application/json"}
    try:
        res = requests.post(ding_url, json=data, headers=headers)
    except Exception as err:
        print(err)
        return ''
    return res.text


def ding():
    url = 'https://open.feishu.cn/open-apis/bot/v2/hook/c2e26d6b-d70d-4f25-a1ce-c37956e54e68'
    data = {
        "msg_type": "text",
        "content": {"text": "测试\n<at user_id='ou_2571ecf6a8808317bb76285e5d75fc1d'></at>"},
        # 'timestamp': timestamp,
        # 'sign': sign,
    }

    headers = {"Content-Type": "application/json"}
    try:
        res = requests.post(url, json=data, headers=headers)
    except Exception as err:
        print(err)
        return ''
    return res.text


def aaa(mobile):
    url = 'https://open.feishu.cn/open-apis/user/v1/batch_get_id?'
    headers = {"Content-Type": "application/json; charset=utf-8",
               'Authorization': 'Bearer t-631df635dcecdec83df576174b662fd8577df0a1'}
    url += f'mobiles={mobile}'
    try:
        res = requests.get(url, headers=headers)
    except Exception as err:
        print(err)
        return ''
    return res.text
    pass


def bbb():
    url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/'
    headers = {"Content-Type": "application/json; charset=utf-8"}
    data = {'app_id': 'cli_a02758318479900c', 'app_secret': 'DlxBX1TI4P8HmLPlpf0j9Xee7YHx704j'}
    try:
        res = requests.post(url, headers=headers, json=data)
    except Exception as err:
        print(err)
        return ''
    return res.text
    pass


if __name__ == '__main__':
    ret = send_ding_ding()
    # ret = ding()
    print(ret)

    # {"code": 0, "expire": 7200, "msg": "ok", "tenant_access_token": "t-631df635dcecdec83df576174b662fd8577df0a1"}

    # ret = bbb()
    # print(ret)

    # {"code": 0, "msg": "success",
    #  "data": {"mobile_users": {"18246196637": [{"open_id": "ou_2571ecf6a8808317bb76285e5d75fc1d"}]},
    #           "mobiles_not_exist": []}}
    # {"code": 0, "msg": "success",
    #  "data": {"mobile_users": {"19979406919": [{"open_id": "ou_decf951d2ed7e7a284c556cfe43437d6"}]},
    #           "mobiles_not_exist": []}}
    # {"code": 0, "msg": "success",
    #  "data": {"mobile_users": {"15148210262": [{"open_id": "ou_29fce947c16d494a69415c8dab3fcac5"}]},
    #           "mobiles_not_exist": []}}
    # ret = aaa('15148210262')
    # print(ret)

    # class UpperAttrMetaClass(type):
    #
    #     def __new__(cls, class_name, class_parents, class_attr):
    #         # 遍历属性字典，把不是__开头的属性名字变为大写
    #         new_attr = {}
    #         for name, value in class_attr.items():
    #             if not name.startswith("__"):
    #                 new_attr[name.upper()] = value
    #
    #         # # 方法1：通过'type'来做类对象的创建
    #         # return type(class_name, class_parents, new_attr)
    #
    #         # 方法2：复用type.__new__方法
    #         # 这就是基本的OOP编程，没什么魔法
    #         return type.__new__(cls, class_name, class_parents, new_attr)
    #
    #
    # class Foo(object, metaclass=UpperAttrMetaClass):
    #     # __metaclass__ = upper_attr  # 设置Foo类的元类为upper_attr
    #     bar = 'bip'
    #
    #
    # print(hasattr(Foo, 'bar'))
    # print(hasattr(Foo, 'BAR'))
    #
    # f = Foo()
    # print(f.BAR)
    # class MyList(object):
    #     """自定义的一个可迭代对象"""
    #
    #     def __init__(self):
    #         self.items = []
    #
    #     def add(self, val):
    #         self.items.append(val)
    #
    #     def __iter__(self):
    #         return MyIterator(self)
    #
    #
    # class MyIterator(object):
    #     """自定义的供上面可迭代对象使用的一个迭代器"""
    #
    #     def __init__(self, mylist):
    #         self.mylist = mylist
    #         # current用来记录当前访问到的位置
    #         self.current = 0
    #
    #     def __next__(self):
    #         if self.current < len(self.mylist.items):
    #             item = self.mylist.items[self.current]
    #             self.current += 1
    #             return item
    #         else:
    #             raise StopIteration
    #
    #     def __iter__(self):
    #         return self
    #
    #
    # mylist = MyList()
    # mylist.add(1)
    # mylist.add(2)
    # mylist.add(3)
    # mylist.add(4)
    # mylist.add(5)
    # for num in mylist:
    #     print(num)

    # class A():
    #     def __init__(self, name):
    #         self._name = name
    #     def __enter__(self):
    #         return open(self._name, 'r')
    #     def __exit__(self, exc_type, exc_val, exc_tb):
    #         pass
    # with A('1') as f:
    #     f.write()
    # pass
