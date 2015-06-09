#coding=utf-8
from selenium import webdriver
import unittest,time
import HTMLTestRunner

class TestBaidu(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(10)
		self.base_url = "http://www.baidu.com"

	def test_baidu_search(self):
		u'''百度搜索用例'''
		driver = self.driver
		driver.get(self.base_url + "/")
		driver.find_element_by_id("kw").clear()
		driver.find_element_by_id("kw").send_keys("HTNMLTestRunner")
		driver.find_element_by_id("su").click()
		time.sleep(2)
		title = driver.title
		self.assertEqual(title,u"HTNMLTestRunner_百度搜索")
		print "百度搜索执行完毕！"

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	#添加测试套件，并向套件中添加案例
	testunit = unittest.TestSuite()
	testunit.addTest(TestBaidu("test_baidu_search"))
	#获取当前时间
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	#定义测试报告存放路径，通过filename将文件以读写的方式打开
	filename = "F:\\test-project\\report\\"+now+"_result.html"
	fp = file(filename,'wb')
	#定义测试报告
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'百度搜索，测试报告',description=u'用例执行情况：')

	#运行用例
	runner.run(testunit)
	#关闭报告文件
	fp.close()



