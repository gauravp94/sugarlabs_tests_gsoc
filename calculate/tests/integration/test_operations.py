#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sugar3.test import unittest
from sugar3.test import uitree
import time

class TestHelper:
    """Basic helper class for Calculate tests"""

    def get_result(self, activity_node):
        equal_button = activity_node.find_child(name="=",
                                                role_name="push button")
        equal_button.do_action("click")

        resultbox = activity_node.find_children(name="", role_name="text")
        return resultbox[0].text

    def get_activity(self):
        root = uitree.get_root()
        #activity = root.find_child(name="Calculate Activity",
        #                           role_name="frame")
        activity = root.find_child(name="Calculate Activity", role_name="frame")
        '''sec = []        
        for i in activity:
            sec.append(i.role_name)        
        return sec'''
        return activity
        '''a = root.find_children()
        lis=[]
        for i in a:
            lis.append([i.name,i.role_name])        
        return lis
        '''
    def click_button(self, activity, name):
        button1 = activity.find_child(name=name, role_name="push button")
        button1.do_action("click")

    def type_number(self, activity, number):
        number = str(number)
        for char in number:
            self.click_button(activity, char)


class OperationsTest(unittest.UITestCase, TestHelper):

    def setUp(self):
        unittest.UITestCase.setUp(self)
        self.bundle_id = "org.laptop.Calculate"
    
    def test_close_activity2(self):
        with self.run_activity():
            print "OOOOOOOOOOOOOOOOOOOOOO"
            activity = self.get_activity()
            time.sleep(2)
            print "PPPPP",activity.dump()
            #for i in activity:
            #    print i
    ''' def test_add_button(self):
        with self.run_activity():
            activity = self.get_activity()

            self.click_button(activity, "1")
            self.click_button(activity, "+")
            self.click_button(activity, "1")

            result = self.get_result(activity)
            self.assertEqual(result, "1+1\n2")

    def test_subtract_button(self):
        with self.run_activity():
            activity = self.get_activity()

            self.click_button(activity, "1")
            self.click_button(activity, "-")
            self.click_button(activity, "1")

            result = self.get_result(activity)
            self.assertEqual(result, "1-1\n0")

    def test_multiply_button(self):
        with self.run_activity():
            activity = self.get_activity()

            self.click_button(activity, "2")
            self.click_button(activity, "×")
            self.click_button(activity, "2")

            result = self.get_result(activity)
            self.assertEqual(result, "2×2\n4")

    def test_divide_button(self):
        with self.run_activity():
            activity = self.get_activity()

            self.click_button(activity, "8")
            self.click_button(activity, "÷")
            self.click_button(activity, "2")

            result = self.get_result(activity)
            self.assertEqual(result, "8÷2\n4")

    def test_numbers_present(self):
        with self.run_activity():
            activity = self.get_activity()

            for i in range(0, 10):
                btn = activity.find_child(name=str(i),
                                          role_name="push button")
                self.assertIsNotNone(btn)'''
