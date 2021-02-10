#!/usr/bin/env python3
#-*- coding:utf-8 -*-

"""
send email from 
              host: shuzhan2021
              Authorization key: RCDVTTKLUFNHJVWI
           to
              1962610298@qq.com
"""

import sys, os
import smtplib
from email.mime.text import MIMEText

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/restart_ps'
sys.path.append(BASE_DIR)
# from restart_ps.Moudle_log import logger
from Moudle_log import logger


mail_host = 'smtp.163.com'
mail_user = 'shuzhan2021'
mail_pass = 'RCDVTTKLUFNHJVWI'
sender = 'shuzhan2021@163.com'
receivers = ['1962610298@qq.com']


# log in and send mail to receviers
def send_mail(title, content):
    message = MIMEText(content, 'plain', 'utf-8')
    # title of mail
    message['Subject'] = title
    # send message to receivers
    message['Form'] = sender
    # message of receviers
    message['To'] = receivers[0]

    try:
        smtpObj = smtplib.SMTP()
        # conn to server
        smtpObj.connect(mail_host, 25)
        # log in to server
        smtpObj.login(mail_user, mail_pass)
        # send mail to qq.com from 163
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        logger.info('email send successfully!')
    except smtplib.SMTPException as e:
        logger.error('email send error: ', e)


if __name__ == "__main__":

    send_mail('test', 'send mail test')

