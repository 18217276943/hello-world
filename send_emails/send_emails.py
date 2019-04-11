# 发邮件？
# 1. 登录mail.126.com/  user/pawd  接收：标题，正文 附件
# 2. 客户端：foxmail user/pawd 协议：SMTP POP3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送邮箱服务器
smtpserver = 'smtp.126.com'
# 发送邮箱用户/密码
user = 'testingwtb@126.com'
password = 'a123456'
# 发送邮箱
sender = 'testingwtb@126.com'
# 接收邮箱
receiver = 'testingwtb@126.com'
# 发送邮件主题
subject = '自动发邮件Python email test'
# 编写 HTML 类型的邮件正文
msg = MIMEText('<html><h1>你好！ </h1></html>','html','utf-8')
msg['Subject'] = Header(subject,'utf-8')

# 连接发送邮件(动作)
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.ehlo()
smtp.starttls()
smtp.login(user,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()

'''
* 自己的邮箱（username,password）
* 对方的邮箱（账号）
* 邮件（标题，正文，附件）

mail.qq.com
mail.126.com

foxamil(服务器：smtp.126.com/pop3.126.com)
'''