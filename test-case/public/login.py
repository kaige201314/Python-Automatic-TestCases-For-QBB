#coding=utf-8
#登录
def login(self,username,password):
	driver = self.driver
	driver.find_element_by_id("idInput").clear()
	driver.find_element_by_id("idInput").send_keys(username)
	driver.find_element_by_id("pwdInput").clear()
	driver.find_element_by_id("pwdInput").send_keys(password)
	driver.find_element_by_id("loginBtn").click()
#退出
def logout(self):
	driver = self.driver
	driver.find_element_by_link_text(u"退出").click()