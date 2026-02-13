# Author: Yi Sun(Tim) 2024-06-16

'''Test Add Quote - Pytest Version'''

import pytest
from pages.add_quote import Add_Quote


class Test_Add_Quote():

    def test_add_quote_001(self, add_quote):
        assert add_quote.check_addquote_url == "http://xxxx/Quote/Create"

    def test_add_quote_002(self, add_quote):
        assert add_quote.check_defaulsection == ('Proposal Details','Contact Details','Site Details','Doors')

    def test_add_quote_003(self, add_quote):
        assert add_quote.check_savequote_btn

    def test_add_quote_004(self, add_quote):
        assert add_quote.check_proposal_details == ('Proposal Number','Pricing Category','User','Account Type','Order Date',
                          'Quote Status','Account Customer','Supply Type')