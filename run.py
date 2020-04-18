#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

#USERS
def create_user(fname,lname,password,email,details):
    newUser=User(fname,lname,password,email,details)
    return newUser

def save_users(user):
    user.save_user()

def delete_user(user):
    user.delete_user()

def find_user(password):
    User.find_by_password(password)

def search_user(first_name):
    User.user_exists(first_name)

def display_users():
    User.display_users()

#CREDENTIALS
def create_credentials(username,password,email,details):
    newCredential=Credentials(username,password,email,details)
    return newCredential

def save_credential(user):
    user.save_credentials()

def delete_credentials(user):
    user.delete_credentials()

def find_credential(password):
    Credentials.find_by_password(password)

def search_user(username):
    Credentials.user_exists(username)

def display_credentials():
    Credentials.display_users()
def main():
    print('''Hello use the codes below to continue:
             CU--create user credentials.
             SC--to save ready credentials.
             DC--to display saved credentials.
             DEL--to delete unused credentials.
             EX--to exit''')
    
    while True:
        print('''Hello use the codes below to continue:
             CU--create user credentials.
             SC--to save ready credentials.
             GET--to search for your credentials.
             DEL--to delete unused credentials.
             EX--to exit''')
        print('Type code to continue:')
        code=input().lower()

        if code=='cu':
            print('First Name:')
            first_name=input()

            print('Second Name:')
            last_name=input()

            print('Password:')
            password=input()

            print('Email:')
            email=input()

            print('Details or Description or Where used:')
            descrption=input()

            save_users(create_user(first_name,last_name,password,email,descrption))
            print('\n')
            print(f'New credentials created==> Username: {first_name} {last_name}, Email:{email}, user Password:{password}')
            print('Go ahead and save the credentials using SC code beow')
            print('\n')

        elif code=='sc':
            print('Please fill the details below to save your credentials:')
            print('Your Username:')
            username=input()

            print('Password:')
            password=input()

            print('Email Address:')
            email=input()

            print('Details:')
            details=input()

            save_credential(create_credentials(username,password,email,details))
            print('\n')
            print(f'{username} credentials successfully saved.')
            print('\n')

        #DISPLAYS ALL THE USERS SAVED CREDENTIALS
        elif code=='get':
            print('To retrieve your credentials type ')














if __name__=="__main__":
    main()
