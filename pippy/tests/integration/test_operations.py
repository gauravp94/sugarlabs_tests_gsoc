#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sugar3.test import unittest
from sugar3.test import uitree
import time
from gi.repository import Gtk


class TestHelper:
    """Basic helper class for Pippy tests"""

    def get_activity(self):
        root = uitree.get_root()
        activity = root.find_child(name="Pippy Activity",
                                   role_name="frame")
        return activity


class OperationsTest(unittest.UITestCase, TestHelper):

    '''
        Setting Up things for running the tests
    '''
    def setUp(self):
        unittest.UITestCase.setUp(self)
        self.bundle_id = "org.laptop.Pippy"
        self.screen_width = Gtk.Window().get_screen().get_width()
        self.screen_height = Gtk.Window().get_screen().get_height()

    '''
        Test to write print 'hello pippy' and the run the program
        and check the out put in the terminal window to be the same.
    '''
    def test_hello_pippy(self):
        with self.run_activity():
            activity = self.get_activity()
            text_entry = activity.find_child(role_name="text")
            text_entry.click(1,
                             0.02*self.screen_width,
                             0.001*self.screen_height)
            time.sleep(1)
            uitree.type_text('print "Hello Pippy"')
            time.sleep(0.25)
            run_activity = activity.find_child(name="Run!")
            run_activity.do_action('click')
            time.sleep(0.50)
            terminal = activity.find_child(name="Terminal",
                                           role_name="terminal")
            self.assertIsNotNone(text_entry)
            self.assertIsNotNone(run_activity)
            self.assertIsNotNone(terminal)
            time.sleep(0.25)
            self.assertEqual(terminal.text.strip(), "Hello Pippy")
            time.sleep(2.0)

    '''
        Test to toggle the open and close terminal button
        in the activity toolbar
    '''
    def test_toggle_terminal(self):
        with self.run_activity():
            activity = self.get_activity()
            toggle_terminal = activity.find_children(role_name="toggle button")
            toggle_terminal[0].do_action('click')
            time.sleep(0.25)
            toggle_terminal[0].do_action('click')
            time.sleep(0.25)
            toggle_terminal[0].do_action('click')
            time.sleep(1.25)
            self.assertIsNotNone(toggle_terminal[0])
            time.sleep(2.0)

    '''
        Test to check the Load example button on the activity toolbar
    '''
    def test_load_example(self):
        with self.run_activity():
            activity = self.get_activity()
            load_examples = activity.find_child(name="Load example",
                                                role_name="push button")
            self.assertIsNotNone(load_examples)
            time.sleep(2.0)

    '''
        Test to click on the activity button on the
        activity toolbar and then check the name of the
        activity to be equal to 'Pippy Activity'
    '''
    def test_check_activity(self):
        with self.run_activity():
            activity = self.get_activity()
            all_push_buttons = activity.find_children(role_name="push button")
            activity_button = all_push_buttons[0]
            activity_button.click()
            import_py = activity.find_child(name=
                                            "Import Python file to new tab",
                                            role_name="push button")
            export_pippy = activity.find_child(name=
                                               "Export as Pippy document",
                                               role_name="push button")
            lib = activity.find_child(name=
                                      "Save this file to the Pippy library",
                                      role_name="push button")
            export_ex = activity.find_child(name=
                                            "Export as new Pippy example",
                                            role_name="push button")
            crt_bund = activity.find_child(name=
                                           "Create a Sugar activity bundle",
                                           role_name="push button")
            exprt_dstils = activity.find_child(name=
                                               "Export as a disutils package",
                                               role_name="push button")
            activity_name = activity.find_child(role_name="text")
            self.assertIsNotNone(activity_button)
            self.assertIsNotNone(import_py)
            self.assertIsNotNone(export_pippy)
            self.assertIsNotNone(lib)
            self.assertIsNotNone(crt_bund)
            self.assertIsNotNone(export_ex)
            self.assertIsNotNone(exprt_dstils)
            self.assertEqual(activity_name.text.strip(), "Pippy Activity")
            time.sleep(2.0)

    '''
        Test to check the name of the file tab in pippy
    '''
    def test_file_tab(self):
        with self.run_activity():
            activity = self.get_activity()
            file_tab = activity.find_child(name="New Source File 1",
                                           role_name="page tab")
            self.assertIsNotNone(file_tab)
            time.sleep(2.0)

    '''
        Test to click on the edit button on the
        activity toolbar and check the presence of the
        various buttons in it like copy, paste, etc.
    '''
    def test_edit_tab(self):
        with self.run_activity():
            activity = self.get_activity()
            all_push_buttons = activity.find_children(role_name="push button")
            edit_toolbar = all_push_buttons[1]
            edit_toolbar.click()
            time.sleep(0.25)
            undo_button = activity.find_child(name="Undo",
                                              role_name="push button")
            redo_button = activity.find_child(name="Redo",
                                              role_name="push button")
            copy_button = activity.find_child(name="Copy",
                                              role_name="push button")
            paste_button = activity.find_child(name="Paste",
                                               role_name="push button")
            self.assertIsNotNone(edit_toolbar)
            self.assertIsNotNone(redo_button)
            self.assertIsNotNone(undo_button)
            self.assertIsNotNone(copy_button)
            self.assertIsNotNone(paste_button)
            time.sleep(2.0)

    '''
        Test to check the stop button in pippy,
        by stopping a running example in pippy
    '''
    def test_stop_button(self):
        with self.run_activity():
            activity = self.get_activity()
            text_entry = activity.find_child(role_name="text")
            text_entry.click(1,
                             0.02*self.screen_width,
                             0.001*self.screen_height)
            time.sleep(1)
            uitree.type_text('i = 0\n')
            uitree.type_text('while i<1000000:\n')
            uitree.type_text('  i+=1\n')
            uitree.type_text('print i\n')
            run_activity = activity.find_child(name="Run!",
                                               role_name="push button")
            stop_activity = activity.find_child(name="Stop",
                                                role_name="push button")
            run_activity.click()
            time.sleep(0.25)
            stop_activity.click()
            terminal = activity.find_child(name="Terminal",
                                           role_name="terminal")
            self.assertIsNotNone(text_entry)
            self.assertIsNotNone(run_activity)
            self.assertIsNotNone(stop_activity)
            self.assertIsNotNone(terminal)
            time.sleep(2.0)

    '''
        Test to run a program and the clear the terminal
        screen in the pippy
    '''
    def test_clear_button(self):
        with self.run_activity():
            activity = self.get_activity()
            text_entry = activity.find_child(role_name="text")
            text_entry.click(1,
                             0.02*self.screen_width,
                             0.001*self.screen_height)
            time.sleep(1)
            uitree.type_text('i = 0\n')
            uitree.type_text('while i<1000000:\n')
            uitree.type_text('  i+=1\n')
            uitree.type_text('print i\n')
            run_activity = activity.find_child(name="Run!",
                                               role_name="push button")
            stop_activity = activity.find_child(name="Stop",
                                                role_name="push button")
            clear_activity = activity.find_child(name="Clear",
                                                 role_name="push button")
            run_activity.click()
            time.sleep(0.25)
            stop_activity.click()
            time.sleep(0.25)
            clear_activity.click()
            uitree.type_text('print "Hello Pippy"')
            time.sleep(0.50)
            run_activity.click()
            time.sleep(0.50)
            terminal = activity.find_child(name="Terminal",
                                           role_name="terminal")
            self.assertIsNotNone(text_entry)
            self.assertIsNotNone(run_activity)
            self.assertIsNotNone(stop_activity)
            self.assertIsNotNone(clear_activity)
            self.assertIsNotNone(terminal)
            self.assertEqual(terminal.text.strip(), "Hello Pippy")
            time.sleep(2.0)
