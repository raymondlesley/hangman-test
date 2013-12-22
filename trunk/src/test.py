'''
Created on 20 Dec 2013

@author: L14202
'''
import unittest
from word import Word

class Test(unittest.TestCase):


    def testWord(self):
        word = Word("something")
        self.assertTrue(word.guessed_for_display() == "_ _ _ _ _ _ _ _ _ ")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCLS']
    unittest.main()