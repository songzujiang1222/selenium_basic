# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
#driver.find_element_by_id("kw").send_keys("Hello World") #漏了by，导致报错；
#driver.find_element_by_id("kw").send_keys(Keys.ENTER) #keys.ENTER的k小写报错：keys未定义，应该是Keys.ENTER；
#driver.find_element_by_id("su").click()   #漏了by，导致报错；
#driver.quit()

"""
181225家庭作业
"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # import后面的Keys不能是小写的k，会报错

class BaiDuSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_baidu_search(self):
        driver = self.driver
        driver.get("https://www.baidu.com")
        driver.find_element_by_id("kw").send_keys("Hello World")
        driver.find_element_by_id("kw").send_keys(Keys.ENTER)
    
    def test_bing_search(self):
        driver = self.driver
        driver.get("https://www.taobao.com")
        driver.find_element_by_id("q").send_keys("西服")
        driver.find_element_by_css_selector("#J_TSearchForm > div.search-button > button").click() #通过css定位
    
    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()