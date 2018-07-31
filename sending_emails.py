__author__ = 'Mitchell'


import smtplib
import random
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_address ="ib.wy.test01@gmail.com"
password = "FILL IN LATER"
to="ib.wy.test02@gmail.com"
server= smtplib.SMTP('smtp.gmail.com', 587)
# random_number=str(random.random())



#message = """From:ib.wy.test01@gmail.com To:ankit.tiwari@webyog.com  Subject: SMTP e-mail test
#This is a test e-mail message. """


#Breaks the MIME into a dictionary
msg = MIMEMultipart()

#All this goes into the MIMEMultipart for the msg
msg['From'] = from_address
msg['To'] = to
msg['Subject'] = "Python email -a "+ str(time.time())
body = "Python test mail"

html = """<h1> THis is a test html email <img src = "https://lh3.googleusercontent.com/Vct_XSpNfhherziE-h0mSSpbrJf2jYM1nvPO2PVkcIECnqqUHCf-2-5j8EObefEmS0o7=w300">

"""

#Method to attach the MIME
#msg.attach(MIMEText(body, 'plain'))
#String conversion from a dictionary

msg.attach(MIMEText(html,'html'))

content = str(msg)

def sendmail():
    try:
        server.starttls()
        print("test print")
        server.login(user=from_address,password=password)
        server.sendmail(from_address,to,msg=content)
        print("Email sent to:"+ to)
    except:
        print("Script failed")

sendmail()
