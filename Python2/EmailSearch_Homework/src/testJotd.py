"""
Test jotd email generation and storage.

NOTE: This test creates the jotd_emails table, dropping any
previous version and should leave it empty. DANGER: this test
will delete any existing jotd_emails table.
"""

import mysql.connector as msc
from database import login_info
from datetime import timedelta
import unittest
import os
import jotd
import time

conn = msc.Connect(**login_info)
curs = conn.cursor()

TBLDEF = """\
CREATE TABLE jotd_emails (
    msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
    msgMessageID VARCHAR(128),
    msgDate DATETIME,
    msgRecipientName VARCHAR(128),
    msgRecipientAddress VARCHAR(128),
    msgText LONGTEXT
)"""

class testJokeOfTheDay(unittest.TestCase):
    def setUp(self):
        """
        Creates settings.py file that contains recipients, start date
        and number of days related to sending Joke of the Day emails. Each
        email will be stored in the database.
        
        DANGER: Any existing message table WILL be lost.
        """
        curs.execute("DROP TABLE IF EXISTS jotd_emails")
        conn.commit()
        curs.execute(TBLDEF)
        conn.commit()
        self.recipients = [("ceeblet", "ceeblet@gmail.com"), ("ceeblet+ostusr2", "ceeblet+ostusr2@gmail.com"), ("ceeblet+ostusr3", "ceeblet+ostusr3@gmail.com")]
        self.message_count = 0
        
    def test_number_emails_per_user(self):
        """
        Verifies the correct number of emails were generated for a single user.
        """
        jotd.settings.DAYCOUNT = 10
        jotd.store_messages()
        
        curs.execute("SELECT COUNT(*) FROM jotd_emails WHERE msgRecipientAddress='{0}'".format(jotd.settings.RECIPIENTS[0][1]))
        msg_count = curs.fetchone()[0]
        self.assertEqual(jotd.settings.DAYCOUNT, msg_count)
        
    def test_number_emails_per_all_users(self):
        """
        Verifies the correct number of emails were generated for a all users.
        """
        jotd.settings.DAYCOUNT = 5
        jotd.store_messages()
        
        curs.execute("SELECT COUNT(*) FROM jotd_emails")
        msg_count = curs.fetchone()[0]
        self.assertEqual((jotd.settings.DAYCOUNT * len(self.recipients)), msg_count)
        
    def test_timings_small(self):
        """
        Tests timeing of email storage based on DAYCOUNT.
        """
        jotd.settings.DAYCOUNT = 5
        start = time.time()
        jotd.store_messages()
        end = time.time()
        interval1 = end - start
        print("Time to complete: ", interval1)
        
        jotd.settings.DAYCOUNT = 10
        start = time.time()
        jotd.store_messages()
        end = time.time()
        interval2 = end - start
        print("Time to complete: ", interval2)
        
        self.assertGreater(interval2, interval1)
        
    def test_timings_large(self):
        """
        Tests timeing of email storage based on DAYCOUNT.
        """
        jotd.settings.DAYCOUNT = 1
        start = time.time()
        jotd.store_messages()
        end = time.time()
        interval1 = end - start
        print("Time to complete: ", interval1)
        
        jotd.settings.DAYCOUNT = 100
        start = time.time()
        jotd.store_messages()
        end = time.time()
        interval2 = end - start
        print("Time to complete: ", interval2)
        
        self.assertGreater(interval2, interval1)

if __name__ == "__main__":
    unittest.main()
