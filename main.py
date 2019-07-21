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

def create_profile(app, persona_name,user_password):
    
    new_profile = profiles(
        app, persona_name,user_password
    )
