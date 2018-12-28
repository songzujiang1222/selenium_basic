"""
测试账户:用户名：user1  密码：123456
"""
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

class Cnode(unittest.TestCase):
    def setUp(self):
        self.Url = 'http://39.107.96.138:3000/'
        self.driver = webdriver.Chrome()
        self.driver.get(self.Url)
        self.driver.find_element_by_css_selector('a[href="/signin"]').click()
        self.driver.find_element_by_id("name").send_keys("user1")
        self.driver.find_element_by_id("pass").send_keys("123456")
        self.driver.find_element_by_class_name("span-primary").click()
        """
        登陆成功后,页面导航到首页
        发布话题的操作
        1.首页点击发布话题--话题发布页面
        2.选择一个版块
        3.输入标题
        4.输入文本
        5.提交
        请将上述5步操作在下面test_post中实现
        """
    def test_post_topic(self):#复制了老师的作业注释，报错了为啥？？？更换"""也还是报错，但选中按ctrl+/注释却可以
        self.driver.find_element_by_class_name("span-success").click()
        self.driver.find_element_by_id("tab-value").click()
        self.driver.find_element_by_css_selector("#tab-value > option:nth-child(4)").click()
        self.driver.find_element_by_class_name("span9").send_keys("我第一次用自动化注册哎")
        content_area = self.driver.find_element_by_class_name("CodeMirror-code")
        content_area.click()

        ActionChains(driver).move_to_element(content_area).send_keys("*****").perform()#为什么运行到这里报错？



    def tearDown(self):
        self.driver.save_screenshot("./posttopic.png")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
