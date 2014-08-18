#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sugar3.test import unittest
from sugar3.test import uitree
import time
from gi.repository import Gtk

class TestHelper:
    """Basic helper class for Log tests"""
    def get_activity(self):
        root = uitree.get_root()
        activity = root.find_child(name="Log Activity",
                                   role_name="frame")
        return activity


class OperationsTest(unittest.UITestCase, TestHelper):

    def setUp(self):
        unittest.UITestCase.setUp(self)
        self.bundle_id = "org.laptop.Log"
        self.screen_width = Gtk.Window().get_screen().get_width()
        self.screen_height = Gtk.Window().get_screen().get_height()

    '''
        Test for Log to test the toggle buttons of
        listing the side panel and the word wrap in the activity
    '''
    def test_toggle_buttons(self):
        with self.run_activity():
            activity = self.get_activity()
            toggle_buttons = activity.find_children(role_name="toggle button")
            list_files = toggle_buttons[0]
            word_wrap = toggle_buttons[1]
            list_files.do_action('click')
            time.sleep(0.25)
            word_wrap.do_action('click')
            time.sleep(0.25)
            word_wrap.do_action('click')
            time.sleep(0.25)
            list_files.do_action('click')
            time.sleep(0.25)
            self.assertEqual(2, len(toggle_buttons))
            time.sleep(1.5)

    '''
        Test for Log to open an instance of Log Activity and
        then close the activity
    '''
    def test_close_activity(self):
        with self.run_activity():
            activity = self.get_activity()
            stop_button = activity.find_child(name="Stop",
                                              role_name="push button")
            stop_button.do_action('click')
            self.assertIsNotNone(stop_button)
            time.sleep(2)

    '''
        Test for Log to click on the activity button and
        then check the name of the activity to be equal to
        "Log Activity"
    '''
    def test_check_activity(self):
        with self.run_activity():
            activity = self.get_activity()
            activity_btns = activity.find_children(role_name="push button")
            activity_button = activity_btns[0]
            activity_button.do_action('click')
            toolbars = activity.find_children(role_name="tool bar")
            sec_toolbar = toolbars[1]
            txt = sec_toolbar.find_child(role_name="text")
            self.assertEqual("Log Activity", txt.text)
            time.sleep(1.5)

    '''
        Test for log to click on the activity button
        and then open the description tab and then
        check the text in it.
    '''
    def test_description_tab(self):
        with self.run_activity():
            activity = self.get_activity()
            activity_btns = activity.find_children(role_name="push button")
            activity_button = activity_btns[0]
            activity_button.do_action('click')
            toolbars = activity.find_children(role_name="tool bar")
            sec_toolbar = toolbars[1]
            des = sec_toolbar.find_child(name="Description",
                                         role_name="push button")
            self.assertEqual("", des.text)
            time.sleep(2)

    '''
        Test to click on the different file tabs present
        in the side panel of Log Activity.
    '''
    def test_click_file_tabs(self):
        with self.run_activity():
            activity = self.get_activity()
            file_tab = activity.find_child(name="/var/log",
                                           role_name="table cell")
            other_tab = activity.find_child(name="Other",
                                            role_name="table cell")
            file_tab.click()
            other_tab.click()
            time.sleep(0.5)
            file_tab.click()
            other_tab.click()
            time.sleep(0.5)
            self.assertIsNotNone(file_tab)
            self.assertIsNotNone(other_tab)
            time.sleep(2)

    '''
        Test for Log to open some log files that are
        present in the Log activity.
    '''
    def test_open_log_file(self):
        with self.run_activity():
            activity = self.get_activity()
            yum_log = activity.find_child(name="yum.log",
                                          role_name="table cell")
            last_log = activity.find_child(name="lastlog",
                                           role_name="table cell")
            readme = activity.find_child(name="README",
                                         role_name="table cell")
            wtmp = activity.find_child(name="wtmp",
                                       role_name="table cell")
            bash_history = activity.find_child(name=".bash_history",
                                               role_name="table cell")
            yum_log.click()
            time.sleep(0.5)
            last_log.click()
            time.sleep(0.5)
            readme.click()
            time.sleep(0.5)
            wtmp.click()
            time.sleep(0.5)
            bash_history.click()
            time.sleep(0.5)
            self.assertIsNotNone(yum_log)
            self.assertIsNotNone(last_log)
            self.assertIsNotNone(readme)
            self.assertIsNotNone(wtmp)
            self.assertIsNotNone(bash_history)
            time.sleep(2)

    '''
        Test for Log to open the yum.log file
        and then search for the word "Installed" in the log
        file and toggle over the results, forward and backward.
    '''
    def test_search_log_file(self):
        with self.run_activity():
            activity = self.get_activity()
            yum_log = activity.find_child(name="yum.log",
                                          role_name="table cell")
            previous_button = activity.find_child(name="Previous",
                                                  role_name="push button")
            forward_button = activity.find_child(name="Next",
                                                 role_name="push button")
            text_entries = activity.find_children(role_name="text")
            search_text = text_entries[0]
            yum_log.click()
            time.sleep(1)
            search_text.click(1, 
                              0.025*self.screen_width,
                              0.02*self.screen_height)
            time.sleep(1)
            uitree.type_text('Installed')
            time.sleep(2)
            count = 5
            while count:
                previous_button.click()
                time.sleep(0.25)
                count -= 1
            count = 5
            time.sleep(1)
            while count:
                forward_button.click()
                time.sleep(0.25)
                count -= 1
            time.sleep(1)
            self.assertIsNotNone(previous_button)
            self.assertIsNotNone(forward_button)
            self.assertIsNotNone(yum_log)
            time.sleep(2)

    '''
        Test to check the Delete Log File button
        present in the Log Activity
    '''
    def test_delete_log_file(self):
        with self.run_activity():
            activity = self.get_activity()
            delete_log = activity.find_child(name="Delete Log File",
                                             role_name="push button")
            self.assertIsNotNone(delete_log)
            time.sleep(1.5)
