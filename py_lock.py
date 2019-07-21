import random
import string
import pyperclip


class personas:

    personas_list = []

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def save_persona(self):

        personas.personas_list.append(self)


class profile:
    
    profile_list =[]
    
    
    
    @classmethod
    def confirm_persona(cls,username,password):
        active_user