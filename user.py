#!/usr/bin/env python3.6
class User:
    userList=[]
    def __init__(self,first_name,last_name,password,email,description):
        self.first_name=first_name
        self.last_name=last_name
        self.password=password
        self.email=email
        self.description=description
       
            
    def save_contact(self):
        #SAVES A NEW CONTACT
        User.userList.append(self)