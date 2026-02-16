

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class AdminPortal:
    def __init__(self, driver):
        self.driver = driver
        self.username_loc = (By.ID,'test_sample')
        self.password_loc = (By.ID,'test_sample')
        self.login_loc = (By.ID,'test_sample')
        self.loginError_loc = (By.ID,'test_sample')  # Example locator
        self.forgetpwd_loc = (By.LINK_TEXT, 'test_sample')
        self.forgetdescription_loc = (By.ID,'test_sample')
        self.inputemail_loc = (By.ID,'test_sample')
        self.forgetsubmit_loc = (By.ID,'test_sample')
        self.wrongemailwaring_loc = (By.ID,'test_sample')
        self.passwordrequire_loc = (By.ID,'test_sample')

    def type_username(self, username):
        self.driver.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.driver.find_element(*self.password_loc).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_loc).click()

    def login(self, username, password):
        self.type_username(username)
        self.type_password(password)
        self.click_login()

    def get_username_text(self):
        return self.driver.find_element(*self.username_loc).get_attribute("value")

    def get_login_error(self):
        return self.driver.find_element(*self.loginError_loc).text

    def click_forget(self):
        self.driver.find_element(*self.forgetpwd_loc).click()

    def get_forget_description(self):
        return self.driver.find_element(*self.forgetdescription_loc).text

    def submit_wrong_email(self):
        self.driver.find_element(*self.inputemail_loc).send_keys('test_sample')
        self.driver.find_element(*self.forgetsubmit_loc).click()

    def get_wrong_email_warning(self):
        return self.driver.find_element(*self.wrongemailwaring_loc).text

    def submit_username(self):
        self.driver.find_element(*self.inputemail_loc).send_keys('test_sample')
        self.driver.find_element(*self.forgetsubmit_loc).click()

    def get_password_require_warning(self):
        return self.driver.find_element(*self.passwordrequire_loc).text


# --- Fixtures ---

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://test_sample")
    yield driver
    driver.quit()