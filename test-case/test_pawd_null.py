#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium import webdriver
import unittest
from time import sleep
#导入login文件
from public import login
import xml.dom.minidom

#打开xml文档
dom = xml.dom.minidom.parse('F:\\test-project\\test-data\\login.xml')
#得到文档元素对象
root = dom.documentElement

class Test_Null(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		logins = root.getElementsByTagName('url')
		self.base_url = logins[0].firstChild.data
		self.verificationErrors = []

	#用例2：输入用户名、但是密码为空
	def test_pawd_null(self):
		u'''用例2：输入用户名、但是密码为空'''
		driver = self.driver
		driver.get(self.base_url)
		logins = root.getElementsByTagName('pawd_null')
		username = logins[0].getAttribute("username")
		password = logins[0].getAttribute("password")
		prompt_info = logins[0].firstChild.data
		sleep(1)
		login.login(self,username,password)
		sleep(2)
		#获取断言信息进行断言
		text = driver.find_element_by_xpath("//div[@class='error-tt']/p").text
		self.assertEqual(text,prompt_info)
		print "用例2执行完毕！"

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([],self.verificationErrors)

if __name__ == "__main__":
	unittest.main()