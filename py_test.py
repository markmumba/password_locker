import unittest
import pyperclip
from py_lock import personas


class TestUser(unittest.TestCase):
    def SetUp(self):
        self.new_persona= personas("markian","Mortyka56//")
        
    def test_init(self):
        self.assertEqual(self.new_persona.username, "markian")
        self.assertEqual(self.new_persona.password,"Mortyka56//")
        
        
    def save_persona(self):
        self.new_persona.test_save_persona()
        self.assertEqual(len())
        
        