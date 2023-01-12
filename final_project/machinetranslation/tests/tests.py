import unittest
from translator import english_to_french, french_to_english

class TestCases(unittest.TestCase):
    def test_null_e2f(self):
        self.assertNotEqual(english_to_french(""), "", "Value is empty")
    def test_null_f2e(self):
        self.assertNotEqual(french_to_english(""), "", "Value is empty")
    def test_e2f(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour", "wrong translation")
    def test_f2e(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello", "wrong translation")

if __name__ == "__main__":
    unittest.main()