import unittest
from time import sleep
from selenium import webdriver
from .jump import BasePage


class JumpCase(unittest.TestCase):
    '''页面跳转测试'''
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome("C:\\Users\\KW\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()

    def setUp(self):
        # 每次都需要打开登录页面
        login_page = BasePage(self.dr)
        login_page.open_homePage()

    def tearDown(self):
        # self.dr.quit()
        pass

# =======================首页起始的跳转=========================

    # 跳转首页
    def test_jump_homePage(self):
        '''跳转首页测试'''
        sleep(2)
        title = self.dr.find_element_by_xpath("/html/body/div[1]/div/div[1]")
        self.assertEqual(title.text,"您好！欢迎来到测试0117专区！")
        sleep(2)

    # 跳转会员中心之登录
    def test_jump_memberCenterLogin(self):
        '''跳转会员中心之登录测试'''
        b_page = BasePage(self.dr)
        b_page.clear_cookies()
        b_page.open_memberCenterLogin()
        title = self.dr.find_element_by_xpath("/ html / body / div[2] / div[1] / span")
        self.assertEqual(title.text,"我的资料")

    # 跳转登录页面
    def test_jump_login(self):
        '''跳转登录页'''
        b_page = BasePage(self.dr)
        b_page.open_login()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/ul/li[1]/a")
        self.assertEqual(title.text,"账户登录")

    # 跳转产品超市页面
    def test_jump_productsMall(self):
        '''跳转产品超市页'''
        b_page = BasePage(self.dr)
        b_page.open_productsMall()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/span")
        self.assertEqual(title.text,"产品超市")

    # 跳转会员中心页面，没有登录状态
    def test_jump_memberCenter(self):
        '''跳转会员中心，没登录'''
        b_page = BasePage(self.dr)
        b_page.open_memberCenter()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/ul/li[1]/a")
        self.assertEqual(title.text,"账户登录")

    # 跳转关于我们页面
    def test_jump_aboutUs(self):
        '''跳转关于我们'''
        b_page = BasePage(self.dr)
        b_page.open_aboutUs()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/span")
        self.assertEqual(title.text,"联系我们")

    # 跳转注册页面
    def test_jump_register(self):
        '''跳转注册页面'''
        b_page = BasePage(self.dr)
        b_page.clear_cookies()
        b_page.open_register()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/a")
        self.assertEqual(title.text,"账号注册")

    # 跳转投保流程指南页面
    def test_jump_insuranceProcessGuide(self):
        '''跳转投保流程指南页面'''
        b_page = BasePage(self.dr)
        b_page.open_insuranceProcessGuide()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/span")
        self.assertEqual(title.text,"投保流程指南")

    # 跳转我的保单页面
    def test_jump_myPolicy(self):
        '''跳转我的保单页面'''
        b_page = BasePage(self.dr)
        b_page.clear_cookies()
        b_page.open_myPolicy()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/ul/li[1]/a")
        self.assertEqual(title.text,"账户登录")

    # 跳转我的保单页面之登录
    def test_jump_myPolicyLogin(self):
        '''跳转我的保单页面之登录'''
        b_page = BasePage(self.dr)
        b_page.clear_cookies()
        b_page.open_myPolicyLogin()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/h2")
        self.assertEqual(title.text,"我的保单")

    # 跳转我的理赔流程指南页面
    def test_jump_guideToClaimsProcess(self):
        '''跳转理赔流程指南页面'''
        b_page = BasePage(self.dr)
        b_page.open_guideToClaimsProcess()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/span")
        self.assertEqual(title.text,"理赔流程指南")

    # 跳转在线客服页面
    def test_jump_onlineService(self):
        '''跳转在线客服页面'''
        b_page = BasePage(self.dr)
        b_page.open_onlineService()
        # title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/span")
        # self.assertEqual(title.text,"理赔流程指南")

    # 跳转发票申请页面
    def test_jump_invoiceApplication(self):
        '''跳转发票申请页面'''
        b_page = BasePage(self.dr)
        b_page.open_invoiceApplication()
        title = self.dr.find_element_by_xpath("//*[@id='one1']/span")
        self.assertEqual(title.text,"电子发票申请与查询")

    # 跳转更多页面
    def test_jump_more(self):
        '''跳转更多页面'''
        b_page = BasePage(self.dr)
        b_page.open_more()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/span")
        self.assertEqual(title.text,"产品超市")

    # 跳转产品详情页面
    def test_jump_productDetails(self):
        '''跳转产品详情页面'''
        b_page = BasePage(self.dr)
        b_page.open_productDetails()
        title = self.dr.find_element_by_xpath("//*[@id='productDetails']/div[2]/div[2]/h3")
        self.assertEqual(title.text,"航意险")

    # 跳转首页底部的关于我们页面
    def test_jump_aboutUsBottom(self):
        '''跳转首页底部的关于我们页面'''
        b_page = BasePage(self.dr)
        b_page.open_aboutUsBottom()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/span")
        self.assertEqual(title.text,"联系我们")

    # 跳转首页底部的常见问题页面
    def test_jump_FAQ(self):
        '''跳转首页底部的常见问题页面'''
        b_page = BasePage(self.dr)
        b_page.open_FAQ()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/span")
        self.assertEqual(title.text,"理赔常见问题")

    # 跳转首页底部的服务指南页面
    def test_jump_serviceGuide(self):
        '''跳转首页底部的服务指南页面'''
        b_page = BasePage(self.dr)
        b_page.open_serviceGuide()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/span")
        self.assertEqual(title.text,"投保流程指南")

# =================================登录页起始的跳转=================================

    # 跳转登录页面的账号登录页面
    def test_jump_accountLogin(self):
        '''跳转登录页面的账号登录页面'''
        b_page = BasePage(self.dr)
        b_page.clear_cookies()
        b_page.open_accountLogin()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/ul/li[1]/a")
        self.assertEqual(title.text,"账户登录")

    # 跳转登录页面的动态登录页面
    def test_jump_dynamicLogin(self):
        '''跳转登录页面的动态登录页面'''
        b_page = BasePage(self.dr)
        b_page.open_dynamicLogin()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[2]/div[1]/div[3]/span")
        self.assertEqual(title.text, "*短信验证码：")

    # 跳转登录页面的首页
    def test_jump_loginHomePage(self):
        '''跳转登录页面的首页'''
        b_page = BasePage(self.dr)
        b_page.open_loginHomePage()
        title = self.dr.find_element_by_xpath("/html/body/ul[1]/li[1]/a/div[2]/p[1]")
        self.assertEqual(title.text, "关于我们")

    # 跳转登录页面的关于我们
    def test_jump_loginAboutUs(self):
        '''跳转登录页面的关于我们'''
        b_page = BasePage(self.dr)
        b_page.open_loginAboutUs()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/span")
        self.assertEqual(title.text, "联系我们")

    # 跳转登录页面的服务指南
    def test_jump_loginServiceGuide(self):
        '''跳转登录页面的服务指南'''
        b_page = BasePage(self.dr)
        b_page.open_loginServiceGuide()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/span")
        self.assertEqual(title.text, "投保流程指南")

    # 跳转登录页面的注册
    def test_jump_loginRegister(self):
        '''跳转登录页面的注册'''
        b_page = BasePage(self.dr)
        b_page.clear_cookies()
        b_page.open_loginRegister()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/a")
        self.assertEqual(title.text, "账号注册")

    # 跳转账户登录框中的立即注册
    def test_jump_loginInRegister(self):
        '''跳转账户登录框中的立即注册'''
        b_page = BasePage(self.dr)
        b_page.open_loginInRegister()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/a")
        self.assertEqual(title.text, "账号注册")

    # 跳转账户登录框中的忘记密码
    def test_jump_loginRetrievePassword(self):
        '''跳转账户登录框中的忘记密码'''
        b_page = BasePage(self.dr)
        b_page.open_loginRetrievePassword()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div/p")
        self.assertEqual(title.text, "找回密码")

    # 跳转动态登录框中的忘记密码
    def test_jump_dynamicLoginRetrievePassword(self):
        '''跳转动态登录框中的忘记密码'''
        b_page = BasePage(self.dr)
        b_page.open_dynamicLoginRetrievePassword()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div/p")
        self.assertEqual(title.text, "找回密码")

    # 跳转动态登录框中的立即注册
    def test_jump_dynamicLoginRegister(self):
        '''跳转动态登录框中的立即注册'''
        b_page = BasePage(self.dr)
        b_page.open_dynamicLoginRegister()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/a")
        self.assertEqual(title.text, "账号注册")

    # 跳转登录页面底部的关于我们
    def test_jump_loginBottomAboutUs(self):
        '''跳转登录页面底部的关于我们'''
        b_page = BasePage(self.dr)
        b_page.open_loginBottomAboutUs()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/span")
        self.assertEqual(title.text, "联系我们")

    # 跳转登录页面底部的常见问题
    def test_jump_loginBottomFAQ(self):
        '''跳转登录页面底部的常见问题'''
        b_page = BasePage(self.dr)
        b_page.open_loginBottomFAQ()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/span")
        self.assertEqual(title.text, "理赔常见问题")

    # 跳转登录页面底部的服务指南
    def test_jump_loginBottomServiceGuide(self):
        '''跳转登录页面底部的服务指南'''
        b_page = BasePage(self.dr)
        b_page.open_loginBottomServiceGuide()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/span")
        self.assertEqual(title.text, "投保流程指南")

# ==========================================关于我们页面跳转==================================

    # 跳转关于我们页面的登录
    def test_jump_aboutUsLogin(self):
        '''跳转关于我们页面的登录'''
        b_page = BasePage(self.dr)
        b_page.open_aboutUsLogin()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/ul/li[1]/a")
        self.assertEqual(title.text, "账户登录")

    # 跳转关于我们页面的注册
    def test_jump_aboutRegister(self):
        '''跳转关于我们页面的注册'''
        b_page = BasePage(self.dr)
        b_page.open_aboutRegister()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/a")
        self.assertEqual(title.text, "账号注册")

    # 跳转关于我们页面的首页
    def test_jump_aboutHomepage(self):
        '''跳转关于我们页面的首页'''
        b_page = BasePage(self.dr)
        b_page.open_aboutHomepage()
        title = self.dr.find_element_by_xpath("/html/body/ul[1]/li[1]/a/div[2]/p[1]")
        self.assertEqual(title.text, "关于我们")

    # 跳转关于我们页面的关于我们
    def test_jump_aboutAboutUs(self):
        '''跳转关于我们页面的关于我们'''
        b_page = BasePage(self.dr)
        b_page.open_aboutAboutUs()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/span")
        self.assertEqual(title.text, "联系我们")

    # 跳转关于我们页面的服务指南
    def test_jump_aboutServiceGuide(self):
        '''跳转关于我们页面的服务指南'''
        b_page = BasePage(self.dr)
        b_page.open_aboutServiceGuide()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/span")
        self.assertEqual(title.text, "投保流程指南")

    # 跳转关于我们页面的联系我们
    def test_jump_aboutConnectUs(self):
        '''跳转关于我们页面的联系我们'''
        b_page = BasePage(self.dr)
        b_page.open_aboutConnectUs()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/h3/span")
        self.assertEqual(title.text, "联系我们")

    # 跳转关于我们页面的联系我们
    def test_jump_aboutCompanyProfile(self):
        '''跳转关于我们页面的联系我们'''
        b_page = BasePage(self.dr)
        b_page.open_aboutCompanyProfile()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/h6/span")
        self.assertEqual(title.text, "公司简介")

    # 跳转关于我们页面的理赔常见问题
    def test_jump_aboutFAQ(self):
        '''跳转关于我们页面的理赔常见问题'''
        b_page = BasePage(self.dr)
        b_page.open_aboutFAQ()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/h6/span")
        self.assertEqual(title.text, "理赔常见问题")

    # 跳转关于我们页面的投保流程指南
    def test_jump_aboutOnlineInsuranceProcess(self):
        '''跳转关于我们页面的投保流程指南'''
        b_page = BasePage(self.dr)
        b_page.open_aboutOnlineInsuranceProcess()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/h3/span")
        self.assertEqual(title.text, "网上投保流程")

    # 跳转关于我们页面的支付方式说明
    def test_jump_aboutDescriptionOfPaymentMethod(self):
        '''跳转关于我们页面的支付方式说明'''
        b_page = BasePage(self.dr)
        b_page.open_aboutDescriptionOfPaymentMethod()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/h6/span")
        self.assertEqual(title.text, "支付方式说明")

    # 跳转关于我们页面的支付方式说明
    def test_jump_aboutClaimsGuide(self):
        '''跳转关于我们页面的支付方式说明'''
        b_page = BasePage(self.dr)
        b_page.open_aboutClaimsGuide()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/h6/span")
        self.assertEqual(title.text, "理赔流程指南")

    # 跳转关于我们页面点击底部的关于我们
    def test_jump_aboutBottomAboutUs(self):
        '''跳转关于我们页面点击底部的关于我们'''
        b_page = BasePage(self.dr)
        b_page.open_aboutBottomAboutUs()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/h3/span")
        self.assertEqual(title.text, "联系我们")

    # 跳转关于我们页面点击底部的常见问题
    def test_jump_aboutBottomFAQ(self):
        '''跳转关于我们页面点击底部的常见问题'''
        b_page = BasePage(self.dr)
        b_page.open_aboutBottomFAQ()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/h6/span")
        self.assertEqual(title.text, "理赔常见问题")

    # 跳转关于我们页面点击底部的服务指南
    def test_jump_aboutBottomServiceGuide(self):
        '''跳转关于我们页面点击底部的服务指南'''
        b_page = BasePage(self.dr)
        b_page.open_aboutBottomServiceGuide()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/h3/span")
        self.assertEqual(title.text, "网上投保流程")

# ======================产品超市跳转=======================

    # 跳转产品超市页面点击登录
    def test_jump_ProductsLogin(self):
        '''跳转产品超市页面点击登录'''
        b_page = BasePage(self.dr)
        b_page.open_ProductsLogin()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/ul/li[1]/a")
        self.assertEqual(title.text, "账户登录")

    # 跳转产品超市页面点击注册
    def test_jump_ProductsRegister(self):
        '''跳转产品超市页面点击注册'''
        b_page = BasePage(self.dr)
        b_page.open_ProductsRegister()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/a")
        self.assertEqual(title.text, "账号注册")

    # 跳转产品超市页面点击首页
    def test_jump_ProductsHomepage(self):
        '''跳转产品超市页面点击首页'''
        b_page = BasePage(self.dr)
        b_page.open_ProductsHomepage()
        title = self.dr.find_element_by_xpath("/html/body/ul[1]/li[1]/a/div[2]/p[1]")
        self.assertEqual(title.text, "关于我们")

    # 跳转产品超市页面点击产品超市
    def test_jump_ProductsProducts(self):
        '''跳转产品超市页面产品超市'''
        b_page = BasePage(self.dr)
        b_page.open_ProductsProducts()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/span")
        self.assertEqual(title.text, "产品超市")

    # 跳转产品超市页面点击会员中心
    def test_jump_ProductsCenter(self):
        '''跳转产品超市页面会员中心'''
        b_page = BasePage(self.dr)
        b_page.open_ProductsCenter()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/ul/li[1]/a")
        self.assertEqual(title.text, "账户登录")

    # 跳转产品超市页面点击会员中心之登录======================
    def test_jump_ProductsCenterLogin(self):
        '''跳转产品超市页面会员中心之登录状态===='''
        b_page = BasePage(self.dr)
        # 涉及到登录时，需要清除cookie操作，避免已经是登录状态的情况
        b_page.clear_cookies()
        b_page.open_ProductsCenterLogin()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/a[2]")
        self.assertEqual(title.text, "会员中心")

    # 跳转产品超市页面点击第一个产品的立即投保
    def test_jump_ProductsInsureImmediately(self):
        '''跳转产品超市页面点击第一个产品的立即投保'''
        b_page = BasePage(self.dr)
        b_page.open_ProductsInsureImmediately()
        title = self.dr.find_element_by_xpath("//*[@id='productDetails']/div[2]/div[2]/h3")
        self.assertEqual(title.text, "航意险")

    # 跳转产品超市页面点击底部的关于我们
    def test_jump_ProductsBottomAboutUs(self):
        '''跳转产品超市页面点击底部的关于我们'''
        b_page = BasePage(self.dr)
        b_page.open_ProductsBottomAboutUs()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/h3/span")
        self.assertEqual(title.text, "联系我们")

    # 跳转产品超市页面点击底部的常见问题
    def test_jump_ProductsBottomFAQ(self):
        '''跳转产品超市页面点击底部的常见问题'''
        b_page = BasePage(self.dr)
        b_page.open_ProductsBottomFAQ()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/h6/span")
        self.assertEqual(title.text, "理赔常见问题")

    # 跳转产品超市页面点击底部的服务指南
    def test_jump_ProductsServiceGuide(self):
        '''跳转产品超市页面点击底部的服务指南'''
        b_page = BasePage(self.dr)
        b_page.open_ProductsBottomServiceGuide()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/h3/span")
        self.assertEqual(title.text, "网上投保流程")

if __name__ == '__main__':
    # unittest.main()
    # 测试套件
    suit = unittest.TestSuite()
    suit.addTest(JumpCase("test_jump_ProductsServiceGuide"))
    '''
    suit.addTest(JumpCase("test_myPolicy"))
    suit.addTest(JumpCase("test_myPolicyLogin"))
    '''
    # 测试运行
    runner = unittest.TextTestRunner()
    runner.run(suit)