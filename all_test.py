#coding=utf-8
import unittest
import unittest,time
import HTMLTestRunner

def createsuite():
	testunit = unittest.TestSuite()
	#定义查找测试文件的目录
	test_dir = 'F:\\test-project'
	discover = unittest.defaultTestLoader.discover(test_dir,pattern ='test_*.py',top_level_dir=None)
	#将discover方法筛选出来的用例，循环添加到测试套件中,打印出的用例信息会递增
	for test_case in discover:
			testunit.addTests(test_case)
			print testunit
	return testunit



if __name__ == '__main__':
	#获取当前时间
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	#定义测试报告存放路径，通过filename将文件以读写的方式打开
	filename = "F:\\test-project\\report\\"+now+"_result.html"
	fp = file(filename,'wb')
	#定义测试报告
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'所有用例的测试报告',description=u'用例执行情况如下所示：')
	
	alltestnames = createsuite()
	runner.run(alltestnames)
	fp.close()