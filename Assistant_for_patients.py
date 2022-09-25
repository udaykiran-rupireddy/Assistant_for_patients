from datetime import datetime

import pytz
import time

tz_kolkata = pytz.timezone('Asia/Kolkata')


import smtplib
import json
from email.message import EmailMessage
from urllib.request import urlopen
url='http://ipinfo.io/json'
response=urlopen(url)
data=json.load(response)

def email_alert(subject,body,to):
    msg =EmailMessage()
    msg.set_content("city : "+data['city']+'  region : '+data['region']+'  country : '+data['country']+'  location : '+data['loc'])
    msg['subject']=subject
    msg['to']=to

    user="sender_mail@gmail.com"
    msg['from']=user 
    password="sender_password"

    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)

    server.quit()


while(True):
    datetime_kolkata = datetime.now(tz_kolkata)
    #print(datetime_kolkata)
    print("time:",datetime_kolkata.strftime("%H:%M:%S"))
    time.sleep(1)
    if (datetime_kolkata.strftime("%H:%M:%S")=="23:52:40" ): # time decided for medicine 1
        print("take medicine 1")
        m=int(input())#gets value 1 if button pressed else 0 
        if (m==1):
            print("medicine taken")
        else:
            print("sending message to care taker")
            if _name=='main_':
                email_alert("medicine 1 not taken ",data,"recipient_mail@gmail.com")

    if (datetime_kolkata.strftime("%H:%M:%S")=="12:00:00" ):
        print("take medicine 2")
        p=int(input())#gets value 1 if button pressed else 0 
        if (p==1):
            print("medicine taken")
        else:
            print("sending message to care taker")
            if _name=='main_':
                email_alert("medicine 1 not taken ",data,"recipient_mail@gmail.com")

    if (datetime_kolkata.strftime("%H:%M:%S")=="16:00:00" ):
        print("take medicine 3")
        q=int(input())#gets value 1 if button pressed else 0 
        if (q==1):
            print("medicine taken")
        else:
            print("sending message to care taker")
            if _name=='main_':
                email_alert("medicine 1 not taken ",data,"recipient_mail@gmail.com")

    if (datetime_kolkata.strftime("%H:%M:%S")=="21:00:00" ):
        print("take medicine 4")
        r=int(input())#gets value 1 if button pressed else 0 
        if (r==1):
            print("medicine taken")
        else:
            print("sending message to care taker")
            if _name=='main_':
                email_alert("medicine 1 not taken ",data,"recipient_mail@gmail.com")