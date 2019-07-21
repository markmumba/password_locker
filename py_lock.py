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

    @classmethod
    def search_profile(cls, app):

        for profile in cls.profiles_list:
            if profile.app == app:
                return profile

    @classmethod
    def profile_exist(cls, app):
        for profile in cls.profiles_list:
            if profile.app == app:
                return True
        return False

    @classmethod
    def display_profile(cls):

        return cls.profiles_list

    def gen_password():
        chars = char = string.ascii_uppercase+string.ascii_lowercase+string.digits
        length = 9
        print('here is  are your password:')
        password = ''.join(random.choice(chars) for _ in range(-1, length))
        print(password)
        return password
