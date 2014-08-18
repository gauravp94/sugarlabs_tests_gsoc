#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sugar3.test import unittest
from sugar3.test import uitree

class OperationsTest(unittest.UITestCase):

    def setUp(self):
        unittest.UITestCase.setUp(self)
        self.bundle_id = "org.sugarlabs.HelloWorld"
	
    """
    Test to check the label in the Hello World Activity is equal to 'Hello World!'
    """
    def test_add_button(self):
        with self.run_activity():
            root = uitree.get_root()
            activity = root.find_child(name="HelloWorld Activity", role_name="frame")
            label = activity.find_child(name="Hello World!", role_name="label")
            self.assertEqual(label.text, "Hello World!")
