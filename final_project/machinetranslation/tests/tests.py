import unittest

from translator import english_to_french, french_to_english

class TestenglishToFrench(unittest.TestCase):
    """english_to_french Test Case""" 
    def test1(self): 
        '''englishToFrench - assertEqual
           englishToFrench - assertNotEqual 
        '''
        self.assertEqual(english_to_french('two'), 'Deux') # test when input text is two.
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test when input text is 'Hello'.
        self.assertNotEqual(english_to_french('None'), '') # test when input text is null (None type).

class TestfrenchToEnglish(unittest.TestCase): 
    """french_to_english Test Case""" 
    def test1(self):
        '''frenchToEnglish - assertEqual
           frenchToEnglish - assertNotEqual 
        ''' 
        self.assertEqual(french_to_english('5'), '5') # test when input text is 5.
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when input text is 'Bonjour'.
        self.assertNotEqual(french_to_english('None'), '') # test when input text is null (None type).

unittest.main()