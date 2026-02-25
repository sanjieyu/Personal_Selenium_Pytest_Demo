# Author: Yi Sun(Tim) 2024-06-16

'''Test Add Quote - Pytest Version'''

import pytest
from pages.add_quote import Add_Quote


class Test_Add_Quote():

    @pytest.mark.p0
    def test_add_quote_001(self, add_quote):
        assert add_quote.check_addquote_url == "http://test_sample"

    @pytest.mark.p1
    def test_add_quote_002(self, add_quote):
        assert add_quote.check_defaulsection == ('test_sample','test_sample','test_sample','test_sample')

    @pytest.mark.p1
    def test_add_quote_003(self, add_quote):
        assert add_quote.check_savequote_btn

    @pytest.mark.p2
    def test_add_quote_004(self, add_quote):
        assert add_quote.check_proposal_details == ('test_sample','test_sample','test_sample','test_sample','test_sample',
                          'test_sample','test_sample','test_sample')