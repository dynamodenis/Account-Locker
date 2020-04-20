#!/usr/bin/env python3.6
from user import User
from credentials import Credentials
import string
import random
import pyperclip
#USERS
def create_user(fname,lname,password,email,details):
    newUser=User(fname,lname,password,email,details)
    return newUser

def save_users(user):
    user.save_user()

def delete_user(user):
    user.delete_user()

def display_users():
    return User.display_users()

#CREDENTIALS
def create_credentials(username,password,email,details):
    new_credential=Credentials(username,password,email,details)
    return new_credential

def save_credentials(credentials):
    credentials.save_credentials()

def delete_credentials(credentials):
    credentials.delete_credentials()

def copy_credentials(password):
    password.copy_credential()

def find_credential(password):
    return Credentials.find_by_password(password)

def search_user(username):
    return Credentials.user_exists(username)

def display_credentials():
    return Credentials.display_users()
def main():
    while True:
        print('''Hello use the codes below to continue:
             CU--create user credentials.
             SC--to save ready credentials.
             GET--to search for your credentials.
             DC--to display saved credentials.
             DEL--to delete unused credentials.
             EX--to exit''')
        print('Type code to continue:')
        code=input().lower()

        if code=='cu':
            #CREATES NEW USER CREDENTIAL
            print('First Name:')
            first_name=input()

            print('Second Name:')
            last_name=input()

            print('For Password: type AUTO --to auto generate or INPUT --to generate your own password!')
            print("Type AUTO or INPUT")
            password_generate=input().lower()

            #THIS AUTO GENERATES
            if password_generate=='auto':
                print('Type password length!')
                size=int(input())
                def password(size=size,chars=string.ascii_uppercase+string.digits+string.ascii_lowercase):
                    return ''.join(random.choice(chars) for _ in range(size))
                password=password()
                print(f"Congratulations here is your password: {password}")
                print('-'*40)

            elif password_generate=='input':
                print('Type your password:')
                password=input()

            else:
                print("-----Unexpected input please use provided options------")
                

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
            #CREATES CREDENTIALS AND SAVES THEM
            print('Please fill the details below to save your credentials:')
            print('Your Username:')
            username=input()

            
            print('Password:')
            password=input()

            print('Email Address:')
            email=input()

            print('Details:')
            details=input()

            save_credentials(create_credentials(username,password,email,details))
            print('\n')
            print(f'{username} credentials successfully saved.')
            print('\n')


        elif code=='dc':
            #DISPLAYS THE USERS TOTAL CREDENTALS
            if display_credentials():
                for credential in display_credentials():
                    print('A list of all credentials.')
                    print('-'*30)
                    print(f'Username: {user.first_name} {user.last_name}, Password:{user.password} ,Email:{user.email} ,Details: {user.descrption}')
                    print('\n')

            else:
                print('Sorry you dont have any saved details.')

            if display_users():
                for user in display_users():
                    print('A list of your credential.')
                    print('-'*30)
                    print(f'Username: {credential.username}, Password:{credential.password} ,Email:{credential.email} ,Details: {credential.details}')
                    print('\n')

            else:
                print('Sorry you dont have any saved credentials.')




        #DISPLAYS ALL THE USERS SAVED CREDENTIALS
        elif code=='get':
            print('To retrieve your credential type username and password')
            print('Type username:')
            username=input()
            print('Type password:')
            password=input()

            if search_user(username):
                user_found=find_credential(password)
                print(f'Here is your credential {user_found.username}')
                print('-'*20)
                print(f'Username: {user_found.username}')
                print(f'Password: {user_found.password}')
                print(f'Email:     {user_found.email}')
                print(f'Details:   {user_found.details}')
                print('\n')
                
            else:
                print("Sorry credentials not found!")
                print('\n')

        elif code=='del':
            #DELETES A CREDENTIAL
            print('Please type in username and password to delete credential.')
            print('Type username to delete.')
            username=input()
            print('Type password:')
            password=input()

            if search_user(username):
                user_found=find_credential(password)
                print(f'Here is your credential {user_found.username}')
                print('-'*20)
                print(f'Username: {user_found.username} Password: {user_found.password} Email: {user_found.email} Details: {user_found.details}')
                print('\n')
                print('This credential will be deleted Y/N')
                y=input().lower()
                if y=='y':
                    delete=delete_credentials(user_found)
                    print('\n')
                    print(f'{user_found.username} credential deleted')
                    print('\n')

                else:
                    print('Aborted! Thank you!')
                    print('\n')
            else:
                print("Sorry credentials not found!")
                print('\n') 

        elif code=='ex':
            print('\n')
            print('Thank You! Bye.....')
            break

        else:
            print('\n')
            print('Unknown input use the code provided')
            














if __name__=="__main__":
    main()
