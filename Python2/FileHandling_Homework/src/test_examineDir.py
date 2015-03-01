'''
Created on Oct 31, 2013

@author: cbrown
'''
import unittest
from examineDir import examineDir
import os
import shutil

PATHSTEM = "v:\\workspace\\FileHandling_Homework\\src\\"
DIR1 = PATHSTEM+"dir1\\"
DIR2 = PATHSTEM+"dir2\\"

class TestExamineDir(unittest.TestCase):

    def setUp(self):
        os.mkdir(DIR1)
        os.mkdir(DIR2)
        self.file_names1 = ["file.new", "file.txt", "file2.txt", "file2.pdf", "file3.txt"]
        for fn in self.file_names1:
            f = open(DIR1+fn, "w")
            f.close()
        self.file_names2 = ["file.old", "file.pdf", "file2.pdf", "file2.txt", "file3.pdf"]
        for fn in self.file_names2:
            f = open(DIR2+fn, "w")
            f.close()

    def tearDown(self):
        os.chdir(PATHSTEM)
        shutil.rmtree(DIR1)
        shutil.rmtree(DIR2)

    def testExamineDir1(self):
        os.chdir(DIR1)
        expected_types = {"new": 1, "txt": 3, "pdf": 1}
        file_types = examineDir()
        self.assertDictEqual(expected_types, file_types, "dir1, number of file types are not equal")
           
    def testExamineDir2(self):
        os.chdir(DIR2)
        expected_types = {"old": 1, "pdf": 3, "txt": 1}
        file_types = examineDir()
        self.assertDictEqual(expected_types, file_types, "dir2, number of file types are not equal")
           

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()