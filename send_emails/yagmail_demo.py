import yagmail


# 连接邮箱服务器
yag = yagmail.SMTP(user="testingwtb@126.com",
                   password="a123456",
                   host="smtp.126.com")


report_text = open("d://result.html","rb")




# 邮箱正文
contents = ['This is the body,and here is just text http://somedomain/image.png',
            'You can find an audio file attached.']

# 发送邮件
# 接收者，标题，正文，附件
yag.send('testingwtb@126.com','yag发送附件',contents,["d://result.html"])