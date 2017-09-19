from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException



class NewVisitorTest(unittest.TestCase):



    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        MAX_WAIT = 10
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except(AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Wafa has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)
        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Clean the house'" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Clean the house')

        # When she hits enter, the page updates, and now the page lists
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Clean the house',  [row.text for row in rows])

        # There is still a text box inviting her to add another item. She

        # The page updates again, and now shows both items on her list

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Clean the lawn')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on her list

        #  Wafa wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep

        def test_can_start_a_list_for_one_user(self):
            #  Wafa has heard about a cool new online to-do app. She goes

            # The page updates again, and now shows both items on her list
            self.wait_for_row_in_list_table('1: Clean the house')
            self.wait_for_row_in_list_table('2: Clean the lawn')

        def test_multiple_users_can_start_lists_at_different_urls(self):
        #  wafa starts a new to-do list
            self.browser.get(self.live_server_url)
            inputbox = self.browser.find_element_by_id('id_new_item')
            inputbox.send_keys('Buy coats')
            inputbox.send_keys(Keys.ENTER)
            self.wait_for_row_in_list_table('1: Buy coats')

            # She notices that her list has a unique URL
            wafa_list_url = self.browser.current_url
            self.assertRegex(wafa_list_url, '/lists/.+')

            # Now a new user, Flora, comes along to the site.

            ## We use a new browser session to make sure that no information
            ## of wafa's is coming through from cookies etc'

            self.browser.quit()
            self.browser = webdriver.Firefox()

            # Francis visits the home page.  There is no sign of Edith's
            # list
            self.browser.get(self.live_server_url)
            page_text = self.browser.find_element_by_tag_name('body').text
            self.assertNotIn('Buy coats', page_text)
            self.assertNotIn('make a fly', page_text)

            # Francis starts a new list by entering a new item. He
            # is less interesting than Edith...
            inputbox = self.browser.find_element_by_id('id_new_item')
            inputbox.send_keys('Buy milk')
            inputbox.send_keys(Keys.ENTER)
            self.wait_for_row_in_list_table('1: Buy milk')

            # Francis gets his own unique URL
            flora_list_url = self.browser.current_url
            self.assertRegex(flora_list_url, '/lists/.+')
            self.assertNotEqual(flora_list_url, wafa_list_url)

            # Again, there is no trace of Edith's list
            page_text = self.browser.find_element_by_tag_name('body').text
            self.assertNotIn('Buy coats', page_text)
            self.assertIn('Buy milk', page_text)

            # Satisfied, they both go back to sleep

            self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
