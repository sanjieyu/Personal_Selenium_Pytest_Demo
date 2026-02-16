# Author:Yi Sun(Tim) 2024-01-19

'''Test the Dealer Portal Page'''

import pytest
from pages.dealer_portal import *

class Test_Dealer_Portal():

    def test_dealer_portal_ui_001(self,dealer_portal):
        assert dealer_portal.check_dealer_url == "http://test_sample"

    def test_dealer_portal_ui_002(self,dealer_portal):
        assert dealer_portal.check_default_values == ("test_sample","test_sample","test_sample")

    def test_dealer_portal_ui_003(self,dealer_portal):
        assert dealer_portal.check_find_dealer_quote is True

    def test_dealer_portal_ui_004(self,dealer_portal):
        assert dealer_portal.check_account_menu == ("test_sample","test_sample")
