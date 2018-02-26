#! /usr/bin/env python3
"""
Script to send mail from command line
Usage: python3 send_mail.py <subject> <content> <to_address>

author: cuongnb14@gmail.com
""" 

import smtplib
from sys import argv

subject = argv[1]
content = argv[2].replace("\\n", "\n")

from_addr = 'demo@gmail.com'
to_addrs  = argv[3]

msg = 'Subject: {}\n\n{}'.format(subject, content)
username = 'demo@gmail.com'
password = 'passdemo'

print("Sending... mail to {}".format(to_addrs))

# Example for gmail, change to your server mail.
server = smtplib.SMTP('smtp.gmail.com:587')
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
