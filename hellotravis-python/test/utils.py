# -*- coding: utf-8 -*-
import unittest2 as unittest


class UtilsTestCase(unittest.TestCase):

    def setUp(self):
        self.testText = "Hello Travis CI!"

    def test_print_text(self):
        print(self.testText)
        expected = "Hello Travis CI!"
        self.assertEqual(self.testText, expected)
