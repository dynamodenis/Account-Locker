#!/usr/bin/env python3.6
class Credentials:
    credentials_list=[]
    def __init__(self,username,password,email,details):
        self.username=username
        self.password=password
        self.details=details
        self.email=email

        

    def save_credentials(self):
        #SAVES A NEW USER
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        #DELETES A USER
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_users(cls):

        return cls.credentials_list
    @classmethod
    def find_by_password(cls,password):
        #FINDS THE USER USING PASSWORD
        for user in cls.credentials_list:
            if user.password==password:
                return  user

    @classmethod
    def user_exists(cls,username):
        for user in Credentials.credentials_list:
            user.username=username
            return True

        return False

    # def save_contact(self):
    #     #this saves a new contact
