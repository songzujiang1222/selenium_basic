# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
#driver.find_element_by_id("kw").send_keys("Hello World") #©��by�����±���
#driver.find_element_by_id("kw").send_keys(Keys.ENTER) #keys.ENTER��kСд����keysδ���壬Ӧ����Keys.ENTER��
#driver.find_element_by_id("su").click()   #©��by�����±���
#driver.quit()

"""
181225��ͥ��ҵ
"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # import�����Keys������Сд��k���ᱨ��

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
        driver.find_element_by_id("q").send_keys("����")
        driver.find_element_by_css_selector("#J_TSearchForm > div.search-button > button").click() #ͨ��css��λ
    
    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()