import unittest
from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    frenchText = MyMemoryTranslator(source='en', target='fr').translate(text='englishText')
    return frenchText

def frenchToEnglish(frenchText):
    englishText = MyMemoryTranslator(source='fr', target='en').translate(text='frenchText')
    return englishText

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertEqual(englishToFrench('Bonjour'), 'Bonjour')
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish('Hello'), 'Hello')

if __name__ == '__main__':
    unittest.main()
