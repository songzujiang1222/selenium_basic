"""
八种定位页面元素的方法
1-Id,2-Name,3-XPath,4-Hyperlinks by Link Text,5-Elements by Tag Name,6-Elements by Class Name 7-Elements by CSS Selectors
"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class BaiDuSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_baidu_search(self):
        driver = self.driver
        driver.get("https://www.baidu.com")
        driver.find_element_by_id("kw").send_keys("Hello World")  #第一种方法：id
        driver.find_element_by_id("kw").send_keys(Keys.ENTER)
        time.sleep(1)

    def test_baidu_seatch2(self):
        driver = self.driver
        driver.get("https://www.baidu.com")
        driver.find_element_by_class_name("s_ipt").send_keys("class_name") #第二种方法：class_name
        driver.find_element_by_class_name("s_ipt").send_keys(Keys.ENTER)
        time.sleep(2)
    
    def test_baidu_search3(self):
        driver3 = self.driver
        driver3.get("https://www.baidu.com")
        driver3.find_element_by_link_text("新闻")   #满足条件：1标签是a-超链接，2取的是页面显示的文字，3、文字是唯一的；
        driver3.find_element_by_link_text("新闻").click()  #第三种方法：link_text
        time.sleep(3)

    def test_baidu_search4(self):
        driver4 =self.driver
        driver4.get("https://www.baidu.com")
        driver4.find_element_by_partial_link_text("新")   #第四种方法：partial_link_text,"检索关键字"
        driver4.find_element_by_partial_link_text("新").click()
        time.sleep(4)

    def test_bing_search5(self):
        driver5 = self.driver
        driver5.get("https://www.taobao.com")
        driver5.find_element_by_id("q").send_keys("西服")
        driver5.find_element_by_css_selector("#J_TSearchForm > div.search-button > button").click()#第五种：css_selector
        time.sleep(5)

    def test_baidu_search6(self):   #search粗心打成了seatch导致报错，无此方法
        driver6 = self.driver
        driver6.get("https://www.baidu.com")   #漏打了www.
        driver6.find_element_by_name("wd").send_keys("by_name") #第六种方法：name
        driver6.find_element_by_name("wd").send_keys(Keys.ENTER) #element_by粗心打成了element—by导致报错；
        time.sleep(6)

    # def test_baidu_search7(self):
    #     driver7 = self.driver
    #     driver7.get("https://www.baidu.com")
    #     driver7.find_element_by_css_selector("a[name="tj_trnews"]").click()  #为什么报错？？？
    #     time.sleep(2)
        
    
    def teatDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()