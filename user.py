#!/usr/bin/env python3.6
class User:
    userList=[]
    def __init__(self,first_name,last_name,password,email,description):
        self.first_name=first_name
        self.last_name=last_name
        self.password=password
        self.email=email
        self.description=description
       
            
    def save_user(self):
        #SAVES A NEW CONTACT
        User.userList.append(self)

    def delete_user(self):
        #DELETES A USER
        User.userList.remove(self)

    @classmethod
    def find_by_password(cls,password):
        #FINDS THE USER USING PASSWORD
        for user in cls.userList:
            if user.password==password:
                return  user

    @classmethod
    def user_exists(cls,first_name):
        for user in User.userList:
            user.first_name=first_name
            return True

        return False