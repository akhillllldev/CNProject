import smtplib
import csv
from email.mime.text import MIMEText


smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'email'
password = 'password'
sender = 'test@test.com'

msg = MIMEText(f'''
<p>Hi</p>
<div>&nbsp;</div>
<div>This is a Test Mail.</div>
<div>&nbsp;</div>
<div>&nbsp;</div>
<p>Best Regards,</p>
<div><span style="color: #3d85c6;"><strong>Akhil Surendran</strong></span></div>
<div><span style="color: #3d85c6;"><strong>17BCE7087</strong></span></div>''', 'html')

targets = ['recipient']
# print(msg)
# msg['Subject'] = 'Voter Details - OSC Election 2019'
# msg['From'] = 'support@oscvitap.co.in'
# msg['To'] = target
# server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
# server.login(username, password)
# server.sendmail(sender, target, msg.as_string())


# username = 'ritwik.badola@vitap.ac.in'


# password = ''
# sender = '<no-reply@ritwik.badola@vitap.ac.in>'
# targets = ['ritwik.badola@vitap.ac.in']

# x = "Anything 123"
# msg = MIMEText(f'{x}')
# msg['Subject'] = 'OSC ka kuch to '
# msg['From'] = sender
# msg['To'] = ', '.join(targets)
#
server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()
print("Mail Successfully Sent!")
