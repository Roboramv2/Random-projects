import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mails=['example1@gmail.com', 'example2@outlook.com']
outacc = "__outlook email id__"
outpwd = "__outlook password__"

def sendit(txt, sub):
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(outacc, outpwd)
    for mail in mails:
        msg = MIMEMultipart()
        msg['From']=outacc
        msg['To']= mail
        msg['Subject']=sub
        msg.attach(MIMEText(txt, 'plain'))
        s.send_message(msg)
        del msg
