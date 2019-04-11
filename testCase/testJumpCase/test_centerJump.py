import unittest
from time import sleep
from selenium import webdriver
from .center_jump import BasePage


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
        title = self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a")
        if title.text != "退出登录":
            login_page.open_memberCenterLogin()
        else:
            pass

    def tearDown(self):
        # self.dr.quit()
        pass

# =======================会员中心页面的跳转=========================

    # 在会员中心跳转首页
    def test_jump_centerHomepage(self):
        '''在会员中心跳转首页'''
        b_page = BasePage(self.dr)
        # b_page.clear_cookies()
        b_page.open_centerHomepage()
        title = self.dr.find_element_by_xpath("/html/body/ul[1]/li[1]/a/div[2]/p[1]")
        self.assertEqual(title.text,"关于我们")

    # 在会员中心跳转产品超市
    def test_jump_centerProduct(self):
        '''在会员中心跳转产品超市'''
        b_page = BasePage(self.dr)
        # b_page.clear_cookies()
        b_page.open_centerProduct()
        title = self.dr.find_element_by_xpath("//*[@id='pageLists']/a[1]/div[1]/div[1]/h1")
        self.assertEqual(title.text,"航意险")

    # 在会员中心点击图标跳转首页
    def test_jump_centerIcon(self):
        '''在会员中心点击中国太平图标跳转首页'''
        b_page = BasePage(self.dr)
        b_page.open_centerIcon()
        title = self.dr.find_element_by_xpath("/html/body/ul[1]/li[1]/a/div[2]/p[1]")
        self.assertEqual(title.text,"关于我们")

    # 在会员中心点击会员中心
    def test_jump_centerCenter(self):
        '''在会员中心点击会员中心'''
        b_page = BasePage(self.dr)
        b_page.open_centerCenter()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/h2")
        self.assertEqual(title.text,"我的资料")

    # 在会员中心点击退出登录
    def test_jump_centerLogout(self):
        '''在会员中心点击退出登录'''
        b_page = BasePage(self.dr)
        b_page.open_centerLogout()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/ul/li[1]/a")
        self.assertEqual(title.text,"账户登录")

    # 在会员中心点击面包屑的会员中心
    def test_jump_centerCrumbsCenter(self):
        '''在会员中心点击面包屑的会员中心'''
        b_page = BasePage(self.dr)
        b_page.open_centerCrumbsCenter()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/h2")
        self.assertEqual(title.text,"我的资料")

    # 在会员中心点击面包屑的首页
    def test_jump_centerCrumbsHomepage(self):
        '''在会员中心点击面包屑的首页'''
        b_page = BasePage(self.dr)
        b_page.open_centerCrumbsHomepage()
        title = self.dr.find_element_by_xpath("/html/body/ul[1]/li[1]/a/div[2]/p[1]")
        self.assertEqual(title.text,"关于我们")

    # 在会员中心点击我的订单
    def test_jump_centerMyOrder(self):
        '''在会员中心点击我的订单'''
        b_page = BasePage(self.dr)
        b_page.open_centerMyOrder()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/h2")
        self.assertEqual(title.text,"我的订单")

    # 在会员中心点击我的保单
    def test_jump_centerMyPolicy(self):
        '''在会员中心点击我的保单'''
        b_page = BasePage(self.dr)
        b_page.open_centerMyPolicy()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/h2")
        self.assertEqual(title.text,"我的保单")

    # 在会员中心点击常用联系人
    def test_jump_centerTopContacts(self):
        '''在会员中心点击常用联系人'''
        b_page = BasePage(self.dr)
        b_page.open_centerTopContacts()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/h2")
        self.assertEqual(title.text,"常用联系人信息")

    # 在会员中心点击保单批改下面的申请批改
    def test_jump_centerApplyForCorrecting(self):
        '''在会员中心点击保单批改下面的申请批改'''
        b_page = BasePage(self.dr)
        b_page.open_centerApplyForCorrecting()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/h2")
        self.assertEqual(title.text,"申请批改")

    # 在会员中心点击保单批改下面的我的批改
    def test_jump_centerMyGrade(self):
        '''在会员中心点击保单批改下面的我的批改'''
        b_page = BasePage(self.dr)
        b_page.open_centerMyGrade()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/h2")
        self.assertEqual(title.text,"批改进度查询")

    # 在会员中心点击理赔服务下面的申请理赔
    def test_jump_centerApplyForClaims(self):
        '''在会员中心点击理赔服务下面的申请理赔'''
        b_page = BasePage(self.dr)
        b_page.open_centerApplyForClaims()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/h2")
        self.assertEqual(title.text,"申请理赔")

    # 在会员中心点击理赔服务下面的我的理赔
    def test_jump_centerMyClaims(self):
        '''在会员中心点击理赔服务下面的我的理赔'''
        b_page = BasePage(self.dr)
        b_page.open_centerMyClaims()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/h2")
        self.assertEqual(title.text,"理赔进度查询")

    # 在会员中心点击理赔服务下面的我的暂存
    def test_jump_centerMyHold(self):
        '''在会员中心点击理赔服务下面的我的暂存'''
        b_page = BasePage(self.dr)
        b_page.open_centerMyHold()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/h2")
        self.assertEqual(title.text,"我的暂存查询")

    # 在会员中心点击会员中心下面的关于我们
    def test_jump_centerBottomAboutUs(self):
        '''在会员中心点击会员中心下面的关于我们'''
        b_page = BasePage(self.dr)
        b_page.open_centerBottomAboutUs()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/h3/span")
        self.assertEqual(title.text,"联系我们")

    # 在会员中心点击会员中心下面的常见问题
    def test_jump_centerBottomFAQ(self):
        '''在会员中心点击会员中心下面的常见问题'''
        b_page = BasePage(self.dr)
        b_page.open_centerBottomFAQ()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/h6/span")
        self.assertEqual(title.text,"理赔常见问题")

    # 在会员中心点击会员中心下面的服务指南
    def test_jump_centerBottomServiceGuide(self):
        '''在会员中心点击会员中心下面的服务指南'''
        b_page = BasePage(self.dr)
        b_page.open_centerBottomServiceGuide()
        title = self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/h3/span")
        self.assertEqual(title.text,"网上投保流程")

if __name__ == '__main__':

    unittest.main()
    # # 测试套件
    # suit = unittest.TestSuite()
    # suit.addTest(JumpCase("test_jump_centerBottomServiceGuide"))
    # '''
    # suit.addTest(JumpCase("test_myPolicy"))
    # suit.addTest(JumpCase("test_myPolicyLogin"))
    # '''
    # # 测试运行
    # runner = unittest.TextTestRunner()
    # runner.run(suit)