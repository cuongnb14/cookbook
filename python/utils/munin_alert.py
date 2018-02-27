#! /usr/bin/env python3
"""
Script to send email alert for munin

Munin Config: munin.conf
contact.admin.command | /path/to/munin_alert.py
contact.admin.max_messages 1

@author: cuongnb14@gmail.com 
"""

import smtplib
import fileinput
import logging

logger = logging.getLogger('munin_alert')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('munin_alert.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

subject = "Munin Alert"
content = ""

from_addr = 'munin@gmail.com'
to_addrs = "cuongnb@gmail.com"

try:
    for line in fileinput.input():
        content = content + line + "\n"

    msg = 'From: {}\nSubject: {}\n\n{}'.format(from_addr, subject, content)
    username = from_addr
    password = '123456'

    print("Sending... mail to {}".format(to_addrs))

    logger.info("================================================")
    logger.info("Sending... mail to {}".format(to_addrs))
    logger.info("------------------------------------------------")
    logger.info("Message \n{}".format(msg))

    # Example for gmail, change to your server mail.
    server = smtplib.SMTP('mail.gmail.com:587')
    # identify ourselves, prompting server for supported features
    server.ehlo()
    # If you can encrypt this session, do it
    if server.has_extn('STARTTLS'):
        server.starttls()
        # re-identify ourselves over TLS connection
        server.ehlo()

    server.login(username, password)
    server.sendmail(from_addr, to_addrs, msg)
    server.quit()
except Exception:
    logger.exception()

