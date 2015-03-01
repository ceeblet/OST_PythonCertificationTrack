"""
Joke of the Day: contains logic to read data from settings.py
and create and store messages in a MySQL database in the jotd_emails table.
"""

from create_msg import create_email_msg
from maildb import store
from datetime import timedelta
import settings

def store_messages():    
    count = 1
    body = "This is a test message."
    while count <= settings.DAYCOUNT:
        for name, address in settings.RECIPIENTS:
            dt = settings.STARTTIME + timedelta(days=count)
            store((create_email_msg(address, body, dt)))
        count += 1
