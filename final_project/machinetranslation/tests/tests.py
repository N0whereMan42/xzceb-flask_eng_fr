import unittest
from translator import english_to_french, french_to_english
from ibm_watson import ApiException 

class Testenglish_to_french(unittest.TestCase):
    def test1(self):
        self.assertRaises((ApiException),english_to_french,"")
        self.assertEqual(english_to_french('Hello'),'Bonjour')

class Testfrench_to_english(unittest.TestCase):
    def test1(self):
        self.assertRaises((ApiException),french_to_english,"")
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()
