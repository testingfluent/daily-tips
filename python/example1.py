import unittest

class Test(unittest.TestCase):

    def test_upper(self):
        string1 = 'testingfluent'
        string2 = 'TESTINGFLUENT'
        self.assertEqual(string1.upper(), string2)

if __name__ == '__main__':
    unittest.main()
