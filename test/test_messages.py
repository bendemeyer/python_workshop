import unittest
from unittest.mock import patch, Mock
from modules.messages import get_welcome_message


class TestMessages(unittest.TestCase):
    @patch('modules.messages.requests')
    def test_get_welcome_message(self, mock_requests):
        mock_response = Mock()
        mock_response.json.return_value = {
            'status': 'success',
            'greeting': 'Howdy-doo'
        }
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_welcome_message('Monty'), "Howdy-doo, Monty!")


if __name__ == '__main__':
    unittest.main()