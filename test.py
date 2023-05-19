from main import unicode, generate_random_numbers, main
import unittest

class TestPinMethods(unittest.TestCase):

    def test_generate_random_numbers(self):
        num = generate_random_numbers(test=True)
        self.assertEqual([48, 57, 65, 90, 97, 122], num)
    
    def test_unicode(self):
        num = generate_random_numbers()
        alpha = unicode(num)
        self.assertTrue(alpha.isalnum())

    def test_main(self):
        num = generate_random_numbers(test=True)
        alpha = unicode(num, test=True)
        self.assertEqual("09AZaz", alpha)

if __name__ == "__main__":
    unittest.main()