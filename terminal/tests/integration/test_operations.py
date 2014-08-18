#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sugar3.test import unittest
from sugar3.test import uitree
import time


def get_activity():
    root = uitree.get_root()
    activity = root.find_child(name="Terminal Activity",
                               role_name="frame")
    return activity


class OperationsTest(unittest.UITestCase):

    def setUp(self):
        unittest.UITestCase.setUp(self)
        self.bundle_id = "org.laptop.Terminal"

    '''
        Test to click on the 1st push button on the panel and
        then find the name of the activity and the name from it
        should be equal to "Terminal Activity".
    '''
    def test_activity_name(self):
        with self.run_activity():
            activity = get_activity()
            all_push = activity.find_children(role_name="push button")
            all_push[0].do_action("click")
            activity_name = activity.find_child(role_name="text")
            all_push[0].do_action("click")
            print activity.dump()
            self.assertEqual(activity_name.text, "Terminal Activity")
            time.sleep(1.5)

    '''
        Test to open an instance of Terminal Activity
        and check the presence of Stop button.
    '''
    def test_stop_button(self):
        with self.run_activity():
            activity = get_activity()
            stop_button = activity.find_child(name="Stop",
                                              role_name="push button")
            self.assertIsNotNone(stop_button)
            time.sleep(1.5)

    '''
        Test to open the edit toolbar button and then check all the buttons,
        present in the sub-toolbar like copy, paste.
    '''
    def test_edit_buttons(self):
        with self.run_activity():
            activity = get_activity()
            all_push = activity.find_children(role_name="push button")
            all_push[1].do_action("click")
            copy_button = activity.find_child(name="Copy",
                                              role_name="push button")
            paste_button = activity.find_child(name="Paste",
                                               role_name="push button")
            undo_button = activity.find_child(name="Undo",
                                              role_name="push button")
            redo_button = activity.find_child(name="Redo",
                                              role_name="push button")
            all_push[1].do_action("click")
            self.assertIsNotNone(copy_button)
            self.assertIsNotNone(paste_button)
            self.assertIsNotNone(undo_button)
            self.assertIsNotNone(redo_button)
            time.sleep(1.5)

    '''
        Test to open the zoom toolbar
        and then test the zoom in button.
    '''
    def test_zoomin_buttons(self):
        with self.run_activity():
            activity = get_activity()
            all_push = activity.find_children(role_name="push button")
            all_push[2].do_action("click")
            zoomin_button = activity.find_child(name="Zoom in",
                                                role_name="push button")
            count = 3
            while count:
                zoomin_button.click()
                time.sleep(0.25)
                count -= 1
            all_push[2].do_action("click")
            self.assertIsNotNone(zoomin_button)
            time.sleep(1.5)

    '''
        Test to open the zoom toolbar
        and then test the zoom out button
        and check the fullscreen button.
    '''
    def test_zoomout_buttons(self):
        with self.run_activity():
            activity = get_activity()
            all_push = activity.find_children(role_name="push button")
            all_push[2].do_action("click")
            zoomout_button = activity.find_child(name="Zoom out",
                                                 role_name="push button")
            count = 3
            while count:
                zoomout_button.click()
                time.sleep(0.25)
                count -= 1
            fullscreen_button = activity.find_child(name="Fullscreen",
                                                    role_name="push button")
            all_push[2].do_action("click")
            self.assertIsNotNone(zoomout_button)
            self.assertIsNotNone(fullscreen_button)
            time.sleep(1.5)

    '''
        Test to open the help toolbar in Terminal
    '''
    def test_help(self):
        with self.run_activity():
            activity = get_activity()
            help_button = activity.find_child(name="Help",
                                              role_name="push button")
            help_button.do_action("click")
            help_button.do_action("click")
            self.assertIsNotNone(help_button)
            time.sleep(1.5)

    '''
        Test to open new tabs in Terminal
    '''
    def test_open_tabs(self):
        with self.run_activity():
            activity = get_activity()
            time.sleep(5)
            print activity.dump()
            time.sleep(1.5)
