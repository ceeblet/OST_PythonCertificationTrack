"""
Modify the classFactory.py source code so that the DataRow class returned by the build_row function has another method:
    retrieve(self, curs, condition=None)
self is (as usual) the instance whose method is being called, curs is a database cursor on an existing database connection, 
and condition (if present) is a string of condition(s) which must be true of all received rows.
The retrieve method should be a generator, yielding successive rows of the result set until it is completely exhausted. 
Each row should be a next object of type DataRow
"""
import unittest
from classFactory import build_row
import mysql.connector
from database import login_info

class DBTest(unittest.TestCase):
    def setUp(self):
        C = build_row("testUser", "id name email")
        self.c = C([1, "Steve Holden", "steve@holdenweb.com"])
        self.db = mysql.connector.Connect(**login_info)
        self.cursor = self.db.cursor()
        sql = 'CREATE TABLE testUser (\
        id int NOT NULL,\
        name varchar(30) NOT NULL,\
        email varchar(30) NOT NULL,\
        PRIMARY KEY (id)     );'
        self.cursor.execute(sql)
        sql = 'INSERT INTO testUser VALUES\
        (1, "Steve Holden", "steve@holdenweb.com")'
        self.cursor.execute(sql)
        
    def test_attributes(self):
        self.assertEqual(self.c.id, 1)
        self.assertEqual(self.c.name, "Steve Holden")
        self.assertEqual(self.c.email, "steve@holdenweb.com")
        
    def test_repr(self):
        self.assertEqual(repr(self.c), "(1, 'Steve Holden', 'steve@holdenweb.com')")
        
    def test_retrieve(self):
        expected_rows = set()
        sql = 'SELECT * FROM testUser;'
        self.cursor.execute(sql)
        for fetchrow in self.cursor.fetchall():
            expected_rows.add(repr(fetchrow))
        
        observed_rows = set()
        for retrieverow in self.c.retrieve(self.cursor):
            observed_rows.add(repr(retrieverow))
            
        self.assertEqual(expected_rows, observed_rows)
        
    def test_retrieve_with_condition(self):
        condition = "name='{0}'".format(self.c.name)
        expected_rows = set()
        sql = 'SELECT * FROM testUser WHERE name="{0}";'.format(self.c.name)
        self.cursor.execute(sql)
        for fetchrow in self.cursor.fetchall():
            expected_rows.add(repr(fetchrow))
        
        observed_rows = set()
        for retrieverow in self.c.retrieve(self.cursor, condition):
            observed_rows.add(repr(retrieverow))
            
        #print("Problem? ", (expected_rows, observed_rows))
        #print("Types:", type(expected_rows.pop()), type(observed_rows.pop()))
        self.assertEqual(expected_rows, observed_rows)
    
    def tearDown(self):
        sql = 'DROP TABLE testUser'
        self.cursor.execute(sql)
        
if __name__ == "__main__":
    unittest.main()

