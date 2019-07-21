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


class profiles:

    profiles_list = []

    @classmethod
    def confirm_persona(cls, username, password):

        active_persona = ''
        for persona in personas.personas_list:
            if(persona.username == username and persona.password == password):
                active_persona == persona.username
        return active_persona

    def __init__(self, app, username, password):
        self.app = app
        self.username = username
        self.password = password

    def save_profile(self):

        profiles.profiles_list.append(self)

    def delete_profile(self):

        profiles.profiles_list.remove(self)
