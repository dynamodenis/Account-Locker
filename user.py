#!/usr/bin/env python3.6
class User:
    def __init__(self,first_name,last_name,password,email,description):
       self.first_name=first_name
       self.last_name=last_name
       self.password=password
       self.email=email
       self.description=description
new=User("Denis","Mbgua","093099308","dmbugua66@gmail.com",'Slack Account')
print(new.email) 