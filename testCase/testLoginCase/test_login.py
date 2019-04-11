import unittest
from time import sleep
from selenium import webdriver
from .login import Login


class LoginCase(unittest.TestCase):
    '''账户登录测试'''
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome("C:\\Users\\KW\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()

    def setUp(self):
        self.dr.implicitly_wait(10)
        # self.dr = webdriver.Chrome()
        # 每次都需要打开登录页面
        login_page = Login(self.dr)
        login_page.open()

    def tearDown(self):
        # self.dr.quit()
        pass

# ====================================账户登录==================================
    # 点击后，显示验证码图片
    def test_verification_code(self):
        '''验证码显示测试'''
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[2]/span").click()
        sleep(2)

    # 正常登录
    def test_login_normal(self):
        '''正常登录测试'''
        b_page = Login(self.dr)
        # b_page.clear_cookies()
        b_page.loginData("18217276943","123qwe","8888")
        title = self.dr.title
        self.assertEqual(title,"测试0117")

    # 账户名信息错误
    def test_login_username_error(self):
        '''账户名信息错误登录测试'''
        b_page = Login(self.dr)
        b_page.loginData("1821727694","123qwe","8888")
        title = self.dr.find_element_by_xpath("/ html / body / div[2] / div[1] / div / div[2] / form[1] / div[3] / p")
        self.assertEqual(title.text,"登录失败,该账户不存在")

    # 账户名为空
    def test_login_username_empty(self):
        '''账户名为空 登录测试'''
        b_page = Login(self.dr)
        b_page.loginData("","123qwe","8888")
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[3]/p")
        self.assertEqual(title.text,"请填写登录账号")

    # 密码错误
    def test_login_password_error(self):
        '''密码错误 登录测试'''
        b_page = Login(self.dr)
        b_page.loginData("18217276943","123123qwe","8888")
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[3]/p")
        self.assertEqual(title.text,"登录失败,用户名或者密码错误")

    # 密码为空
    def test_login_password_empty(self):
        '''密码为空 登录测试'''
        b_page = Login(self.dr)
        b_page.loginData("18217276943","","8888")
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[3]/p")
        self.assertEqual(title.text,"请填写登录密码")

    # 验证码错误
    def test_login_code_error(self):
        '''验证码错误 登录测试'''
        b_page = Login(self.dr)
        b_page.loginData("18217276943","123qwe","88188")
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[3]/p")
        self.assertEqual(title.text,"图形验证码有误")

    # 验证码为空
    def test_login_code_empty(self):
        '''验证码为空 登录测试'''
        b_page = Login(self.dr)
        b_page.loginData("18217276943","123qwe","")
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[3]/p")
        self.assertEqual(title.text,"请填写验证码!")


# ====================================动态登录==================================
    # 正常的动态登录
    def test_dynamicLogin_normal(self):
        '''正常动态登录'''
        b_page = Login(self.dr)
        b_page.dynamicLoginData("18217276943","8888","8888")
        title = self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a")
        self.assertEqual(title.text,"退出登录")

    # 动态登录手机号码错误
    def test_dynamicLogin_username_error(self):
        '''动态登录手机号码错误'''
        b_page = Login(self.dr)
        b_page.dynamicLoginData("182172176943","8888","8888")
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[2]/div[3]/p")
        self.assertEqual(title.text,"手机号码有误，请重新输入")

    # 动态登录手机号码为空
    def test_dynamicLogin_username_empty(self):
        '''动态登录手机号码为空'''
        b_page = Login(self.dr)
        b_page.dynamicLoginData("","8888","8888")
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[2]/div[3]/p")
        self.assertEqual(title.text,"请输入手机号码")

    # 动态登录图片验证码为空
    def test_dynamicLogin_code_empty(self):
        '''动态登录图片验证码为空'''
        b_page = Login(self.dr)
        b_page.dynamicLoginData("18217276943","","8888")
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[2]/div[3]/p")
        self.assertEqual(title.text,"请输入图形验证码")

    # 动态登录图片验证码错误
    def test_dynamicLogin_code_error(self):
        '''动态登录图片验证码错误'''
        b_page = Login(self.dr)
        b_page.dynamicLoginData("18217276943","123","8888")
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[2]/div[3]/p")
        self.assertEqual(title.text,"图形验证码有误")

    # 动态登录短信验证码错误
    def test_dynamicLogin_SMScode_error(self):
        '''动态登录短信验证码错误'''
        b_page = Login(self.dr)
        b_page.dynamicLoginData("18217276943","8888","123")
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[2]/div[3]/p")
        self.assertEqual(title.text,"请重新获取手机短信校验码")

    # 动态登录短信验证码为空
    def test_dynamicLogin_SMScode_empty(self):
        '''动态登录短信验证码为空'''
        b_page = Login(self.dr)
        b_page.dynamicLoginData("18217276943","8888","")
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[2]/div[3]/p")
        self.assertEqual(title.text,"请输入手机验证码")

    # 动态登录短信验证码为空
    def test_dynamicLogin_SMScode_empty(self):
        '''动态登录短信验证码为空'''
        b_page = Login(self.dr)
        b_page.dynamicLoginData("18217276943","8888","")
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[2]/div[3]/p")
        self.assertEqual(title.text,"请输入手机验证码")

if __name__ == '__main__':
    unittest.main()
    # 测试套件
    # suit = unittest.TestSuite()
    # suit.addTest(LoginCase("test_dynamicLogin_SMScode_empty"))
    #
    # # 测试运行
    # runner = unittest.TextTestRunner()
    # runner.run(suit)