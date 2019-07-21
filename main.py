#!/usr/bin/env python3.8
import pyperclip
import random
import string
from py_lock import personas, profiles


def create_persona(persona_name, password):

    new_persona = personas(persona_name, password)

    return new_persona


def save_New_persona(persona_name):

    personas.personas_list.append(persona_name)


def accept_persona(persona_name, password):

    accept_persona = profiles.confirm_persona(persona_name, password)

    return accept_persona


def create_profile(app, persona_name, user_password):

    new_profile = profiles(
        app, persona_name, user_password
    )
    return new_profile


def save_profile(py_lock):
    py_lock.save_profile()


def delete_profile(py_lock):

    py_lock.delete_profile()


def find_profile(app):

    return profiles.search_profile(app)


def check_existing_profile(app):

    return profiles.profile_exist(app)


def display_profile():

    return profiles.display_profile()


def copy_password(app):

    profiles.copy_password(app)


def gen_password():
    auto_generic_password = profiles.gen_password()

    return auto_generic_password


def main():
    print("Welome to your user profiles list.Create An Account :CA or Already have an Account LI? :")
    short_code = input("CA ,LI").lower()
    if short_code == 'ca':
        username = input("Enter your prefered username").capitalize()
        password = input("Enter Your Password As Well")
        save_New_persona(create_persona(username, password))

    elif short_code == 'li':
        username = input("Enter your prefered username").capitalize()
        password = input("Enter Your Password As Well")
        validate_persona = (accept_persona(username, password))

        if validate_persona == username:
            print(f"Hello {username}.Welcome To PassWord Locker Manager")
            print('\n')
            print("what would you like to do?")
            print('\n')

    while True:
        print("Use these short codes : cc - Create a new credential, dc - Display Credential(s), fc - Find a credential,ex - Exit the application, gp- Generate A randomn password, del- Delete credential,cp-Copy Password")
        short_code = input().lower()

        if short_code == 'cc':
            print("New Profile")
            print("-"*10)

            print("App name.....")
            app_name = input().capitalize()

            print("Your App name ...e.g instagram username")
            persona_name = input()
            while True:
                print(" For Type/Paste Password type TP ; For generate_Password type gp")
                password == input("Enter").lower()
                if password == 'tp':
                    password = input("Enter Password")
                    break
                elif password == 'gp':
                    password = gen_password()
                    break
                elif password != 'tp' or 'gp':
                    print("Invalid password please try again")
                    break
                else:
                    print("Invalid password please try again")
                    save_profile(create_profile(app_name, username, password))
                    print('\n')
                    print(
                        f"New Credential : {app_name} UserName: {username}  created")
                    print('\n')

        elif short_code == 'dc':
            if display_profile():
                print(
                    "Your Account(s) Credential(S) are as follows :")
                print('\n')
                for password_locker in display_profile():
                    print(
                        f"App_name :{password_locker.app_name} ; UserName: {password_locker.username} ; PassWord :{password_locker.password}")

                print('\n')
            else:
                print('\n')
                print(
                    "Oops !!! You dont seem to have any Credentials saved yet")
                print('\n')

        elif short_code == 'fc':

            print("Enter the Account Name you want to search for")
            search_name = input().capitalize()
            if check_existing_profile(search_name):
                search_profile = find_profile(search_name)
                print(f"app_name:{search_profile.app_name}")
                print('-'*100)
                print(
                    f"app_name:{search_profile.app_name} password :{search_profile.password}")
            else:
                print("That Credential does not exist")
                print('\n')

        elif short_code == 'cp':
            print("Enter the app name of the profile you want to generate password for")
            search_name = input().capitalize()
            if check_existing_profile(search_name):
                search_profile = find_profile(search_name)
                print(f"{search_profile.app_name}")
                print('-'*20)
                password = copy_password(search_name)
                print('\n')
                print(
                    f"New profile : {app_name} username: {username} You can proceed and paste to your account")
                print('\n')
            else:
                print("That profile does not exist")
        elif short_code == 'gp':
            password = gen_password()

        elif short_code == 'ex':
            print("Happy Coding See You Dear")
            break
        else:
            print("Invalid response kindly refer to the Menu above")


if __name__ == '__main__':
    main()
