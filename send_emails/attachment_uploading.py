import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

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
subject = '发送邮件附件'

# 发送的附件
sendfile = open('D://result.html','rb').read()
att = MIMEText(sendfile,'base64','utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="result.html"'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)


# 连接发送邮件(动作)
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.ehlo()
smtp.starttls()
smtp.login(user,password)
smtp.sendmail(sender,receiver,msgRoot.as_string())
smtp.quit()

'''
* 自己的邮箱（username,password）
* 对方的邮箱（账号）
* 邮件（标题，正文，附件）

mail.qq.com
mail.126.com

foxamil(服务器：smtp.126.com/pop3.126.com)
'''