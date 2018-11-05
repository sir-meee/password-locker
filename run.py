#!/usr/bin/env python3.6
from user import User , Credentials 
def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User (username,password)
    return new_user
 def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()
 def check_existing_users(surname):
    '''
    Function that check if a user exists with that username and return a Boolean
    '''
    return User.user_exist(surname)
    def create_credentials(acc_name,login_name,pword):
    '''
    Function to create a new credential
    '''
    new_credentials = Credentials (acc_name,login_name,pword)
    return new_credentials
 def save_credentialss(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()
 def del_credentials(credentials):
    '''
    Function to delete a credential
    '''
    credentials.delete_credentials()