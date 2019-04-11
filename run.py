import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

# from testAdd import Addtest
# from testSub import Subtest

# 这个方法的存在就是:批量执行用例。前面是文件放置路径，后面是文件保存格式

suit = unittest.defaultTestLoader.discover(start_dir="testCase",pattern="test_*.py")

# ===================定义发送邮件——文件内容===================
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header("专区pc测试报告",'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login("testingwtb@126.com","a123456")
    smtp.sendmail("testingwtb@126.com","testingwtb@126.com",msg.as_string())
    smtp.quit()
    print("email has send out !")

# ===================定义发送邮件——附件===================
def send_attchment(file_new):
    # 发送的附件
    sendfile = open(report, 'rb').read()
    att = MIMEText(sendfile, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="result.html"'

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = "发送附件"
    msgRoot.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect("smtp.qq.com")
    smtp.login("2467346003@qq.com", "sowpqyenyygrecie")
    smtp.sendmail("2467346003@qq.com", "2467346003@qq.com", msgRoot.as_string())
    smtp.quit()
    print("email has send out !")

# 如果想要用例先执行，那么改文件名/类名/方法名字/“a 到 z /A Z/0 9”
# AA_TEST.PY / ZZ.TEST.PY
# 套件的话就直接写就好了

if __name__ == '__main__':
    # unittest.main()

    # 使用html报表
    now_time = time.strftime("%Y_%m_%d %H_%M_%S")
    # 报告名称
    report = "report"+now_time+"result.html"
    f = open(report,'wb')
    runner = HTMLTestRunner(
        stream=f,
        verbosity=1,
        title="专区pc功能测试报告",
        description="运行环境：Windows/Chrome,Author:朝阳")

    runner.run(suit)
    f.close()
    # 邮件发送功能调用
    send_attchment(report)