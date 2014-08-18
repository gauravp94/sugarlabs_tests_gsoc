#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import logging
import time
from sugar3.test import unittest
from sugar3.test import uitree


class OperationsTest(unittest.UITestCase):

    def setUp(self):
        unittest.UITestCase.setUp(self)
        self.bundle_id = "org.laptop.ImageViewerActivity"

    '''
        Test to open a file named test.png in Imageviewer
    '''
    def test_open_file(self):
        uri = os.getcwd() + '/tests/integration/test.png'
        logging.error('OPEN WITH URI %s', uri)
        with self.run_activity_with_uri(uri):
            root = uitree.get_root()
            activity = root.find_child(name="Image Viewer Activity",
                                       role_name="frame")
            try:
                logging.error(activity.dump())
            except:
                logging.error("Error")
                pass
            stop_button = activity.find_child(name="Stop",
                                              role_name="push button")
            full_screen = activity.find_child(name="Fullscreen",
                                              role_name="push button")
            stop_button.click()
            self.assertIsNotNone(stop_button)
            self.assertIsNotNone(full_screen)
            time.sleep(1.5)
    '''
        Test to open a Imageviewer activity and then check that the
        name of the text box in the activity button is equal to
        'Image Viewer Activity'
    '''
    def test_check_activity(self):
        uri = os.getcwd() + '/tests/integration/test.png'
        logging.error('OPEN WITH URI %s', uri)
        with self.run_activity_with_uri(uri):
            root = uitree.get_root()
            activity = root.find_child(name="Image Viewer Activity",
                                       role_name="frame")
            try:
                logging.error(activity.dump())
            except:
                logging.error("Error")
                pass
            all_buttons = activity.find_children(role_name="push button")
            activity_button = all_buttons[0]
            activity_button.click()
            time.sleep(0.25)
            activity_name = activity.find_child(role_name="text")
            self.assertEqual(activity_name.text, "Image Viewer Activity")
            time.sleep(1.5)
    '''
        Test open a image named test.png and then
        test the zoom in button of the activity
    '''
    def test_zoom_in(self):
        uri = os.getcwd() + '/tests/integration/test.png'
        logging.error('OPEN WITH URI %s', uri)
        with self.run_activity_with_uri(uri):
            root = uitree.get_root()
            activity = root.find_child(name="Image Viewer Activity",
                                       role_name="frame")
            try:
                logging.error(activity.dump())
            except:
                logging.error("Error")
                pass
            zoomin_button = activity.find_child(name="Zoom in",
                                                role_name="push button")
            count = 5
            while count:
                zoomin_button.click()
                time.sleep(0.25)
                count -= 1
            self.assertIsNotNone(zoomin_button)
            time.sleep(1.5)
    '''
        Test open a image named test.png and then
        test the zoom out button of the activity
    '''
    def test_zoom_out(self):
        uri = os.getcwd() + '/tests/integration/test.png'
        logging.error('OPEN WITH URI %s', uri)
        with self.run_activity_with_uri(uri):
            root = uitree.get_root()
            activity = root.find_child(name="Image Viewer Activity",
                                       role_name="frame")
            try:
                logging.error(activity.dump())
            except:
                logging.error("Error")
                pass
            zoom_out_button = activity.find_child(name="Zoom out",
                                                  role_name="push button")
            count = 5
            while count:
                zoom_out_button.click()
                time.sleep(0.25)
                count -= 1
            self.assertIsNotNone(zoom_out_button)
            time.sleep(1.5)
    '''
        Test open a image named test.png and then
        test the Fit to Window button of the activity
    '''
    def test_fit_window(self):
        uri = os.getcwd() + '/tests/integration/test.png'
        logging.error('OPEN WITH URI %s', uri)
        with self.run_activity_with_uri(uri):
            root = uitree.get_root()
            activity = root.find_child(name="Image Viewer Activity",
                                       role_name="frame")
            try:
                logging.error(activity.dump())
            except:
                logging.error("Error")
                pass
            zoom_out_button = activity.find_child(name="Zoom out",
                                                  role_name="push button")
            fit_window = activity.find_child(name="Fit to window",
                                             role_name="push button")
            count = 5
            while count:
                zoom_out_button.click()
                time.sleep(0.25)
                count -= 1
            fit_window.click()
            time.sleep(0.5)
            self.assertIsNotNone(zoom_out_button)
            self.assertIsNotNone(fit_window)
            time.sleep(1.5)
    '''
        Test open a image named test.png and then
        test the Orignal Size of image button of the activity
    '''
    def test_orignal_size(self):
        uri = os.getcwd() + '/tests/integration/test.png'
        logging.error('OPEN WITH URI %s', uri)
        with self.run_activity_with_uri(uri):
            root = uitree.get_root()
            activity = root.find_child(name="Image Viewer Activity",
                                       role_name="frame")
            try:
                logging.error(activity.dump())
            except:
                logging.error("Error")
                pass
            zoom_out_button = activity.find_child(name="Zoom out",
                                                  role_name="push button")
            orignal_size = activity.find_child(name="Original size",
                                               role_name="push button")
            count = 5
            while count:
                zoom_out_button.click()
                time.sleep(0.25)
                count -= 1
            orignal_size.click()
            time.sleep(0.5)
            self.assertIsNotNone(zoom_out_button)
            self.assertIsNotNone(orignal_size)
            time.sleep(1.5)
    '''
        Test open a image named test.png and then
        test the rotate clockwise button of the activity
    '''
    def test_rotate_clockwise(self):
        uri = os.getcwd() + '/tests/integration/test.png'
        logging.error('OPEN WITH URI %s', uri)
        with self.run_activity_with_uri(uri):
            root = uitree.get_root()
            activity = root.find_child(name="Image Viewer Activity",
                                       role_name="frame")
            try:
                logging.error(activity.dump())
            except:
                logging.error("Error")
                pass
            rotate_clockwise = activity.find_child(name="Rotate clockwise",
                                                   role_name="push button")
            count = 4
            while count:
                rotate_clockwise.click()
                time.sleep(0.25)
                count -= 1
            self.assertIsNotNone(rotate_clockwise)
            time.sleep(1.5)
    '''
        Test open a image named test.png and then
        test the rotate anticlockwise button of the activity
    '''
    def test_rotate_aclockwise(self):
        uri = os.getcwd() + '/tests/integration/test.png'
        logging.error('OPEN WITH URI %s', uri)
        with self.run_activity_with_uri(uri):
            root = uitree.get_root()
            activity = root.find_child(name="Image Viewer Activity",
                                       role_name="frame")
            try:
                logging.error(activity.dump())
            except:
                logging.error("Error")
                pass
            rotate_aclock = activity.find_child(name="Rotate anticlockwise",
                                                role_name="push button")
            count = 4
            while count:
                rotate_aclock.click()
                time.sleep(0.25)
                count -= 1
            self.assertIsNotNone(rotate_aclock)
            time.sleep(1.5)
