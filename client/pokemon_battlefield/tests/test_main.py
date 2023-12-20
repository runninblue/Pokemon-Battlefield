
import unittest
from unittest.mock import patch
import main
from exceptions import *

class TestMainModule(unittest.TestCase):
    @patch.object(main.sys, 'argv', ['main.py'])
    def test_parse_args_no_arguments(self):
        # Tests module without arguments
        result = main.parse_args()
        self.assertIsNone(result)

    @patch.object(main.sys, 'argv', ['main.py', 'pikachu', 'snorlax'])
    def test_parse_args_with_arguments(self):
        # Tests module with valid arguments
        result = main.parse_args()
        self.assertIsInstance(result, dict)
        expected_keys = ['pokemon1', 'pokemon2']
        self.assertCountEqual(result.keys(), expected_keys)
            
class TestParseArgs(unittest.TestCase):
    @patch('main.validate_contesters')
    def test_parse_args_valid_arguments(self, mock_validate_contesters):
        # Tests that validate_contesters() is called once froom parse_args function
        mock_validate_contesters.return_value = True
        with patch.object(main.sys, 'argv', ['main.py', 'pikachu', 'raichu']):
            result = main.parse_args()
        mock_validate_contesters.assert_called_once_with('pikachu', 'raichu')
        self.assertEqual(result, True)

    @patch('main.validate_contesters', side_effect=main.validate_contesters)
    def test_parse_args_invalid_arguments(self, validate_contesters):
        # Tests that validate_contesters() is called once from parse_args() and returns None for invalid arguments
        with patch.object(main.sys, 'argv', ['main.py', 'pokemon', 'nomekop']):
            result = main.parse_args()
        validate_contesters.assert_called_once_with('pokemon', 'nomekop')
        self.assertIsNone(result)

    @patch('main.validate_contesters')
    def test_parse_args_invalid_number_of_arguments(self, mock_validate_contesters):
        # Tests the behaviour of args_parse() if invalid number of arguments is passed - validate_contesters is not called and returns None
        with patch.object(main.sys, 'argv', ['main.py', 'pokemon1']):
                result = main.parse_args()
        self.assertIsNone(result)
        mock_validate_contesters.assert_not_called()

class TestValidateContesters(unittest.TestCase):
    @patch('main.requests.post')
    def test_validate_contesters_success(self, mock_post):
        # Tests that validate_contesters() returns the correct value when correct arguments are passed
        mock_post.return_value.ok = True
        mock_post.return_value.json.return_value = {'pokemon_details': 'some_details'}
        result = main.validate_contesters('pikachu', 'raichu')
        self.assertEqual(result, {'pokemon_details': 'some_details'})
        mock_post.assert_called_once_with("http://localhost:5000", data={'pokemon1': 'pikachu', 'pokemon2': 'raichu'})

    @patch('main.requests.post')
    def test_validate_contesters_failure(self, mock_post):
        # Tests that the response from validate_contesters() is None invalid arguments are passed
        mock_post.return_value.ok = False
        result = main.validate_contesters('pikachu', 'snorlaxx')
        self.assertIsNone(result)
        mock_post.assert_called_once_with("http://localhost:5000", data={'pokemon1': 'pikachu', 'pokemon2': 'snorlaxx'})

if __name__ == '__main__':
    unittest.main()