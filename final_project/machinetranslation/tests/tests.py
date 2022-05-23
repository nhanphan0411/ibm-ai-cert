import unittest
from ./translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_1(self):
        """Test assertEqual"""
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test_2(self):
        """Test assertNotEqual"""
        self.assertNotEqual(english_to_french('Hello'), None)
    def test_3(self):
        """Test assertEqual"""
        self.assertEqual(english_to_french("How are you"), "Comment vous êtes")

class TestFrenchToEnglish(unittest.TestCase):
    def test_1(self):
        """Test assertEqual"""
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test_2(self):
        """Test assertNotEqual"""
        self.assertNotEqual(french_to_english('Bonjour'), None)
    def test_3(self):
        """Test assertEqual"""
        self.assertEqual(french_to_english("Comment vous êtes?"), "How are you?")

unittest.main()
