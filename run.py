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

def find_credential(username):
    Credentials.find_by_username(username)

def search_user(username):
    Credentials.user_exists(username)

def display_users():
    Credentials.display_users()
