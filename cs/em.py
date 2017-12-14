# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ----------1.跟发件相关的参数------
smtpserver = "smtp.qq.com"

port = 465  # 端口

sender = "2528148607@qq.com" #发送者
psw = "lbuswdisttotdiae"    #授权码密码
receiver = "2628749327@qq.com" #收件人

# ----------2.编辑邮件的内容------
# 读文件
file_path = "D:\\test\\sww\\result.html"  #报告的路劲
with open(file_path, "rb") as fp:
     mail_body = fp.read()

msg = MIMEMultipart()
msg["from"] = sender             #发件人
msg["to"] = receiver             #收件人
msg["subject"] = "这个我的主题"  #主题

# 正文
body = MIMEText(mail_body, "html", "utf-8")
msg.attach(body)
# 附件
att = MIMEText(mail_body, "base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename="test_report.html"'
msg.attach(att)

# ----------3.发送邮件------

try:
       smtp = smtplib.SMTP()
       smtp.connect(smtpserver)  # 连服务器
       smtp.login(sender, psw)
except:
      smtp = smtplib.SMTP_SSL(smtpserver, port)
      smtp.login(sender, psw)

smtp.sendmail(sender, receiver, msg.as_string())   # 发送
smtp.quit()




