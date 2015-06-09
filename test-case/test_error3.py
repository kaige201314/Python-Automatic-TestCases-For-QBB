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

	#用例6：输入正确的用户名，正确的密码，登陆成功，但是断言是错误的
	def test_error3(self):
		u'''输入正确的用户名，正确的密码'''
		driver = self.driver
		driver.get(self.base_url)
		logins = root.getElementsByTagName('right')
		username = logins[0].getAttribute("username")
		password = logins[0].getAttribute("password")
		title = driver.title
		#print title
		sleep(1)
		login.login(self,username,password)
		sleep(2)
		#获取断言信息进行断言
		text = u"126网易免费邮--你的专业电子邮局"
		self.assertEqual(text,title)
		print "用例6执行完毕！"

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([],self.verificationErrors)

if __name__ == "__main__":
	unittest.main()