"""
Write a function that takes an email address, a string, and a list argument. 
It should return an email message addressed to the email address passed as the 
first argument, with the second argument as the message body. If the list is 
non-empty, then each list item should be treated as the name of a file and the 
corresponding file should be attached (with an appropriate MIME type) to the message.

Please include any files to attach in the same folder as your program.  
There is no need to send it as an email with smtp, though you may wish to 
print it as a string as a part of testing.
"""

import os
import email
import mimetypes
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def create_email_msg(address, body, file_list=None):
    msg = None
    if file_list is not None:
        msg = MIMEMultipart()
        for file in file_list:
            content_type, encoding = mimetypes.guess_type(file)
            type, format = content_type.split("/")
            print(type)
            if (type == "image"):
                fp = open(file, 'rb')
                part = MIMEImage(fp.read())
                fp.close()
            elif (type == "text"):
                fp = open(file)
                part = MIMEText(fp.read())
                fp.close()
            msg.attach(part)
    else:
        msg = email.message_from_string(body)
    
    msg['To'] = address
    msg['From'] = "ceeblet@gmail.com"
    #print(msg.as_string())
    return msg





