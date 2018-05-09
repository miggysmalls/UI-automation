from selenium import webdriver
import selenium.common
from robot.utils import asserts
from robot.api.deco import keyword


class WestField(object):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self.browser = None

    def ui_setup(self):
        self.browser = webdriver.Firefox()

        self.browser.implicitly_wait(10)

    def ui_teardown(self):
        self.browser.close()

    def go_to_page(self, url):
        self.browser.get(url=url)

    @keyword('Click on ${class_button} to close window')
    def close_window_by_class(self, class_button):
        try:
            button = self.browser.find_element_by_class_name(class_button)
            button.click()
        except selenium.common.exceptions.NoSuchElementException:
            asserts.fail('\nUnable to find class {}!'.format(close))

    def enter_take_over(self, class_take_over):
        take_over = self.browser.find_element_by_class_name(class_take_over)
        take_over.click()

    def click_by_xpath(self, xpath):
        selection = self.browser.find_element_by_xpath(xpath)
        selection.click()

    def subscribe_form(self, css_selector):
        name_input = self.browser.find_element_by_css_selector(css_selector=css_selector)

    @keyword('XPath ${name}')
    def get_form_field_by_id(self, name):
        name_input = self.browser.find_element_by_id(name)
        name_input.send_keys('Miggy')
