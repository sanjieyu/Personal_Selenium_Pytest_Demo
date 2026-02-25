# Author:Yi Sun(Tim) 2024-08-12

import pytest
from pages.standard import Standard_Door

@pytest.mark.p1
class Test_Standard_Door():

    def test_standard_door_001(self,standard_door):
        '''Verify the main elements in the page, should including correct title, Add button and Close button '''
        expected = ('test_sample', 'test_sample')
        actual  = standard_door.check_door_page
        assert actual == expected,f"Expected:{expected},but got: {actual}"

    def test_standard_door_002(self, standard_door):
        '''Verify each element for install details'''
        expected = ('test_sample', 'test_sample', 'test_sample', 'test_sample', 'test_sample', 'test_sample',
                    'test_sample', 'test_sample', 'test_sample')
        actual = standard_door.check_install_details
        assert actual == expected,f"Expected:{expected},but got: {actual}"

    def test_standard_door_003(self, standard_door):
        '''Verify the Install Type dropdown list'''
        assert ("Please Select\ntest_sample\ntest_sample\ntest_sample\n"
                                                  "test_sample\ntest_sample") in standard_door.check_install_type


    def test_standard_door_004(self, standard_door):
        '''Verify the Door Type dropdown list'''
        assert standard_door.check_door_type == ("Please Select\ntest_sample\ntest_sample\ntest_sample\n"
                                                  "test_sample\ntest_sample")

    def test_standard_door_005(self, standard_door):
        '''Verify the Colour Category dropdown list'''
        assert ("Please Select\ntest_sample\ntest_sample\ntest_sample\n"
                                                  "test_sample\ntest_sample") in standard_door.check_colour_category

    def test_standard_door_006(self, standard_door):
        '''Verify the Design dropdown for Panel Lift-Safe Door'''
        assert ("Please Select\ntest_sample\ntest_sample\ntest_sample\n"
                                                  "test_sample\ntest_sample") in standard_door.check_design_panel


    def test_standard_door_007(self, standard_door):
        '''Verify the Design dropdown for Insulated Sectional Door'''
        assert ("Please Select\ntest_sample\ntest_sample\ntest_sample\n"
                                                  "test_sample\ntest_sample") in standard_door.check_design_insulated

    def test_standard_door_010(self, standard_door):
        '''Verify the Door Colour dropdown for Custom Category, should be disabled'''
        assert standard_door.check_colour_custom is True

    def test_standard_door_019(self, standard_door):
        '''Verify each element for size details,'''
        expected = ('test_sample', 'test_sample', 'test_sample', 'test_sample', 'test_sample')
        actual = standard_door.check_size_details
        assert actual == expected,f"Expected:{expected},but got: {actual}"

    def test_standard_door_020(self, standard_door):
        '''Verify the default value for Opening Size LH, should be "0" '''
        assert standard_door.check_openinglh_default == "0"

    def test_standard_door_027(self, standard_door):
        '''Verify each element for Timer/Taper/AdditionalFab details'''
        expected = ('test_sample', 'test_sample', 'test_sample', 'test_sample', 'test_sample')
        actual = standard_door.check_timber_details
        assert actual == expected,f"Expected:{expected},but got: {actual}"

    def test_standard_door_028(self, standard_door):
        '''Verify each element for all checkboxes'''
        expected = ('test_sample', 'test_sample', 'test_sample', 'test_sample', 'test_sample')
        actual = standard_door.check_checkboxes_details
        assert actual == expected, f"Expected:{expected},but got: {actual}"
