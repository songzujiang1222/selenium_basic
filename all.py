#190109-��ݼ��Ĳ������Զ�������ʵ��-�ο�action��
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# driver = webdriver.Chrome()
# driver.get("http://39.107.96.138:3000/")
# driver.find_element_by_css_selector('a[href="/signup"]').click()
# driver.find_element_by_id("loginname").send_keys("xiaosong")
# driver.find_element_by_id("pass").send_keys("admin")
# driver.find_element_by_id("re_pass").send_keys("admin")
# driver.find_element_by_id("email").send_keys("1547954934@qq.com")
# driver.find_element_by_class_name("span-primary").click()
# driver.quit()
#���ϴ�����ע����̣�success��

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# driver = webdriver.Chrome()
# driver.get("http://39.107.96.138:3000/")
# driver.find_element_by_css_selector('a[href="/signin"]').click()
# driver.find_element_by_id("name").send_keys("user1")
# driver.find_element_by_id("pass").send_keys("123456")
# driver.find_element_by_class_name("span-primary").click()
# time.sleep(2)
# driver.quit()
#���ϴ����ǵ�¼���̣�success��

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# driver = webdriver.Chrome()
# driver.get("http://39.107.96.138:3000/")
# driver.find_element_by_css_selector('a[href="/signin"]').click()
# driver.find_element_by_id("name").send_keys("user1")
# driver.find_element_by_id("pass").send_keys("123456")
# driver.find_element_by_class_name("span-primary").click()
# time.sleep(2)
# driver.find_element_by_class_name('span-success').click()
# driver.find_element_by_id("tab-value").click()
# driver.find_element_by_css_selector('option[value="share"]').click()
# driver.find_element_by_id("title").send_keys("20190109ҹ")
# content_area = driver.find_element_by_class_name("CodeMirror-scroll")
# content_area.click()
# ActionChains(driver).move_to_element(content_area).send_keys("��ϲ��֮��").perform()
# time.sleep(2)
# ##driver.find_element_by_class_name("span-primary submit_btn").click() #���д��붨λ����Ϊclass������ֵ�����Բ�����
# driver.find_element_by_css_selector('input[type="submit"]').click()
# driver.quit()
#���ϴ����ǵ�¼�������̣�success��