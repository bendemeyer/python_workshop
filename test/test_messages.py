import unittest
from unittest.mock import patch, Mock
from modules.messages import get_welcome_message


class TestMessages(unittest.TestCase):
    @patch('modules.messages.datetime.datetime')
    @patch('modules.messages.requests')
    def test_get_welcome_message(self, mock_requests, mock_datetime):
        mock_response = Mock()
        mock_response.json.return_value = {
            'status': 'success',
            'greeting': 'Howdy-doo'
        }
        mock_requests.get.return_value = mock_response
        mock_datetime.now = Mock()
        mock_datetime.now.return_value = 5
        self.assertEqual(get_welcome_message('Monty'), "Howdy-doo, Monty! The current time is 5")


if __name__ == '__main__':
    unittest.main()