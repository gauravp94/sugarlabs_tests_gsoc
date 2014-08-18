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
        activity = root.find_child(name="Write Activity",
                                   role_name="frame")
        return activity


class OperationsTest(unittest.UITestCase, TestHelper):

    '''
        Setting up things for running the write tests
    '''
    def setUp(self):
        unittest.UITestCase.setUp(self)
        self.bundle_id = "org.laptop.AbiWordActivity"
        self.screen_width = Gtk.Window().get_screen().get_width()
        self.screen_height = Gtk.Window().get_screen().get_height()

    '''
        Test to click on the activity button on the
        activity toolbar and then check the name of the
        activity to be write activity.
    '''
    def test_check_activity(self):
        with self.run_activity():
            activity = self.get_activity()
            all_push_buttons = activity.find_children(role_name="push button")
            activity_button = all_push_buttons[0]
            activity_button.click()
            time.sleep(0.50)
            description = activity.find_child(name="Description",
                                              role_name="push button")
            private = activity.find_child(name="Private",
                                          role_name="push button")
            rich_text = activity.find_child(name="Rich Text (RTF)",
                                            role_name="push button")
            hypertext = activity.find_child(name="Hypertext (HTML)",
                                            role_name="push button")
            plain_text = activity.find_child(name="Plain Text (TXT)",
                                             role_name="push button")
            pdf_format = activity.find_child(name=
                                             "Portable Document Format (PDF)",
                                             role_name="push button")
            activity_name = activity.find_child(role_name="text")
            self.assertIsNotNone(description)
            self.assertIsNotNone(private)
            self.assertIsNotNone(rich_text)
            self.assertIsNotNone(hypertext)
            self.assertIsNotNone(plain_text)
            self.assertIsNotNone(pdf_format)
            self.assertIsNotNone(activity_name)
            self.assertEqual(activity_name.text.strip(), "Write Activity")
            time.sleep(2.50)

    '''
        Test to click on the edit button on the
        activity toolbar and then check the various
        buttons in the edit section.
    '''
    def test_edit_tab(self):
        with self.run_activity():
            activity = self.get_activity()
            all_push_buttons = activity.find_children(role_name="push button")
            edit_toolbar = all_push_buttons[1]
            edit_toolbar.click()
            time.sleep(1.50)
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
            time.sleep(2.50)

    '''
        Test to click on the edit button on the
        activity toolbar and then check the working
        of the search in it.
    '''
    def test_search(self):
        with self.run_activity():
            activity = self.get_activity()
            uitree.type_text('This is the test input\n')
            uitree.type_text('This is a test file\n')
            uitree.type_text('This is test1 test2 test3 \n')
            edit_toolbar = activity.find_child(name="Edit",
                                               role_name="push button")
            edit_toolbar.click()
            time.sleep(1.0)
            previous_button = activity.find_child(name="Find previous",
                                                  role_name="push button")
            next_button = activity.find_child(name="Find next",
                                              role_name="push button")
            search_label = activity.find_child(name="Search: ",
                                               role_name="label")
            search_box = activity.find_child(role_name="text")
            search_box.click(1,
                             0.05*self.screen_width,
                             0.03*self.screen_height)
            time.sleep(1.0)
            uitree.type_text('test')
            time.sleep(1.0)
            count = 3
            while count:
                next_button.click()
                time.sleep(0.25)
                count -= 1
            count = 3
            while count:
                previous_button.click()
                time.sleep(0.25)
                count -= 1
            self.assertIsNotNone(edit_toolbar)
            self.assertIsNotNone(search_box)
            self.assertIsNotNone(previous_button)
            self.assertIsNotNone(next_button)
            self.assertEqual(search_box.text, "test")
            self.assertEqual(search_label.text, "Search: ")
            time.sleep(2.50)

    '''
        Test to click on the view button on the
        activity toolbar and then check the various
        buttons in the view section.
    '''
    def test_view_tab(self):
        with self.run_activity():
            activity = self.get_activity()
            uitree.type_text('This is a test input')
            time.sleep(1.0)
            view_toolbar = activity.find_child(name="View",
                                               role_name="push button")
            view_toolbar.click()
            time.sleep(0.50)
            zoom_in = activity.find_child(name="Zoom Out",
                                          role_name="push button")
            zoom_out = activity.find_child(name="Zoom In",
                                           role_name="push button")
            zoom_width = activity.find_child(name="Zoom to width",
                                             role_name="push button")
            percent_label = activity.find_child(name="%",
                                                role_name="label")
            page_label = activity.find_child(name="Page: ",
                                             role_name="label")
            spin_btns = activity.find_children(role_name="spin button")
            count = 10
            time.sleep(2.0)
            while count:
                zoom_in.click()
                time.sleep(0.5)
                count -= 1
            zoom_width.click()
            time.sleep(0.5)
            count = 10
            time.sleep(1.0)
            while count:
                zoom_out.click()
                time.sleep(0.5)
                count -= 1
            time.sleep(1.0)
            zoom_width.click()
            self.assertIsNotNone(zoom_in)
            self.assertIsNotNone(zoom_out)
            self.assertIsNotNone(zoom_width)
            self.assertEqual(percent_label.text, "%")
            self.assertEqual(page_label.text, "Page: ")
            self.assertEqual(len(spin_btns), 2)
            time.sleep(2.50)

    '''
        Test to click on the speak button on the
        activity toolbar and then check the various
        buttons in the speak section.
    '''
    def test_speak_tab(self):
        with self.run_activity():
            activity = self.get_activity()
            uitree.type_text('This is a test input')
            time.sleep(1.5)
            all_push_buttons = activity.find_children(role_name="push button")
            speak_btn = all_push_buttons[3]
            speak_btn.click()
            time.sleep(1.50)
            uitree.drag(self.screen_width*0.09,
                        self.screen_height*0.20,
                        self.screen_width*0.70,
                        self.screen_height*0.30)
            time.sleep(2.50)
            play_btn = activity.find_child(role_name="toggle button")
            stop_btn = activity.find_child(name="Stop",
                                           role_name="push button")
            time.sleep(0.50)
            '''
            TO FIX: Often TTS module crashes in some versions of abiword rpm
                    Hence commented the below line
            play_btn.click()
            '''
            self.assertIsNotNone(play_btn)
            self.assertIsNotNone(stop_btn)
            self.assertIsNotNone(speak_btn)
            time.sleep(2.50)

    '''
        Test to click on the text button on the
        activity toolbar and then check the various
        buttons in the text section.
    '''
    def test_text_tab(self):
        with self.run_activity():
            activity = self.get_activity()
            uitree.type_text('This is a test input')
            time.sleep(1)
            text_tab = activity.find_child(name="Text",
                                           role_name="push button")
            text_tab.click()
            time.sleep(1)
            sans_btn = activity.find_child(name="Sans",
                                           role_name="push button")
            sans_btn.click()
            time.sleep(1)
            all_panel = activity.find_children(role_name="panel")
            font_choose = all_panel[17]
            all_font = font_choose.find_children(role_name="push button")
            small_font = all_font[0]
            large_font = all_font[1]
            count = 4
            while count:
                time.sleep(0.25)
                count -= 1
                large_font.click()
            uitree.type_text(" Large font")
            time.sleep(0.50)
            count = 8
            while count:
                time.sleep(0.25)
                count -= 1
                small_font.click()
            time.sleep(0.50)
            uitree.type_text(" Small font \n")
            bold_text = all_panel[18].find_child(role_name="toggle button")
            italic_text = all_panel[19].find_child(role_name="toggle button")
            under_text = all_panel[20].find_child(role_name="toggle button")
            color_text = all_panel[21].find_child(role_name="push button")
            choose_align = activity.find_child(name="Choose alignment",
                                               role_name="push button")
            bold_text.click()
            time.sleep(0.50)
            uitree.type_text(" Bold Text \n")
            time.sleep(0.50)
            bold_text.click()
            time.sleep(0.5)
            italic_text.click()
            time.sleep(0.50)
            uitree.type_text(" Italic Text \n")
            time.sleep(0.50)
            italic_text.click()
            time.sleep(0.5)
            under_text.click()
            time.sleep(0.50)
            uitree.type_text(" Underline Text \n")
            time.sleep(0.50)
            under_text.click()
            time.sleep(0.50)
            color_text.click()
            time.sleep(0.50)
            choose_align.click()
            self.assertIsNotNone(text_tab)
            self.assertIsNotNone(sans_btn)
            self.assertIsNotNone(small_font)
            self.assertIsNotNone(large_font)
            self.assertIsNotNone(bold_text)
            self.assertIsNotNone(italic_text)
            self.assertIsNotNone(under_text)
            self.assertIsNotNone(color_text)
            self.assertIsNotNone(choose_align)
            time.sleep(2.50)

    '''
        Test to click on the paragraph button on the
        activity toolbar and then check the various
        buttons in the paragraph section.
    '''
    def test_para_tab(self):
        with self.run_activity():
            activity = self.get_activity()
            uitree.type_text('This is a test input\n')
            time.sleep(1)
            para_tab = activity.find_child(name="Paragraph",
                                           role_name="push button")
            para_tab.click()
            time.sleep(1.50)
            normal_text = activity.find_child(name="Normal",
                                              role_name="radio button")
            heading_1 = activity.find_child(name="Heading 1",
                                            role_name="radio button")
            heading_2 = activity.find_child(name="Heading 2",
                                            role_name="radio button")
            heading_3 = activity.find_child(name="Heading 3",
                                            role_name="radio button")
            heading_4 = activity.find_child(name="Heading 4",
                                            role_name="radio button")
            block_text = activity.find_child(name="Block Text",
                                             role_name="radio button")
            plain_text = activity.find_child(name="Plain Text",
                                             role_name="radio button")
            select_list = activity.find_child(name="Select list",
                                              role_name="push button")
            normal_text.click()
            time.sleep(0.5)
            uitree.type_text('Normal Text\n')
            time.sleep(1)
            heading_1.click()
            time.sleep(0.5)
            uitree.type_text('Heading 1 Text\n')
            time.sleep(1)
            heading_2.click()
            time.sleep(0.5)
            uitree.type_text('Heading 2 Text\n')
            time.sleep(1)
            heading_3.click()
            time.sleep(0.5)
            uitree.type_text('Heading 3 Text\n')
            time.sleep(1)
            heading_4.click()
            time.sleep(0.5)
            uitree.type_text('Heading 4 Text\n')
            time.sleep(1)
            block_text.click()
            time.sleep(0.5)
            uitree.type_text('Block Text\n')
            time.sleep(1)
            plain_text.click()
            time.sleep(0.5)
            uitree.type_text('Plain Text\n')
            time.sleep(1)
            select_list.click()
            self.assertIsNotNone(para_tab)
            self.assertIsNotNone(normal_text)
            self.assertIsNotNone(heading_1)
            self.assertIsNotNone(heading_2)
            self.assertIsNotNone(heading_3)
            self.assertIsNotNone(heading_4)
            self.assertIsNotNone(block_text)
            self.assertIsNotNone(plain_text)
            self.assertIsNotNone(select_list)
            time.sleep(2.50)

    '''
        Test to click on the table button on the
        activity toolbar and then check the various
        buttons in the table section.
    '''
    def test_table_tab(self):
        with self.run_activity():
            activity = self.get_activity()
            uitree.type_text('This is a test input\n')
            table_tab = activity.find_child(name="Table",
                                            role_name="push button")
            table_tab.click()
            time.sleep(0.50)
            create_table = activity.find_child(name="Create table",
                                               role_name="push button")
            insert_row = activity.find_child(name="Insert Row",
                                             role_name="push button")
            delete_row = activity.find_child(name="Delete Row",
                                             role_name="push button")
            insert_col = activity.find_child(name="Insert Column",
                                             role_name="push button")
            del_col = activity.find_child(name="Delete Column",
                                          role_name="push button")
            create_table.click()
            self.assertIsNotNone(table_tab)
            self.assertIsNotNone(insert_row)
            self.assertIsNotNone(delete_row)
            self.assertIsNotNone(create_table)
            self.assertIsNotNone(insert_col)
            self.assertIsNotNone(del_col)
            time.sleep(2.50)

    '''
        Test to check the add image button on the
        activity toolbar
    '''
    def test_image_tab(self):
        with self.run_activity():
            activity = self.get_activity()
            uitree.type_text('This is a test input\n')
            image_tab = activity.find_child(name="Insert Image",
                                            role_name="push button")
            self.assertIsNotNone(image_tab)
            time.sleep(2.50)

    '''
        Test to open an instance of write and
        and then stop the activity using the
        stop button.
    '''
    def test_stop_activity(self):
        with self.run_activity():
            activity = self.get_activity()
            uitree.type_text('This is a test input\n')
            stop_tab = activity.find_child(name="Stop",
                                           role_name="push button")
            stop_tab.click()
            self.assertIsNotNone(stop_tab)
            time.sleep(2.50)
