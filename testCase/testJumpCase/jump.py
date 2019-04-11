from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BasePage():
    # =webdriver.Chrome()
    def __init__(self,dr,
                 base_url="http://nettest.tpstic.com/policy-operation-web/partner?partnerCode=0117"):
        self.dr = dr
        self.base_url = base_url
        self.dr.implicitly_wait(10)

    # 清除浏览器缓存
    def clear_cookies(self):
        self.dr.delete_all_cookies()
        # print("123") # 涉及到登录的用例，用清除cookies

# =============================首页起始的跳转=============================

    # 访问该地址后，跳转首页页面
    def open_homePage(self):
        self.dr.get(self.base_url)
        sleep(2)

    # 访问该地址后，跳转登录页面
    def open_login(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)

    # 访问该地址后，跳转产品超市页面
    def open_productsMall(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)

    # 访问该地址后，跳转关于我们页面
    def open_aboutUs(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/ul[1]/li[1]/a/div[2]/p[1]").click()
        sleep(2)

    # 访问该地址后，跳转会员中心页面
    def open_memberCenter(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)

    # 访问该地址后，跳转会员中心页面====>>登录状态
    def open_memberCenterLogin(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)# 点击会员中心后，会弹出登录页面，只有登录后，才能真正的进入会员中心页面，下面就是登录的操作
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[1]/div[1]/div/input").send_keys(
            "18217276943")
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[1]/div[2]/div/input").send_keys(
            "123qwe")
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[1]/div[3]/div/input").send_keys(
            "8888")
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[2]/button").click()
        sleep(2)
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)

    # 访问该地址后，跳转注册页面
    def open_register(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[2]").click()
        sleep(2)

    # 访问该地址后，跳转投保流程指南页面
    def open_insuranceProcessGuide(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/ul[1]/li[2]/a/div[2]/p[1]").click()
        sleep(2)

    # 访问该地址后，跳转我的保单页面
    def open_myPolicy(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/ul[1]/li[3]/a/div[2]/p[1]").click()
        sleep(2)

    # 访问该地址后，跳转我的保单页面====>>登录状态
    def open_myPolicyLogin(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/ul[1]/li[3]/a/div[2]/p[1]").click()
        sleep(2)# 登录操作
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[1]/div[1]/div/input").send_keys(
            "18217276943")
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[1]/div[2]/div/input").send_keys(
            "123qwe")
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[1]/div[3]/div/input").send_keys(
            "8888")
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[2]/button").click()
        sleep(1)# 点击会员中心操作
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(1)# 点击我的保单操作
        self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/dl[2]/dd[3]/a/span/i").click()

    # 访问该地址后，跳转我的理赔流程指南
    def open_guideToClaimsProcess(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/ul[1]/li[4]/a/div[2]/p[1]").click()
        sleep(2)

    # 访问该地址后，跳转在线客服页面
    def open_onlineService(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/ul[1]/li[5]/a/div[2]/p[1]").click()
        sleep(2)

    # 访问该地址后，跳转发票申请页面
    def open_invoiceApplication(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/ul[1]/li[6]/a/div[2]/p[1]").click()
        sleep(2)


    # 访问该地址后，点击首页中的更多，跳转产品超市页面
    def open_more(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("//*[@id='floor1']/h3/a").click()
        sleep(2)

    # 访问该地址后，跳转产品详情页面
    def open_productDetails(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("//*[@id='floor1']/div/div[2]/div/a/img").click()
        sleep(2)

    # 访问该地址后，点击底部的关于我们，跳转关于我们页面
    def open_aboutUsBottom(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/footer/div/ul/li[1]/a").click()
        sleep(2)

    # 访问该地址后，点击底部的常见问题，跳转常见问题页面
    def open_FAQ(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/footer/div/ul/li[2]/a").click()
        sleep(2)

    # 访问该地址后，点击底部的服务指南，跳转服务指南页面
    def open_serviceGuide(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/footer/div/ul/li[3]/a").click()
        sleep(2)

# ============登录页起始的跳转================

    # 访问该地址后，跳转账号登录页面
    def open_accountLogin(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 登录页面点击登录
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)

    # 访问该地址后，跳转动态登录页面
    def open_dynamicLogin(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 登录页面点击动态登录
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/ul/li[2]/a").click()
        sleep(2)

    # 访问该地址后，从登录页面跳转首页
    def open_loginHomePage(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 登录页面点击首页
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[1]/a").click()
        sleep(2)

    # 访问该地址后，从登录页面跳转关于我们
    def open_loginAboutUs(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 登录页面点击关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)

    # 访问该地址后，从登录页面跳转服务指南
    def open_loginServiceGuide(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 登录页面点击服务指南
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)

    # 访问该地址后，从登录页面跳转注册
    def open_loginRegister(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 登录页面点击注册
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[2]").click()
        sleep(2)

    # 访问该地址后，登录框内进行点击立即注册
    def open_loginInRegister(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 登录框内进行点击立即注册
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[3]/p[1]/a").click()
        sleep(2)

    # 访问该地址后，登录框内进行点击忘记密码
    def open_loginRetrievePassword(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 登录框内进行点击忘记密码
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[3]/p[2]/a").click()
        sleep(2)

    # 访问该地址后，动态登录框内进行点击立即注册
    def open_dynamicLoginRegister(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 点击动态登录
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/ul/li[2]/a").click()
        sleep(1)
        # 点击动态登录中的立即注册
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[3]/p[1]/a").click()
        sleep(2)

    # 访问该地址后，动态登录框内进行点击忘记密码
    def open_dynamicLoginRetrievePassword(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 点击动态登录
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/ul/li[2]/a").click()
        sleep(1)
        # 点击动态登录中的忘记密码
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[3]/p[2]/a").click()
        sleep(2)

    # 访问该地址后，在登录页面底部点击关于我们跳转
    def open_loginBottomAboutUs(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 点击登录页面底部的关于我们
        self.dr.set_window_size(1238,1238)
        sleep(3)
        self.dr.find_element_by_xpath("/html/body/div[2]/footer/div/ul/li[1]/a").click()
        sleep(2)

    # 访问该地址后，在登录页面底部点击常见问题跳转
    def open_loginBottomFAQ(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 点击登录页面底部的常见问题
        self.dr.set_window_size(1238,1238)
        sleep(3)
        self.dr.find_element_by_xpath("/html/body/div[2]/footer/div/ul/li[2]/a").click()
        sleep(2)

    # 访问该地址后，在登录页面底部点击常见问题跳转
    def open_loginBottomServiceGuide(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 点击登录页面底部的常见问题
        self.dr.set_window_size(1238,1238)
        sleep(3)
        self.dr.find_element_by_xpath("/html/body/div[2]/footer/div/ul/li[3]/a").click()
        sleep(2)

# =======================================关于我们页面跳转====================================

    # 访问该地址后，在关于我们页面点击登录跳转
    def open_aboutUsLogin(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在关于我们页面点击登录
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)

    # 访问该地址后，在关于我们页面点击注册跳转
    def open_aboutRegister(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在关于我们页面点击注册
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[2]").click()
        sleep(2)

    # 访问该地址后，在关于我们页面点击首页跳转
    def open_aboutHomepage(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在关于我们页面点击首页
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[1]/a").click()
        sleep(2)

    # 访问该地址后，在关于我们页面点击关于我们跳转
    def open_aboutAboutUs(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在关于我们页面点击关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)

    # 访问该地址后，在关于我们页面点击服务指南跳转
    def open_aboutServiceGuide(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在关于我们页面点击服务指南
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)

    # 访问该地址后，在关于我们页面点击关于我们下的联系我们跳转
    def open_aboutConnectUs(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在关于我们页面点击联系我们
        self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/dl[1]/ul[1]/li/a").click()
        sleep(2)

    # 访问该地址后，在关于我们页面点击关于我们下的公司简介跳转
    def open_aboutCompanyProfile(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在关于我们页面点击公司简介
        self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/dl[1]/ul[2]/li/a").click()
        sleep(2)

    # 访问该地址后，在关于我们页面点击常见问题下的理赔常见问题跳转
    def open_aboutFAQ(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在关于我们页面点击理赔常见问题
        self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/dl[2]/ul/li/a").click()
        sleep(2)

    # 访问该地址后，在关于我们页面点击常见问题下的投保流程指南跳转
    def open_aboutOnlineInsuranceProcess(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在关于我们页面点击投保流程指南
        self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/dl[3]/ul[1]/li/a").click()
        sleep(2)

    # 访问该地址后，在关于我们页面点击常见问题下的支付方式说明
    def open_aboutDescriptionOfPaymentMethod(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在关于我们页面点击支付方式说明
        self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/dl[3]/ul[2]/li/a").click()
        sleep(2)

    # 访问该地址后，在关于我们页面点击常见问题下的理赔流程指南
    def open_aboutClaimsGuide(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在关于我们页面点击支付方式说明
        self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/dl[3]/ul[3]/li/a").click()
        sleep(2)

    # 访问该地址后，在关于我们页面点击底部的关于我们
    def open_aboutBottomAboutUs(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在关于我们页面底部点击关于我们
        self.dr.find_element_by_xpath("/html/body/footer/div/ul/li[1]/a").click()
        sleep(2)

    # 访问该地址后，在关于我们页面点击底部的常见问题
    def open_aboutBottomFAQ(self):
        self.dr.get(self.base_url)
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)# 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在关于我们页面底部点击常见问题
        self.dr.find_element_by_xpath("/html/body/footer/div/ul/li[2]/a").click()
        sleep(2)

    # 访问该地址后，在关于我们页面点击底部的服务指南
    def open_aboutBottomServiceGuide(self):
        self.dr.get(self.base_url)
        # 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在关于我们页面底部点击服务指南
        self.dr.find_element_by_xpath("/html/body/footer/div/ul/li[3]/a").click()
        sleep(2)

# =====================================产品超市跳转=================================

    # 访问该地址后，在产品超市页面点击登录
    def open_ProductsLogin(self):
        self.dr.get(self.base_url)
        # 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在产品超市页面点击登录
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[1]").click()
        sleep(2)

    # 访问该地址后，在产品超市页面点击注册
    def open_ProductsRegister(self):
        self.dr.get(self.base_url)
        # 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在产品超市页面点击注册
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a[2]").click()
        sleep(2)

    # 访问该地址后，在产品超市页面点击首页
    def open_ProductsHomepage(self):
        self.dr.get(self.base_url)
        # 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在产品超市页面点击首页
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[1]/a").click()
        sleep(2)

    # 访问该地址后，在产品超市页面点击产品超市
    def open_ProductsProducts(self):
        self.dr.get(self.base_url)
        # 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在产品超市页面点击产品超市
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)

    # 访问该地址后，在产品超市页面点击会员中心
    def open_ProductsCenter(self):
        self.dr.get(self.base_url)
        # 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在产品超市页面点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)

    # 访问该地址后，在产品超市页面点击会员中心之登录===============
    def open_ProductsCenterLogin(self):
        self.dr.get(self.base_url)
        # 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在产品超市页面点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)# 如果是没有登录，点击会员中心时，会跳转登录页面；这时需要在登录页面进行登录操作
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[1]/div[1]/div/input").send_keys(
            "18217276943")
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[1]/div[2]/div/input").send_keys(
            "123qwe")
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[1]/div[3]/div/input").send_keys(
            "8888")
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form[1]/div[2]/button").click()
        sleep(1)  # 点击会员中心操作
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()

    # 访问该地址后，在产品超市页面点击第一个产品进行立即投保
    def open_ProductsInsureImmediately(self):
        self.dr.get(self.base_url)
        # 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在产品超市页面点击立即投保
        self.dr.find_element_by_xpath("//*[@id='pageLists']/a[1]/div[1]/div[2]/button").click()
        sleep(2)

    # 访问该地址后，在产品超市页面点击第一个产品进行立即投保
    def open_ProductsInsureImmediately(self):
        self.dr.get(self.base_url)
        # 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在产品超市页面点击立即投保
        self.dr.find_element_by_xpath("//*[@id='pageLists']/a[1]/div[1]/div[2]/button").click()
        sleep(2)

    # 访问该地址后，在产品超市页面点击底部的关于我们
    def open_ProductsBottomAboutUs(self):
        self.dr.get(self.base_url)
        # 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在产品超市页面点击底部的关于我们
        self.dr.find_element_by_xpath("/html/body/footer/div/ul/li[1]/a").click()
        sleep(2)

    # 访问该地址后，在产品超市页面点击底部的常见问题
    def open_ProductsBottomFAQ(self):
        self.dr.get(self.base_url)
        # 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在产品超市页面点击底部的常见问题
        self.dr.find_element_by_xpath("/html/body/footer/div/ul/li[2]/a").click()
        sleep(2)

    # 访问该地址后，在产品超市页面点击底部的服务指南
    def open_ProductsBottomServiceGuide(self):
        self.dr.get(self.base_url)
        # 点击登录页面的关于我们
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)# 在产品超市页面点击底部的服务指南
        self.dr.find_element_by_xpath("/html/body/footer/div/ul/li[3]/a").click()
        sleep(2)

# a = BasePage()
# a.open_ProductsLogin()
# 被调用时，记得注释下代码R