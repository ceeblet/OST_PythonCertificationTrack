"""
Email message handling module: contains logic to store and retrieve
email messages using a MySQL relational database.
"""
from database import login_info
import mysql.connector as msc
from email import message_from_string
from email.utils import parsedate_tz, mktime_tz, parseaddr
from datetime import datetime, timedelta
import settings

conn = msc.Connect(**login_info)
curs = conn.cursor()

def store(msg):
    """
    Stores an email message, if necessary, returning its primary key.
    """
    message_id = msg['message-id']
    #print("messageid is: {0}".format(message_id))
    #text = msg.as_string()
    curs.execute("SELECT msgID FROM jotd_emails WHERE msgMessageID=%s", (message_id, ))
    result = curs.fetchone()
    if result:
        return result[0]
    date = msg['Date']
    name, email = parseaddr(msg['To'])
    #dt = datetime.fromtimestamp(mktime_tz(parsedate_tz(date)))
    #dt = date
    #text = msg.as_string()
    text = msg.get_payload()
    curs.execute("""INSERT INTO jotd_emails 
                    (msgMessageID, msgDate, msgRecipientName, msgRecipientAddress, msgText) 
                    VALUES (%s, %s, %s, %s, %s)""",
                    (message_id, date, name, email, text))
    conn.commit()
    curs.execute("SELECT msgID FROM jotd_emails WHERE msgMessageID=%s", (message_id, ))
    #return curs.fetchone()[0]
    return curs.fetchone()
