#!/usr/bin/env python3.6
import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
         '''
        self.user=Credentials("dynamodenis","987654321",'dmbugus@gmail.com',"hello world")


    def test_init_(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.user.username,"dynamodenis")
        self.assertEqual(self.user.password,"987654321")
        self.assertEqual(self.user.email,"dmbugus@gmail.com")
        self.assertEqual(self.user.details,"hello world")


    def test_save_credentials(self):
        self.user.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        '''
            tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list=[]


    def test_save_multiple_user(self):
        '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
        '''
        self.user.save_credentials()
        newUser=Credentials('mwangijohn','000000000','much@sept.com','twitter account')
        newUser.save_credentials()
        denis=Credentials('mwangijohn','000000000','much@sept.com','twitter account')
        denis.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),3)


    def test_find_by_password(self):
        self.user.save_credentials()
        newUser=Credentials('mwangijohn','000000000','much@sept.com','twitter account')
        newUser.save_credentials()
        
        find_user=Credentials.find_by_password('987654321')
        self.assertEqual(find_user.password,self.user.password)

    def test_delete_credentials(self):
        self.user.save_credentials()
        newUser=Credentials('mwangijohn','000000000','much@sept.com','twitter account')
        newUser.save_credentials()

        self.user.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_user_exists(self):
        self.user.save_credentials()
        newUser=Credentials('mwangijohn','000000000','much@sept.com','twitter account')
        newUser.save_credentials()

        credentials_exist=Credentials.user_exists("dynamodenis")
        self.assertTrue(credentials_exist)

    def test_display_users(self):
        display=Credentials.display_users()
        self.assertEqual(display,Credentials.credentials_list)


if __name__=="__main__":
    unittest.main()
