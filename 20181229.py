"""
�����˻�:�û�����user1  ���룺123456
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
        ��½�ɹ���,ҳ�浼������ҳ
        ��������Ĳ���
        1.��ҳ�����������--���ⷢ��ҳ��
        2.ѡ��һ�����
        3.�������
        4.�����ı�
        5.�ύ
        �뽫����5������������test_post��ʵ��
        """
    def test_post_topic(self):#��������ʦ����ҵע�ͣ�������Ϊɶ����������"""Ҳ���Ǳ�����ѡ�а�ctrl+/ע��ȴ����
        self.driver.find_element_by_class_name("span-success").click()
        self.driver.find_element_by_id("tab-value").click()
        self.driver.find_element_by_css_selector("#tab-value > option:nth-child(4)").click()
        self.driver.find_element_by_class_name("span9").send_keys("�ҵ�һ�����Զ���ע�ᰥ")
        content_area = self.driver.find_element_by_class_name("CodeMirror-code")
        content_area.click()

        ActionChains(driver).move_to_element(content_area).send_keys("*****").perform()#Ϊʲô���е����ﱨ��



    def tearDown(self):
        self.driver.save_screenshot("./posttopic.png")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
