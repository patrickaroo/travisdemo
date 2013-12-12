import unittest

import travisdemo

class TestHello(unittest.TestCase):
    def test_greeting(self):
        message = travisdemo.hello()
        self.assertTrue(message.lower().startswith('hello'))
