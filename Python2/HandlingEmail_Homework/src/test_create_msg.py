import unittest
import os
import email
import mimetypes
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from create_msg import create_email_msg

class messageTest(unittest.TestCase):
    def setUp(self):
        self.sendTo = "ceeblet@gmail.com"
        self.sendFrom = "ceeblet@gmail.com"
        self.message = "test message from tester"
        
    def send_email_msg(self, msg):
        srv = smtplib.SMTP('mail.oreillyschool.com', 25)
        srv.sendmail(msg['From'], msg['To'], msg.as_string())
        srv.quit()
        
    def test_create_msg(self):
        msg = create_email_msg(self.sendTo, self.message)
        self.assertEqual(msg["To"], self.sendTo, "To fields don't match")
        self.assertEqual(msg["From"], self.sendFrom, "From fields don't match")
        #print(msg.as_string())
        #self.send_email_msg(msg)
    
#    def test_create_msg_with_attachments(self):
    def test_create_msg_multipart(self):
        file_list = ["python-logo.png", "example-email.txt"]  
        msg = create_email_msg(self.sendTo, self.message, file_list)
        self.assertEqual(msg["To"], self.sendTo, "To fields don't match")
        self.assertTrue(msg.is_multipart())
        #print(msg.get_payload())
        #self.assertEqual(msg.get_payload(), "[<email.mime.image.MIMEImage object at 0x000000000220BD30>, <email.mime.text.MIMEText object at 0x000000000222D400>]", "payload not equal")
        #self.assert_(("MIMEImage" in msg.get_payload()), "payload not equal")
        #self.send_email_msg(msg)
        #print(msg)

    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
