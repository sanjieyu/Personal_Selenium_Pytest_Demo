# Author:Yi Sun(Tim) 2024-5-05

'''Test Add a Quote with a Custom door function'''

import pytest
from pages.add_quote_with_parts import Add_Quote_With_CustomDoor

@pytest.mark.p1
class Test_Add_Quote_With_Customdoor():

    def test_add_quote_with_customdoor_001(self,add_quote_with_customdoor):
        '''Verify  Add a Quote with a Custom door function'''
        expected = ('test_sample','test_sample')
        actual = add_quote_with_customdoor.verify_new_quote
        assert actual == expected,f"Expected:{expected},but got: {actual}"
