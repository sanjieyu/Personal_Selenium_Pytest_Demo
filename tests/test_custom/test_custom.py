# Author:Yi Sun(Tim) 2023-11-02

'''Test  Add Custom Door Page - Pytest Version'''

import pytest
from pages.custom import Custom_Door

class Test_Custom_Door():

    @pytest.mark.p0
    def test_custom_door_001(self,custom_door):
        '''Verify the main elements in the page, should including correct title, Add button and Close button '''
        assert custom_door.check_customdoor_page == "test_sample"

    @pytest.mark.p1
    def test_custom_door_002(self,custom_door):
        '''Verify each element for install details'''
        expected = ('test_sample','test_sample','test_sample')
        actual = custom_door.check_install_details
        assert actual == expected,f"Expected:{expected},but got: {actual}"

    @pytest.mark.p1
    def test_custom_door_003(self, custom_door):
        '''Verify the Install Type dropdown list'''
        assert custom_door.check_install_type == ("Please Select\ntest_sample\ntest_sample\ntest_sample\n"
                                                  "test_sample\ntest_sample")

    @pytest.mark.p1
    def test_custom_door_004(self, custom_door):
        '''Verify the Design dropdown list'''
        assert ("Please Select\ntest_sample\ntest_sample\ntest_sample\n"
                                                  "test_sample\ntest_sample") in custom_door.check_design

    @pytest.mark.p1
    def test_custom_door_005(self, custom_door):
        '''Verify the Colour Category dropdown list'''
        assert custom_door.check_colour_category == ("Please Select\ntest_sample\ntest_sample\ntest_sample\n"
                                                  "test_sample\ntest_sample")

    @pytest.mark.p2
    def test_custom_door_006(self, custom_door):
        '''Verify the Door Colour dropdown list should be diabled if select "Custom" in Colour Category'''
        assert custom_door.check_door_colour_custom is False

    @pytest.mark.p2
    def test_custom_door_007(self, custom_door):
        '''Verify the Door Colour dropdown if select "OliColour" in Colour Category '''
        assert custom_door.check_door_colour_oilcolour == ("Please Select\ntest_sample\ntest_sample\ntest_sample\n"
                                                  "test_sample\ntest_sample")

    @pytest.mark.p2
    def test_custom_door_008(self, custom_door):
        '''Verify the Door Colour dropdown if select "Painted" in Colour Category '''
        assert custom_door.check_door_colour_painted == ("Please Select\ntest_sample\ntest_sample\ntest_sample\n"
                                                  "test_sample\ntest_sample")

    @pytest.mark.p2
    def test_custom_door_009(self, custom_door):
        '''Verify the Door Colour dropdown if select "Raw" in Colour Category '''
        assert custom_door.check_door_colour_raw == ("Please Select\ntest_sample\ntest_sample\ntest_sample\n"
                                                  "test_sample\ntest_sample")

    @pytest.mark.p2
    def test_custom_door_010(self, custom_door):
        '''Verify the Door Colour dropdown if select "SealedColour" in Colour Category '''
        assert custom_door.check_door_colour_sealedcolour == ("Please Select\ntest_sample\ntest_sample\ntest_sample\n"
                                                  "test_sample\ntest_sample")

    @pytest.mark.p2
    def test_custom_door_011(self, custom_door):
        '''Verify the Frame Colour dropdown list '''
        assert custom_door.check_frame_colour == ("Please Select\ntest_sample\ntest_sample\ntest_sample\n"
                                                  "test_sample\ntest_sample")

    @pytest.mark.p2
    def test_custom_door_012(self, custom_door):
        '''Verify the Timber Profile dropdown list'''
        assert custom_door.check_timber_profile == ("Please Select\ntest_sample\ntest_sample\ntest_sample\n"
                                                  "test_sample\ntest_sample")

    @pytest.mark.p2
    def test_custom_door_013(self, custom_door):
        '''Verify the Insert Material dropdown list'''
        assert custom_door.check_insert_material == ("Please Select\ntest_sample\ntest_sample\ntest_sample\n"
                                                  "test_sample\ntest_sample")

    @pytest.mark.p2
    def test_custom_door_014(self, custom_door):
        '''Verify the Insert Location dropdown list'''
        assert custom_door.check_insert_location == ("Please Select\ntest_sample\ntest_sample\ntest_sample\n"
                                                  "test_sample\ntest_sample")

    @pytest.mark.p1
    def test_custom_door_015(self, custom_door):
        '''Verify Insert Type dropdown list, the default value should be empty '''
        assert custom_door.check_insert_type_default == "test_sample"

    @pytest.mark.p2
    def test_custom_door_016(self, custom_door):
        '''Verify the Insert Type dropdown if select "ACPS Cat1" in Insert Material category'''
        assert custom_door.check_insert_type_cat1 == ("Please Select\ntest_sample\ntest_sample\ntest_sample\n"
                                                  "test_sample\ntest_sample")

    @pytest.mark.p2
    def test_custom_door_017(self, custom_door):
        '''Verify the Insert Type dropdown if select "ACPS Cat2" in Insert Material category'''
        assert custom_door.check_insert_type_cat2 == ("Please Select\ntest_sample\ntest_sample\ntest_sample\n"
                                                  "test_sample\ntest_sample")

    @pytest.mark.p2
    def test_custom_door_018(self, custom_door):
        '''Verify the Insert Type dropdown if select "Acrylic" in Insert Material category'''
        assert custom_door.check_insert_type_acrylic == ("Please Select\ntest_sample\ntest_sample\ntest_sample\n"
                                                  "test_sample\ntest_sample")

    @pytest.mark.p2
    def test_custom_door_019(self, custom_door):
        '''Verify the Insert Type dropdown if select "Aluminium" in Insert Material category'''
        assert custom_door.check_insert_type_aluminium == ("Please Select\ntest_sample\ntest_sample\ntest_sample\n"
                                                  "test_sample\ntest_sample")




