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

'''
class TestLogin(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.base_url = "http://mail.126.com"
		self.verificationerros = []

	def test_login(self):
		driver = self.driver
		driver.get(self.base_url)
		#调用登录函数
		login.login(self,"xxk_student","xxk-881218")
		sleep(3)
		#获取断言信息进行断言
		text = driver.find_element_by_id("spnUid").text
		self.assertEqual(text,"xxk_student@126.com")
		sleep(3)
		#调用退出函数
		login.logout(self)

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([],self.verificationerros)

if __name__ == "__main__":
	unittest.main()
'''
#打开xml文档
dom = xml.dom.minidom.parse('F:\\test-project\\test-data\\login.xml')
#得到文档元素对象
root = dom.documentElement

class TestLogin(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		logins = root.getElementsByTagName('url')
		self.base_url = logins[0].firstChild.data
		self.verificationErrors = []
 


	def tearDown(self):
		self.driver.quit()
		self.assertEqual([],self.verificationErrors)

if __name__ == '__main__':
	unittest.main()

