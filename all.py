#190109-快捷键的操作（自动化代码实现-参考action）
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
#以上代码是注册过程，success；

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
#以上代码是登录过程，success；

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
# driver.find_element_by_id("title").send_keys("20190109夜")
# content_area = driver.find_element_by_class_name("CodeMirror-scroll")
# content_area.click()
# ActionChains(driver).move_to_element(content_area).send_keys("新喜剧之王").perform()
# time.sleep(2)
# ##driver.find_element_by_class_name("span-primary submit_btn").click() #此行代码定位，因为class有两个值，所以不能用
# driver.find_element_by_css_selector('input[type="submit"]').click()
# driver.quit()
#以上代码是登录发帖过程，success；