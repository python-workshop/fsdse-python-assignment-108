from unittest import TestCase


class TestFizz_buzz(TestCase):
    def test_fizz_buzz(self):
        try:
            from build import  fizz_buzz
        except ImportError:
            self.assertFalse("no function found")

        self.assertRaises(TypeError, fizz_buzz, None)
        self.assertRaises(ValueError, fizz_buzz, 0)
        expected = [
            '1',
            '2',
            'Fizz',
            '4',
            'Buzz',
            'Fizz',
            '7',
            '8',
            'Fizz',
            'Buzz',
            '11',
            'Fizz',
            '13',
            '14',
            'FizzBuzz'
        ]
        self.assertEqual(fizz_buzz(15), expected)
