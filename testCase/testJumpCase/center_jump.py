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

# =============================会员中心的跳转=============================

    # 访问该地址后，跳转首页页面
    def open_homePage(self):
        self.dr.get(self.base_url)
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
        sleep(2)# 登录后再次点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)

    # 访问会员中心后，跳转首页页面
    def open_centerHomepage(self):
        self.dr.get(self.base_url)
        # 点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)# 会员中心页面点击首页
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[1]/a").click()
        sleep(2)

    # 访问会员中心后，跳转产品超市页面
    def open_centerProduct(self):
        self.dr.get(self.base_url)
        # 点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)# 会员中心页面点击产品超市
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[2]/a").click()
        sleep(2)

    # 访问会员中心后，点击图标进行跳转
    def open_centerIcon(self):
        self.dr.get(self.base_url)
        # 点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)# 会员中心页面点击中国太平图标
        self.dr.find_element_by_xpath("/html/body/header/a/div").click()
        sleep(2)

    # 访问会员中心后，点击会员中心
    def open_centerCenter(self):
        self.dr.get(self.base_url)
        # 点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)# 会员中心页面点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)

    # 访问会员中心后，点击会员中心
    def open_centerCenter(self):
        self.dr.get(self.base_url)
        # 点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)# 会员中心页面点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)

    # 访问会员中心后，点击退出登录
    def open_centerLogout(self):
        self.dr.get(self.base_url)
        # 点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)# 会员中心页面点击退出登录
        self.dr.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[3]/a").click()
        sleep(2)

    # 访问会员中心后，点击crumbs面包屑的会员中心
    def open_centerCrumbsCenter(self):
        self.dr.get(self.base_url)
        # 点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)# 会员中心页面点击面包屑的会员中心
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/a[2]").click()
        sleep(2)

    # 访问会员中心后，点击crumbs面包屑的首页
    def open_centerCrumbsHomepage(self):
        self.dr.get(self.base_url)
        # 点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)# 会员中心页面点击面包屑的首页
        self.dr.find_element_by_xpath("/html/body/div[2]/div[1]/a[1]").click()
        sleep(2)

    # 访问会员中心后，点击我的订单
    def open_centerMyOrder(self):
        self.dr.get(self.base_url)
        # 点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)# 会员中心页面点击我的订单
        self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/dl[2]/dd[2]/a/span/i").click()
        sleep(2)

    # 访问会员中心后，点击我的保单
    def open_centerMyPolicy(self):
        self.dr.get(self.base_url)
        # 点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)# 会员中心页面点击我的保单
        self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/dl[2]/dd[3]/a/span/i").click()
        sleep(2)

    # 访问会员中心后，点击常用联系人
    def open_centerTopContacts(self):
        self.dr.get(self.base_url)
        # 点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)# 会员中心页面点击常用联系人
        self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/dl[2]/dd[4]/a/span/i").click()
        sleep(2)

    # 访问会员中心后，点击保单批改下面的申请批改
    def open_centerApplyForCorrecting(self):
        self.dr.get(self.base_url)
        # 点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)# 会员中心页面点击保单批改下面的申请批改
        self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/dl[2]/dd[5]/a/span/i").click()
        sleep(2)
        self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/dl[2]/dd[5]/ul/li[1]/a/span/i").click()
        sleep(2)

    # 访问会员中心后，点击保单批改下面的我的批改
    def open_centerMyGrade(self):
        self.dr.get(self.base_url)
        # 点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)# 会员中心页面点击保单批改下面的我的批改
        self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/dl[2]/dd[5]/a/span/i").click()
        sleep(2)
        self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/dl[2]/dd[5]/ul/li[2]/a/span/i").click()
        sleep(2)

    # 访问会员中心后，点击理赔服务下面的申请理赔
    def open_centerApplyForClaims(self):
        self.dr.get(self.base_url)
        # 点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)# 会员中心页面点击理赔服务下面的申请理赔
        self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/dl[2]/dd[6]/a/span").click()
        sleep(2)
        self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/dl[2]/dd[6]/ul/li[1]/a/span/i").click()
        sleep(2)

    # 访问会员中心后，点击理赔服务下面的我的理赔
    def open_centerMyClaims(self):
        self.dr.get(self.base_url)
        # 点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)# 会员中心页面点击理赔服务下面的我的理赔
        self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/dl[2]/dd[6]/a/span").click()
        sleep(2)
        self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/dl[2]/dd[6]/ul/li[2]/a/span/i").click()
        sleep(2)

    # 访问会员中心后，点击理赔服务下面的我的暂存
    def open_centerMyHold(self):
        self.dr.get(self.base_url)
        # 点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)# 会员中心页面点击理赔服务下面的我的暂存
        self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/dl[2]/dd[6]/a/span").click()
        sleep(2)
        self.dr.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/dl[2]/dd[6]/ul/li[3]/a/span/i").click()
        sleep(2)

    # 访问会员中心后，点击会员中心下面的关于我们
    def open_centerBottomAboutUs(self):
        self.dr.get(self.base_url)
        # 点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)# 会员中心页面点击底部的关于我们
        self.dr.find_element_by_xpath("/html/body/footer/div/ul/li[1]/a").click()
        sleep(2)

    # 访问会员中心后，点击会员中心下面的常见问题
    def open_centerBottomFAQ(self):
        self.dr.get(self.base_url)
        # 点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)# 会员中心页面点击底部的常见问题
        self.dr.find_element_by_xpath("/html/body/footer/div/ul/li[2]/a").click()
        sleep(2)

    # 访问会员中心后，点击会员中心下面的服务指南
    def open_centerBottomServiceGuide(self):
        self.dr.get(self.base_url)
        # 点击会员中心
        self.dr.find_element_by_xpath("/html/body/header/div[2]/ul/li[3]/a").click()
        sleep(2)# 会员中心页面点击底部的服务指南
        self.dr.find_element_by_xpath("/html/body/footer/div/ul/li[3]/a").click()
        sleep(2)

# a = BasePage()
# a.open_ProductsLogin()
# 被调用时，记得注释下代码R