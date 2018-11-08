
import unittest
import requests

import ddt  # #可做参数化  自动读文件中数据

from BeautifulReport import BeautifulReport as bf

from urllib import parse


@ddt.ddt
class Login(unittest.TestCase):
    base_url = 'https://ceshilanxiongdianshang.billionss.com/api/v5/'

    @ddt.file_data('/Users/air/Documents/BL/testcases/冒烟_消息_通知条数.yaml')
    def test_request(self, **kwargs):

        detail = kwargs.get('detail', '没写用例描述')  # '''和%s组合来描述用例在这里无效。

        self._testMethodDoc = detail  # 动态的用例描述

        url = kwargs.get('url')  # url

        url = parse.urljoin(self.base_url, url)  # 拼接好url  只能拼接 比如关于/的问题处理

        method = kwargs.get('method', 'post')  # post  防止没有传请求方式

        data = kwargs.get('data', {})  # 请求参数

        header = kwargs.get('header', {})  # 请求头

        cookie = kwargs.get('cookie', {})  # cookie

        check = kwargs.get('check')

        method = method.lower()  # 便于处理

        try:

            if method == 'get':

                res = requests.get(url, params=data, cookies=cookie, headers=header).text

                # 因为接口有异常的情况下， 可能返回的不是json串，会报错

            else:

                res = requests.post(url, data=data, cookies=cookie, headers=header).text

        except Exception as e:

            print('接口请求出错')

            res = e

        for c in check:
            self.assertIn(c, res, msg='预计结果不符，预期结果包含[%s],实际结果[%s]' % (c, res))  # 查看是否包含 断言查看一次错误就停止，后面加如错误提示  但check在yml中得是list方便查看是否包含。


sutie = unittest.TestSuite()

sutie.addTest(unittest.makeSuite(Login))  # 添加用例

run = bf(sutie)  # 实例化

run.report('api_test', '冒烟测试用例')

print(run.success_count)  # 通过的次数

print(run.failure_count)  # 失败的次数