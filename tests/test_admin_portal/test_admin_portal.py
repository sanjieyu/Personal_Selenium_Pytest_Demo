# Author: Yi Sun(Tim) 2023-08-29

'''Admin Page - Pytest Version'''

import pytest
from pages.admin_portal import AdminPage

@pytest.mark.p0
class Test_Admin_Portal():

    def test_admin_portal_001(self,admin_page):
        '''Verify the url of Admin login Page'''
        assert "test_sample" in admin_page.get_url.lower()

    def test_admin_portal_002(self,admin_page):
        '''Verify the default Sections in Admin login Page'''
        add_menu, list_menu, account_menu = admin_page.check_default_menu
        assert "test_sample" in add_menu
        assert "test_sample" in list_menu
        assert "test_sample" in account_menu

    def test_admin_portal_003(self,admin_page):
        '''Verify the Find Quote in Admin Login page'''
        assert admin_page.check_find_quote is True

    def test_admin_portal_004(self,admin_page):
        '''Verify the Find Address in Admin Login page'''
        assert admin_page.check_find_address is True

    def test_admin_portal_005(self,admin_page):
        '''Verify the Find Client in Admin Login page'''
        assert admin_page.check_find_client is True

    def test_admin_portal_006(self,admin_page):
        '''Verify the Copyright and Terms'''
        copyright_, terms = admin_page.check_copyright
        assert "2023" in copyright_ or "©" in copyright_
        assert "Terms" in terms