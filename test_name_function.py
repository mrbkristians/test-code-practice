import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    '''Test for "name_function.py". '''

    def test_first_last_name(self):
        '''Do name work?'''
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle(self):
        '''Do the middle name work?'''
        formatted_name = get_formatted_name('wolfgan', 'brown', 'jr')
        self.assertEqual(formatted_name, 'Wolfgan Jr Brown')

if __name__ == '__main__':
    unittest.main() 