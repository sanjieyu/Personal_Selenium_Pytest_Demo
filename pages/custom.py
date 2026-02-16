# Author:Yi Sun(Tim) 2023-9-29

'''Add a Custom Door Details Page'''

from pages.add_quote import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class Custom_Door(Add_Quote):

    """
        Note: For security and confidentiality, specific XPath/CSS selectors
        have been replaced with 'test_sample', and additional private locators
        have been omitted from this public sample.
    """
    add_door_menu = (By.ID,'test_sample')
    add_custom_btn = (By.NAME,'test_sample')
    add_btn_loc = (By.CSS_SELECTOR, "[aria-label='test_sample']")

    # [Remaining 50+ locators redacted for confidentiality]
    '''loc for each element for install details'''
    '''loc for each element for SIZE details'''
    '''loc for each element for Panels details'''
    '''loc for each element for checkboxes details'''
    '''loc for Opener details'''
    '''loc for other elements details '''
    '''loc for additional infomation details '''
    '''loc for Extra and Site Pictures'''
    '''loc for each element in Extra'''

    def go_addcustomdoor(self):
        '''Open the Add Custom Door from Quote Page'''
        self.driver.find_element(*self.add_door_menu).click()
        self.driver.find_element(*self.add_custom_btn).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])


    @property
    def check_customdoor_page(self):
        '''check the main elements in the page'''
        form_element = self.driver.find_element(*self.door_main_page)
        standarddoor_title = self.driver.find_element(*self.title_loc).text
        self.driver.execute_script("arguments[0].scrollIntoView(false);", form_element)
        return standarddoor_title

    @property
    def check_install_details(self):
        '''check each element for install details'''
        install_type = self.driver.find_element(*self.install_type_loc).text
        design = self.driver.find_element(*self.design_loc).text
        colour_category = self.driver.find_element(*self.colour_category_loc).text
        door_colour = self.driver.find_element(*self.door_colour_loc).text
        frame_colour = self.driver.find_element(*self.frame_colour_loc).text
        timber_profile = self.driver.find_element(*self.timber_profile_loc).text
        insert_material = self.driver.find_element(*self.insert_material_loc).text
        insert_location = self.driver.find_element(*self.insert_location_loc).text
        insert_type = self.driver.find_element(*self.insert_type_loc).text
        insert_colour = self.driver.find_element(*self.insert_colour_loc).text
        insert_other = self.driver.find_element(*self.insert_other_loc).text
        custom_colour = self.driver.find_element(*self.custom_colour_loc).text
        return  (install_type,design,colour_category,door_colour,frame_colour,timber_profile,insert_material,
                 insert_location,insert_type,insert_colour,insert_other,custom_colour)

    @property
    def check_install_type(self):
        '''check the install type dropdown'''
        self.driver.find_element(*self.install_type_select).click()
        install_type_list = self.driver.find_element(*self.install_type_select).text
        return  install_type_list



    @property
    def check_door_colour_custom(self):
        '''check the Door Colour dropdown for Custom Colour Category'''
        global colour_category
        colour_category = Select(self.driver.find_element(*self.colour_category_select))
        custom_colour = colour_category.select_by_visible_text('Custom')
        door_colour_list = self.driver.find_element(*self.door_colour_select)
        if door_colour_list.is_enabled():
            return  True
        else:
            return False

    @property
    def check_colour_custom(self):
        '''check the Door Colour dropdown for Custom Category'''
        custom = colour_category.select_by_visible_text('Custom')
        custom_colour = self.driver.find_element(*self.door_colour_select)
        if custom_colour.is_enabled():
            return  False
        else:
            return True

    @property
    def check_customcolour_box(self):
        '''check the Custom Colour input box should be disable by default'''
        custom_colour_box = self.driver.find_element(*self.custom_colour_inputbox)
        if custom_colour_box.is_enabled():
            return  False
        else:
            return True

    @property
    def check_customcolourbox_custom(self):
            '''check the Custom Colour input box should be enable for Custom Colour Category'''
            colour_category1 = Select(self.driver.find_element(*self.colour_category_select))
            custom = colour_category1.select_by_visible_text('test_sample')
            custom_colour_box = self.driver.find_element(*self.custom_colour_inputbox)
            if custom_colour_box.is_enabled():
                return True
            else:
                return False

    @property
    def check_openinglh_default(self):
        '''check the default value for Opening Size LH'''
        openinglh_default = self.driver.find_element(*self.opensize_lh_select).get_attribute('value')
        return  openinglh_default



if __name__ == '__main__':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("http://test_sample/")
        driver.implicitly_wait(10)
        page = Custom_Door(driver)
        page.typeUserName('test_sample')
        page.typePassword('test_sample')
        page.clickLogin()
        page.go_addquote()
        page.go_addcustomdoor()
