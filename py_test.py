import unittest
import pyperclip
from py_lock import personas,profiles


class Testpersona(unittest.TestCase):
    def SetUp(self):
        self.new_persona = personas("markian", "Mortyka56//")

    def test_init(self):
        self.assertEqual(self.new_persona.username, "markian")
        self.assertEqual(self.new_persona.password, "Mortyka56//")

    def test_save_persona(self):
        self.new_persona.save_persona()
        self.assertEqual(len(profiles.profiles_list),1)


class Testprofile(unittest.TestCase):
    
    def SetUp(self):
        self.new_profile = profiles("instagram","markian","Mortyka56//")
    def test_int(self):
        self.assertEqual(self.new_profile.app,"instagram")
        self.assertEqual(self.new_profile.username,"markian")
        self.assertEqual(self.new_profile.password,"Mortyka56//")
        
    def save_profile(self):
           self.new_profile.save_profile()
           self.assertEqual(len(profiles.profiles_list),1)
           
    def tearDown(self):
        profiles.profiles_list=[]
        
    def test_save_mutiple_profiles(self):
        self.new_profile.save_profile()
        test_profile = profiles(
            "instagram","markian","Mortyka56//"
        )
        test_profile.save_profile()
        self.assertEqual(len(profiles.profiles_list),2)
        
        
    def test_delete_profile(self):
        self.new_profile.save_profile()
        test_profile = profiles(
            "instagram","markian","Mortyka56//"
        )
        test_profile.delete_profile()
        self.assertEqual(len(profiles.profiles_list),1)
        
    def test_search_profile(self):
        self.new_profile.save_profile()
        test_profile = profiles(
            "instagram","markian","Mortyka56//"
        )
        test_profile.save_profile()
        
        found_profile = profiles.search_profile("instagram")
        
        
        
      