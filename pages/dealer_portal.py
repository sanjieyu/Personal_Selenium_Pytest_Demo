# Author:Yi Sun(Tim) 2024-03-13

'''Dealer Portal Page'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.admin_portal import AdminPage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Deal_Portal(AdminPage):

    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    '''loc for the dealer portal page'''
    find_quote_box = (By.ID,'test_sample')
    find_quote_btn = (By.Name, 'test_sample')
    account_dealer_loc = (By.ID,'test_sample')

    '''loc for Add btn'''
    '''loc for Search btn'''
    '''loc for Account menu'''


    @property
    def check_dealer_url(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.add_dealer_quote_loc)) #new added
        dealer_url = self.driver.current_url
        return dealer_url

    @property
    def check_default_values(self):
        add_quote = self.driver.find_element(*self.add_dealer_quote_loc).text
        search_quote = self.driver.find_element(*self.list_dealer_quote_loc).text
        account_menu = self.driver.find_element(*self.account_loc).text
        return  add_quote,search_quote,account_menu

    @property
    def check_find_dealer_quote(self):
        find_dealer_quote = self.driver.find_element(*self.find_quote_box)
        if find_dealer_quote.is_displayed():
            return  True
        else:
            return False


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://test_sample/")
    driver.implicitly_wait(10)

    login = Deal_Portal(driver)
    login.typeUserName('test_sample')
    login.typePassword('test_sample!')
    login.clickLogin()
