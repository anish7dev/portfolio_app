import smtplib,ssl
import os

def send_mail(msg):
    host="smtp.gmail.com"
    port= 465


    username="anishchoudhary1998@gmail.com"
    password=os.getenv("PASSWORD")

    receiver="anishchoudhary1998@gmail.com"
    context=ssl.create_default_context()

    # message="""\
    # Subject: Status
    #     How are you?
    # """

    with smtplib.SMTP_SSL(host=host,port=port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,msg)