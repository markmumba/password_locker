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


de
