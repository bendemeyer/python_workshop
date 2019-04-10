import unittest

from modules.messages import get_welcome_message


class TestMessages(unittest.TestCase):
    def test_get_welcome_message(self):
        self.assertEqual(get_welcome_message('Monty'), "Welcome, Monty!")

if __name__ == '__main__':
    unittest.main()