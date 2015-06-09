#coding=utf-8
from selenium import webdriver
import unittest,time

class TestYoudao(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(10)
		self.base_url = "http://www.youdao.com"

	def test_youdao_search(self):
		u'''有道搜索用例'''
		driver = self.driver
		driver.get(self.base_url + "/")
		driver.find_element_by_id("query").clear()
		driver.find_element_by_id("query").send_keys("webdriver")
		driver.find_element_by_id("qb").click()
		time.sleep(2)
		title = driver.title
		self.assertEqual(title,u"webdriver - 有道搜索")
		print "有道搜索执行完毕！"


	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()

