from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import selenium.common
from robot.utils import asserts
from robot.api.deco import keyword


class WestField(object):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self.browser = None

    def ui_setup(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)

    def ui_teardown(self):
        self.browser.close()

    def go_to_page(self, url):
        self.browser.get(url=url)

    def click_button_by_class(self, class_button):
        try:
            self.browser.find_element_by_class_name(class_button).click()
        except selenium.common.exceptions.NoSuchElementException:
            asserts.fail('\nUnable to find class {}!'.format(close))

    def enter_take_over(self, class_take_over):
        try:
            take_over = self.browser.find_element_by_class_name(class_take_over)
            take_over.click()
        except NoSuchElementException:
            asserts.fail('****** Expected page element not found!\n'
                         '****** Unable to locate "{page_element}".\n'.format(page_element=class_take_over))

    def click_by_xpath(self, xpath):
        self.browser.find_element_by_xpath(xpath).click()

    def subscribe_form(self, css_selector):
        name_input = self.browser.find_element_by_css_selector(css_selector=css_selector)

    @keyword('Enter ${text} into ${form_field}')
    def send_text_to_form(self, form_field, text):
        self.browser.find_element_by_xpath(text).send_keys(form_field)

