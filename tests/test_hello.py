import unittest

import travisdemo

class TestHello(unittest.TestCase):
    def test_greeting(self):
        message = travisdemo.hello()
        self.assertTrue(message.lower().startswith('hello'))

    def test_recipient(self):
        message = travisdemo.hello()
        self.assertTrue(message.endswith('TriLUG!'))
