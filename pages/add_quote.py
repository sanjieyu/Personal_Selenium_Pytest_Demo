# Author: Yi Sun(Tim) 2023-09-04

'''Add Quote Page'''

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from pages.admin_portal import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException

class Add_Quote(AdminPage):
    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """

    main_page_loc = (By.ID,'test_sample')

    '''loc for each section in this page'''
    proposal_details_loc = (By.NAME,'test_sample')
    contact_details_loc = (By.NAME,'test_sample')

    # [Remaining 50+ locators redacted for confidentiality]

    '''loc for each section in this page'''
    '''Quote Sucessfully modified popup'''
    '''loc for each element in "Proposal Details" section'''
    '''loc for each element in "Client Contact Details" section'''
    '''loc for each element in "Site Contact Details" section'''
    '''loc for Doors'''
    '''loc for Valication page'''
    '''loc for add successfully'''


    def go_add(self):
        '''Switch to ADD Menu'''
        self.driver.find_element(*self.add_loc).click()

    def go_addquote(self):
        '''Switch to Add Quotes from Add Menu'''
        self.driver.find_element(*self.add_loc).click()
        self.driver.find_element(*self.quote_add_loc).click()
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.contact_details_loc))

    @property
    def check_addquote_url(self):
        '''check the url for Add Quote page'''
        add_quote_url = self.driver.current_url
        return add_quote_url

    @property
    def check_defaulsection(self):
        '''check the default section in Add Quotes page'''
        proposal_details = self.driver.find_element(*self.proposal_details_loc).text
        contact_details = self.driver.find_element(*self.contact_details_loc).text
        site_details = self.driver.find_element(*self.site_details_loc).text
        doors = self.driver.find_element(*self.doors_loc).text
        return proposal_details,contact_details,site_details,doors

    @property
    def check_savequote_btn(self):
        '''check the save quote buton in Add Quotes page'''
        savequote_btn = self.driver.find_element(*self.save_quote_btn)
        if savequote_btn:
            return  True
        else:
            return False
    @property
    def check_proposal_details(self):
        '''check each description of Proplsal Details in Add Quotes page'''
        proposal_num = self.driver.find_element(*self.proposal_num_loc).text
        pricing_cate = self.driver.find_element(*self.pricing_cate_loc).text
        user_quote = self.driver.find_element(*self.user_quote_loc).text
        account_type = self.driver.find_element(*self.account_type_loc).text
        order_date = self.driver.find_element(*self.order_date_loc).text
        quote_status = self.driver.find_element(*self.quote_status_loc).text
        account_cus = self.driver.find_element(*self.account_customer_loc).text
        supply_type = self.driver.find_element(*self.supply_type_loc).text
        return proposal_num,pricing_cate,user_quote,account_type,order_date,quote_status,account_cus,supply_type

    @property
    def check_pricing_cate_value(self):
        '''check each value in "Pricing Category" list'''
        self.driver.find_element(*self.pricing_cate_select).click()
        pricing_value = self.driver.find_element(*self.pricing_cate_select).text
        return pricing_value

    @property
    def check_changeto_Account(self):
        '''The "Account Customer" list should enable after select "Account" in "Account Type" list'''
        wait = WebDriverWait(self.driver,5)
        self.driver.find_element(*self.account_type_select).click()
        account_type_select = Select(wait.until(EC.presence_of_element_located(self.account_type_select)))
        account_type_select.select_by_visible_text('test_sample')
        account_customer_dropdown1 = wait.until(EC.presence_of_element_located(self.account_customer_select))
        print('attribute is:',account_customer_dropdown1.get_attribute)
        is_disabled = account_customer_dropdown1.get_attribute("disabled")
        if is_disabled:
            return  True
        else:
            return False

    @property
    def check_contact_details(self):
        '''check each section in "Contact Details"'''
        client_contact_details = self.driver.find_element(*self.client_contact_details_loc).text
        site_contact_details = self.driver.find_element(*self.site_contact_details_loc).text
        return client_contact_details,site_contact_details

    @property
    def check_client_contact_details(self):
        '''check each section in "Client Contact Details"'''
        client_name_details = self.driver.find_element(*self.client_name_loc).text
        cus_pur_order = self.driver.find_element(*self.customer_purchase_order_loc).text
        contact_name_details = self.driver.find_element(*self.contact_name_loc).text
        contact_mobile_details = self.driver.find_element(*self.contact_mobile_loc).text
        contact_email_details = self.driver.find_element(*self.contact_email_loc).text
        contact_address_details = self.driver.find_element(*self.contact_address_loc).text
        contact_suburb_details = self.driver.find_element(*self.contact_suburb_loc).text
        contact_postcode_details = self.driver.find_element(*self.contact_postcode_loc).text
        return (client_name_details,cus_pur_order,contact_name_details,contact_mobile_details,contact_email_details,
                contact_address_details,contact_suburb_details,contact_postcode_details)

    @property
    def check_client_name_box(self):
        '''check the input editbox for "Client Name"'''
        client_name_box_display = self.driver.find_element(*self.client_name_box)
        if client_name_box_display.is_displayed():
            return True
        else:
            return False

    @property
    def check_order_num_box(self):
        '''check the input editbox for "Customer Purchase Order"'''
        cus_order_display = self.driver.find_element(*self.order_num_box)
        if cus_order_display.is_displayed():
            return True
        else:
            return False

    @property
    def check_contact_name_box(self):
        '''check the input editbox for "Contact Name"'''
        contact_name_display = self.driver.find_element(*self.contact_name_box)
        if contact_name_display.is_displayed():
            return True
        else:
            return False

    @property
    def check_contact_mobile_box(self):
        '''check the input editbox for "Contact Mobile"'''
        contact_mobile_display = self.driver.find_element(*self.contact_mobile_box)
        if contact_mobile_display.is_displayed():
            return True
        else:
            return False


    @property
    def check_adddoor_menu(self):
        '''check the add new door menu'''
        door_item = []
        self.driver.implicitly_wait(3)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        self.driver.find_element(*self.add_door_btn).click()
        add_door_menu = self.driver.find_element(*self.add_door_menu)
        menu_element = add_door_menu.find_elements(By.ID,"test_sample")
        for item in menu_element:
            door_item.append(item.text)
        return door_item

    @property
    def check_validation(self):
        '''check the validation for Add Quote page'''
        self.driver.find_element(*self.save_quote_btn).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        validation_error = self.driver.find_element(*self.validation_error_loc).text
        validation_1 = self.driver.find_element(*self.validation_1_loc).text
        validation_2  = self.driver.find_element(*self.validation_2_loc).text
        self.driver.find_element(*self.validation_ok_btn).click()
        return validation_error,validation_1,validation_2

    @property
    def check_add_quote_success(self):
        '''check Add Quote Successfully'''
        select_supplytype = Select(self.driver.find_element(*self.supply_type_select))
        select_supplytype.select_by_index(1)
        self.driver.find_element(*self.contact_email_box).send_keys('test_sample')
        select_accounttype = Select(self.driver.find_element(*self.account_type_select))
        select_accounttype.select_by_visible_text("test_sample")
        self.driver.find_element(*self.account_customer_btn).click()
        self.driver.find_element(*self.propertygroup_customer_loc).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*self.save_quote_btn).click()
        self.driver.execute_script("window.scrollTo(0, 0);")
        quote_success_created = WebDriverWait(self.driver,3).until(EC.visibility_of_element_located
                                                                   (self.quote_success_created_loc)).text
        return quote_success_created

    @property
    def change_quote_detail(self):
        '''Change quote details from Account Cusomter to Cash sale, use for "add quote with door.py"'''
        select_supplytype = Select(self.driver.find_element(*self.supply_type_select))
        select_supplytype.select_by_index(2)
        select_accounttype = Select(self.driver.find_element(*self.account_type_select))
        select_accounttype.select_by_visible_text("Cash sale")
        self.driver.find_element(*self.client_name_box).send_keys("test_sample")
        self.driver.find_element(*self.contact_name_box).send_keys("test_sample")
        self.driver.find_element(*self.contact_mobile_box).send_keys("test_sample")
        self.driver.find_element(*self.contact_email_box).send_keys("test_sample")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*self.save_quote_btn).click()
        self.driver.find_element(*self.proceed_quote_btn).click()
        alert = self.driver.switch_to.alert
        alert.accept()


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://test_sample/")
    driver.implicitly_wait(10)
    login = Add_Quote(driver)
    login.typeUserName('test_sample')
    login.typePassword('test_sample')
    login.clickLogin()
    login.go_addquote()
    # login.check_addquote_url
    # login.check_searchurl