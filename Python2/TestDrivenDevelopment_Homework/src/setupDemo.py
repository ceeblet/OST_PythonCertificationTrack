"""
Demonstration of setUp and tearDown.
The tests do not actually test anything - this is a demo.
"""
import unittest
import tempfile
import shutil
import glob
import os

class FileTest(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        #print("Created", self.dirname)
        os.chdir(self.dirname)
        
    def test_1(self):
        "Verify creation of files is possible."
        new_filenames = set(["this.txt", "that.txt", "the_other.txt"])
        for filename in (new_filenames):
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
            self.assertTrue(f.closed)
        existing_filenames = set(os.listdir(self.dirname))
        self.assertEqual(new_filenames, existing_filenames)
        
    def test_2(self):
        "Verify that the current directory is empty."
        self.assertEqual(glob.glob("*"), [], "Directory not empty")
        
    def test_3(self):
        "Verify size of binary file."
        filename = 'byte_file'
        bf = open(filename, 'wb')
        bf.write(b'X' * 1000000)
        bf.close()
        self.assertEqual(os.path.getsize(bf.name), 1000000)
        
    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)
        #print("Deleted", self.dirname)
        
if __name__ == "__main__":
    unittest.main()