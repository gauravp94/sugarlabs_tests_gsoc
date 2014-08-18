#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import logging
import time
from sugar3.test import unittest
from sugar3.test import uitree
from gi.repository import Gtk


class OperationsTest(unittest.UITestCase):

    def setUp(self):
        unittest.UITestCase.setUp(self)
        self.bundle_id = "org.laptop.sugar.ReadActivity"
        self.screen_width = Gtk.Window().get_screen().get_width()
        self.screen_height = Gtk.Window().get_screen().get_height()

    '''
        Test to open a file named t2.txt in Read
    '''
    def test_open_file(self):
        uri = 'file://' + os.getcwd() + '/tests/integration/t2.txt'
        logging.error('OPEN WITH URI %s', uri)
        with self.run_activity_with_uri(uri):
            root = uitree.get_root()
            activity = root.find_child(name="Read Activity", role_name="frame")
            try:
                logging.error(activity.dump())
            except:
                logging.error("Error")
                pass
            stop_button = activity.find_child(name="Stop",
                                              role_name="push button")
            stop_button.click()
            self.assertIsNotNone(stop_button)

    '''
        Test to click the activity button and verify
        that the name of the activity is Read Activity
    '''
    def test_check_file(self):
        uri = 'file://' + os.getcwd() + '/tests/integration/t2.txt'
        logging.error('OPEN WITH URI %s', uri)
        with self.run_activity_with_uri(uri):
            root = uitree.get_root()
            activity = root.find_child(name="Read Activity", role_name="frame")
            try:
                logging.error(activity.dump())
            except:
                logging.error("Error")
                pass
            all_push_buttons = activity.find_children(role_name="push button")
            activity_buttons = all_push_buttons[0]
            activity_buttons.click()
            time.sleep(1)
            all_content = activity.find_children(role_name="text")
            activity_name = all_content[1].text.strip()
            self.assertEqual(activity_name, "Read Activity")

    '''
        Test to search for letter 't' in the test file and
        then scroll over the results and also click on the
        highlight button of the activity search results
    '''
    def test_search(self):
        uri = 'file://' + os.getcwd() + '/tests/integration/t2.txt'
        logging.error('OPEN WITH URI %s', uri)
        with self.run_activity_with_uri(uri):
            root = uitree.get_root()
            activity = root.find_child(name="Read Activity", role_name="frame")
            try:
                logging.error(activity.dump())
            except:
                logging.error("Error")
                pass
            all_push_buttons = activity.find_children(role_name="push button")
            edit_buttons = all_push_buttons[1]
            edit_buttons.click()
            time.sleep(0.25)
            all_panels = activity.find_children(role_name="panel")
            search_panel = all_panels[20]
            search_box = search_panel.find_child(role_name="text")
            search_box.click(1,
                             0.04*self.screen_width,
                             0.02*self.screen_height)
            time.sleep(0.5)
            uitree.type_text('t')
            time.sleep(1)
            backward_panel = all_panels[21]
            forward_panel = all_panels[22]
            hlight_panel = all_panels[24]
            forward_button = forward_panel.find_child(role_name="push button")
            back_button = backward_panel.find_child(role_name="push button")
            hlight_button = hlight_panel.find_child(role_name="toggle button")
            count = 2
            while count:
                forward_button.click()
                time.sleep(1)
                count -= 1
            hlight_button.click()
            count = 2
            while count:
                back_button.click()
                time.sleep(1)
                count -= 1
            self.assertIsNotNone(forward_button)
            self.assertIsNotNone(back_button)
            self.assertIsNotNone(hlight_button)
            self.assertIsNotNone(search_box)

    '''
        Test to open a file named t2.txt in Read and test the zoom buttons
    '''
    def test_zoom(self):
        uri = 'file://' + os.getcwd() + '/tests/integration/t2.txt'
        logging.error('OPEN WITH URI %s', uri)
        with self.run_activity_with_uri(uri):
            root = uitree.get_root()
            activity = root.find_child(name="Read Activity", role_name="frame")
            try:
                logging.error(activity.dump())
            except:
                logging.error("Error")
                pass
            time.sleep(2)
            all_push_buttons = activity.find_children(role_name="push button")
            zoom_buttons = all_push_buttons[2]
            zoom_buttons.click()
            zoom_in = activity.find_child(name="Zoom in",
                                          role_name="push button")
            zoom_out = activity.find_child(name="Zoom out",
                                           role_name="push button")
            zoom_width = activity.find_child(name="Zoom to width",
                                             role_name="push button")
            zoom_fit = activity.find_child(name="Zoom to fit",
                                           role_name="push button")
            actual_size = activity.find_child(name="Actual size",
                                              role_name="push button")
            fullscreen = activity.find_child(name="Fullscreen",
                                             role_name="push button")
            rotate_left = activity.find_child(name="Rotate left",
                                              role_name="push button")
            rotate_right = activity.find_child(name="Rotate right",
                                               role_name="push button")
            count = 10
            while count:
                zoom_in.click()
                time.sleep(0.25)
                count -= 1
            count = 5
            while count:
                zoom_out.click()
                time.sleep(0.25)
                count -= 1
            self.assertIsNotNone(zoom_in)
            self.assertIsNotNone(zoom_out)
            self.assertIsNotNone(zoom_width)
            self.assertIsNotNone(zoom_fit)
            self.assertIsNotNone(actual_size)
            self.assertIsNotNone(fullscreen)
            self.assertIsNotNone(rotate_left)
            self.assertIsNotNone(rotate_right)

    '''
        Test to change the pages in given test file
    '''
    def test_change_pages(self):
        uri = 'file://' + os.getcwd() + '/tests/integration/t2.txt'
        logging.error('OPEN WITH URI %s', uri)
        with self.run_activity_with_uri(uri):
            root = uitree.get_root()
            activity = root.find_child(name="Read Activity", role_name="frame")
            try:
                logging.error(activity.dump())
            except:
                logging.error("Error")
                pass
            forward_button = activity.find_child(name="Forward",
                                                 role_name="push button")
            backward_button = activity.find_child(name="Back",
                                                  role_name="push button")
            forward_button.click()
            time.sleep(1)
            backward_button.click()
            time.sleep(1)
            self.assertIsNotNone(forward_button)
            self.assertIsNotNone(backward_button)

    '''
        Test to click on bookmark button and then
        check that it is present/not none
    '''
    def test_bookmarks(self):
        uri = 'file://' + os.getcwd() + '/tests/integration/t2.txt'
        logging.error('OPEN WITH URI %s', uri)
        with self.run_activity_with_uri(uri):
            root = uitree.get_root()
            activity = root.find_child(name="Read Activity", role_name="frame")
            try:
                logging.error(activity.dump())
            except:
                logging.error("Error")
                pass
            print activity.dump()
            toggle_buttons = activity.find_children(role_name="toggle button")
            bookmark_button = toggle_buttons[0]
            bookmark_button.click()
            time.sleep(1)
            self.assertIsNotNone(bookmark_button)

    '''
        Test to select a part of text and then
        click on the play button found in the speak panel
    '''
    def test_speak(self):
        uri = 'file://' + os.getcwd() + '/tests/integration/t2.txt'
        logging.error('OPEN WITH URI %s', uri)
        with self.run_activity_with_uri(uri):
            root = uitree.get_root()
            activity = root.find_child(name="Read Activity", role_name="frame")
            try:
                logging.error(activity.dump())
            except:
                logging.error("Error")
                pass
            all_push_buttons = activity.find_children(role_name="push button")
            uitree.drag(0.05*self.screen_width,
                        0.08*self.screen_height,
                        0.1*self.screen_width,
                        0.1*self.screen_height)
            speak_button = all_push_buttons[5]
            speak_button.click()
            time.sleep(1)
            all_toolbar = activity.find_children(role_name="tool bar")
            speak_toolbar = all_toolbar[1]
            play_button = speak_toolbar.find_child(role_name="toggle button")
            stop_button = speak_toolbar.find_child(role_name="push button")
            play_button.click()
            time.sleep(3)
            self.assertIsNotNone(play_button)
            self.assertIsNotNone(stop_button)
