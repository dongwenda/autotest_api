# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
class SendEmail:
    global sendUser
    global emailHost
    global password
    sendUser = "xxxxx@163.com"
    emailHost = "smtp.163.com"
    password = "xxxxxxx"
    def send_mail(self,userList,subject,content):
        user = "Mushishi"+"<"+sendUser+">"
        msg = MIMEText(content,_subtype='plain',_charset='utf-8')
        msg['Subject'] = subject
        msg['From'] = user
        msg['To'] = ";".join(userList)
        server = smtplib.SMTP()
        server.connect(emailHost)
        server.login(sendUser,password)
        server.sendmail(user,userList,msg.as_string())
        server.close()

    def send_main(self,passList,failList):
        passNum = float(len(passList))
        failNum = float(len(failList))
        countNum = passNum + failNum

        passRes = "%.2f%%" %(passNum/countNum*100)
        failRes = "%.2f%%" %(failNum/countNum*100)

        userList = ['xxxxx@qq.com', 'xxxxxx@163.com']
        subject = "接口自动化测试报告"
        content = "运行接口个数为%s个，通过个数为%s个，失败个数为%s，通过率为%s，失败率为%s" %(countNum,passNum,failNum,passRes,failRes)

        self.send_mail(userList,subject,content)

if __name__ == '__main__':
    sen = SendEmail()
    userList = ['xxxxx@qq.com','xxxxxx@163.com']
    subject = "主题"
    content = "内容"
    sen.send_mail(userList,subject,content)
