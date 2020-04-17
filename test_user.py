#!/usr/bin/env python3.6
import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
         '''
        self.user=User("Denis","Mbugua","093099308","dmbugua66@gmail.com",'Slack Account')

    def test_init_(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.user.first_name,"Denis")
        self.assertEqual(self.user.last_name,"Mbugua")
        self.assertEqual(self.user.password,"093099308")
        self.assertEqual(self.user.email,"dmbugua66@gmail.com")
        self.assertEqual(self.user.description,"Slack Account")


if __name__=="__main__":
    unittest.main()
