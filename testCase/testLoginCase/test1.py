from selenium import webdriver
from time import sleep


dr = webdriver.Chrome()
dr.get("http://nettest.tpstic.com/policy-operation-web/partner?partnerCode=0117")
dr.implicitly_wait(10)

# 进入登录页
dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()

# 定位登录页中登录的元素
dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[1]/div[1]/div/input").send_keys("18217276943")
dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[1]/div[2]/div/input").send_keys("123qwe")
# dr.find_element_by_id("username").send_keys("18217276943")
# dr.find_element_by_id("password").send_keys("123qwe")
dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[1]/div[3]/div/input").send_keys("8888")
dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[2]/button").click()

