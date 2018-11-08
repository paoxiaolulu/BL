import unittest,requests
import ddt
from BeautifulReport import BeautifulReport as bf
from urllib import parse
from conf.setting import BASE_URL

@ddt.ddt
class %s(unittest.TestCase): #是百分号s指变量class_name
	base_url = BASE_URL
	@ddt.file_data(r'%s')#ddt帮你读文件，获取文件内容，循环调用函数 百分号s是指变量file_name
	def test_request(self,**kwargs):
		detail = kwargs.get('detail','没写用例描述')
		self._testMethodDoc = detail  #动态的用例描述
		url = kwargs.get('url')#url
		url = parse.urljoin(self.base_url,url)#拼接好url
		method = kwargs.get('method','get')#请求方式
		data = kwargs.get('data',{}) #请求参数
		header = kwargs.get('header',{})#请求头
		cookie = kwargs.get('cookie',{})#cookie
		check = kwargs.get('check')
		method = method.lower() #便于处理
		try:
			if method=='get':
				res = requests.get(url,params=data,cookies=cookie,headers=header).text
				#因为接口有异常的情况下， 可能返回的不是json串，会报错
			else:
				res = requests.post(url,data=data,cookies=cookie,headers=header).text
		except Exception as e:
			print('接口请求出错')
			res = e
		for c in check:
			self.assertIn(c,res,msg='预计结果不符，预期结果：'+c + '实际结果：' +res)