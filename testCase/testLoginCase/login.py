from time import sleep
from selenium import webdriver

class BasePage():
    # =webdriver.Chrome()
    def __init__(self,dr,
                 base_url="http://nettest.tpstic.com/policy-operation-web/partner?partnerCode=0117"):
        self.dr = dr
        self.base_url = base_url
        # self.dr.implicitly_wait(10)

    # 访问该地址后，跳转登录页面
    def open(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)

class Login(BasePage):

    # 清除浏览器缓存
    def clear_cookies(self):
        self.dr.delete_all_cookies()
        # print("123") # 涉及到登录的用例，用清除cookies

    # 账户登录信息输入框
    def loginData(self,username,password,code):
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[1]/div[1]/div/input").send_keys(
            username)
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[1]/div[2]/div/input").send_keys(
            password)
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[1]/div[3]/div/input").send_keys(
            code)
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[2]/button").click()
        sleep(1)

    # 动态登录信息输入框
    def dynamicLoginData(self, username, code, SMScode):
        # 先进行点击动态登录，进入动态登录页面框
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/ul/li[2]/a").click()
        sleep(1)
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[2]/div[1]/div[1]/div/input").send_keys(
            username)
        self.dr.find_element_by_xpath("//*[@id='validatecode']").send_keys(
            code)
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[2]/div[1]/div[3]/div/input[1]").send_keys(
            SMScode)
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[2]/div[2]/button").click()
        sleep(1)

# a = BasePage()
# a.open()