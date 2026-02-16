# Author:Yi Sun(Tim) 2023-5-05

'''Add a Quote with a Custom  door function'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.custom_door import *
from pages.add_custom_door import Add_Custom_Door

class Add_Quote_With_CustomDoor(Add_Custom_Door):

    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    proposal_number_loc = (By.ID,'test_sample')
    find_quote_input = (By.ID,'test_sample')
    find_quote_btn = (By.ID,'test_sample')

    # [Remaining 5+ locators redacted for confidentiality]


    def __init__(self,driver):
        self.driver = driver
        self.add_quote = Add_Quote(self.driver)
        self.add_custom_door = Add_Custom_Door(self.driver)

    def add_custom_door_fun(self):
        self.add_quote.go_addquote()
        self.add_custom_door.go_addcustomdoor()
        self.add_custom_door.add_custom_detail()
        self.add_quote.check_add_quote_success

    @property
    def get_proposal_number(self):
        global proposal_number
        proposal_number = self.driver.find_element(*self.proposal_number_loc).get_attribute('value')
        return proposal_number

    def search_new_quote(self):
        self.driver.refresh()
        self.driver.find_element(*self.find_quote_input).send_keys(proposal_number)
        self.driver.find_element(*self.find_quote_btn).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.searched_door_no_loc))

    @property
    def verify_new_quote(self):
        searched_proposal_no = self.driver.find_element(*self.searched_proposal_no_loc).text
        searched_door_no = self.driver.find_element(*self.searched_door_no_loc).text
        searched_door_status = self.driver.find_element(*self.searched_door_status_loc).text
        return searched_door_no,searched_door_status

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://test_sample/")
    page = Add_Quote_With_CustomDoor(driver)
    page.typeUserName('test_sample')
    page.typePassword('test_sample')
    page.clickLogin()
    page.add_custom_door_fun()
    page.get_proposal_number
    page.search_new_quote()
    page.verify_new_quote