# Author: Yi Sun(Tim) 2023-08-29

'''Admin Page - Pytest Version'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_admin import Admin_Portal


class AdminPage(Admin_Portal):

    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    '''loc for default values in this page'''
    eco_icon_loc = (By.ID,'test_sample')
    add_loc = (By.CSS_SELECTOR, 'test_sample')
    list_loc = (By.NAME,'test_sample')

    # [Remaining 30+ locators redacted for confidentiality]
    '''Add Menu'''
    '''List Menu'''
    '''Account Menu'''
    '''Add Menu'''
    '''List Menu'''
    '''Account Menu'''


    @property
    def get_url(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.copyright_loc)
        )
        return self.driver.current_url

    @property
    def check_default_menu(self):
        return (
            self.driver.find_element(*self.add_loc).text,
            self.driver.find_element(*self.list_loc).text,
            self.driver.find_element(*self.account_loc).text,
        )

    @property
    def check_find_quote(self):
        return self.driver.find_element(*self.findquote_box_loc).is_displayed()

    @property
    def check_find_address(self):
        return self.driver.find_element(*self.findaddress_box_loc).is_displayed()

    @property
    def check_find_client(self):
        return self.driver.find_element(*self.findclient_box_loc).is_displayed()

    @property
    def check_copyright(self):
        return (
            self.driver.find_element(*self.copyright_loc).text,
            self.driver.find_element(*self.terms_loc).text
        )

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://test_sample")
    page = AdminPage(driver)
    page.typeUserName('test_sample')
    page.typePassword('test_sample')
    page.clickLogin()
    page.get_url
    driver.quit()