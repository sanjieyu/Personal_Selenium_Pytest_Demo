# Author:Yi Sun(Tim) 2023-11-02

'''Test  Add Custom Door Page - Pytest Version'''

import pytest
from UIModule.custom_door import Custom_Door

class Test_Custom_Door():

    def test_custom_door_001(self,custom_door):
        '''Verify the main elements in the page, should including correct title, Add button and Close button '''
        assert custom_door.check_customdoor_page == "Custom Door Details"

    def test_custom_door_002(self,custom_door):
        '''Verify each element for install details'''
        expected = ('Install Type','Design','Colour Category','Door Colour','Frame Colour','Timber Profile',
                    'Insert Material','Insert Location','Insert Type','Insert Colour','Insert Other','Custom Colour')
        actual = custom_door.check_install_details
        assert actual == expected,f"Expected:{expected},but got: {actual}"

    def test_custom_door_003(self, custom_door):
        '''Verify the Install Type dropdown list'''
        assert custom_door.check_install_type == ("Please Select\nCommercial Cat 1\nCommercial Cat 2\nCommercial STD\n"
                                                  "Full Panel Replacement\nResidential")

    def test_custom_door_004(self, custom_door):
        '''Verify the Design dropdown list'''
        assert ("Ali Batten\nAli Louvre Panel\nAliwood\nAlumalite\nAlumicomp\nBar panel\nBarn Panel\nCarriage Panel\n"
                "Cedar Batten\nCedar Panel 135\nCedar Panel 86\nClassic Panel\nFrame Only STD\nFrame Only Welded\n"
                "Glasslite\nGrille Panel\nHerringbone Panel\nLouvre Panel\nPerfalite\nRaised Panel\nRecessed Panel\n"
                "Tranquilo Panel\nTwinlight\nVerti Panel") in custom_door.check_design

    def test_custom_door_005(self, custom_door):
        '''Verify the Colour Category dropdown list'''
        assert custom_door.check_colour_category == ("Please Select\nCustom\nOilColour\nPainted\nPowderCoatStandard\n"
                                                     "PowderCoatUpgrade\nPrimed\nRaw\nSealedColour")


    def test_custom_door_006(self, custom_door):
        '''Verify the Door Colour dropdown list should be diabled if select "Custom" in Colour Category'''
        assert custom_door.check_door_colour_custom is False

    def test_custom_door_007(self, custom_door):
        '''Verify the Door Colour dropdown if select "OliColour" in Colour Category '''
        assert custom_door.check_door_colour_oilcolour == "Please Select\nBlack Ash\nClear\nCustom\nSela Brown\nTBA"

    def test_custom_door_008(self, custom_door):
        '''Verify the Door Colour dropdown if select "Painted" in Colour Category '''
        assert custom_door.check_door_colour_painted == "Please Select\nCustom Colour"


    def test_custom_door_009(self, custom_door):
        '''Verify the Door Colour dropdown if select "Raw" in Colour Category '''
        assert custom_door.check_door_colour_raw == "Please Select\nTBA"


    def test_custom_door_010(self, custom_door):
        '''Verify the Door Colour dropdown if select "SealedColour" in Colour Category '''
        assert custom_door.check_door_colour_sealedcolour == "Please Select\nClear\nCustom\nDark oak\nEbony\nHemlock\n"
                                                              "Light oak\nRosewood\nTBA\nWalnut"

    def test_custom_door_011(self, custom_door):
        '''Verify the Frame Colour dropdown list '''
        assert custom_door.check_frame_colour == ("Please Select\nClear\nCustom\nDark oak\nEbony\nHemlock\nLight oak\n"
                                                  "Rosewood\nTBA\nWalnut\nMill Finish")

    def test_custom_door_012(self, custom_door):
        '''Verify the Timber Profile dropdown list'''
        assert custom_door.check_timber_profile == "Please Select\n135mm Shiplap\n135mm V-Join\n86mm Shiplap\n86mm V-Join"

    def test_custom_door_013(self, custom_door):
        '''Verify the Insert Material dropdown list'''
        assert custom_door.check_insert_material == ("Please Select\nACPS Upgrade - Cat 1\nACPS Upgrade - Cat 2\n"
                                                     "Acrylic\nAluminium\nExterier Ply\nGlass\nOther\nPolycarbonate\n"
                                                     "tandard ACPS\nSupplied By Client\nTBA")

    def test_custom_door_014(self, custom_door):
        '''Verify the Insert Location dropdown list'''
        assert custom_door.check_insert_location == "Please Select\nFace Fixed\nInserted into Frame\nTBA"

    def test_custom_door_015(self, custom_door):
        '''Verify Insert Type dropdown list, the default value should be empty '''
        assert custom_door.check_insert_type_default == "Please Select"

    def test_custom_door_016(self, custom_door):
        '''Verify the Insert Type dropdown if select "ACPS Cat1" in Insert Material category'''
        assert custom_door.check_insert_type_cat1 == "Please Select\nAlutile\nOther\nUltrabond\nVitrabond"

    def test_custom_door_017(self, custom_door):
        '''Verify the Insert Type dropdown if select "ACPS Cat2" in Insert Material category'''
        assert custom_door.check_insert_type_cat2 == "Please Select\nAlpolic\nAlucabond\nOther\nSymonite"

    def test_custom_door_018(self, custom_door):
        '''Verify the Insert Type dropdown if select "Acrylic" in Insert Material category'''
        assert custom_door.check_insert_type_acrylic == "Please Select\n3mm Acrylic\n4.5mm Acrylic\n6mm Acrylic"

    def test_custom_door_019(self, custom_door):
        '''Verify the Insert Type dropdown if select "Aluminium" in Insert Material category'''
        assert custom_door.check_insert_type_aluminium == ("Please Select\nCLOVERLEAF - 36%\nOther\n"
                                                           "P1012SQ - 10mm Square-70%\nP1925 - 19mm Round-51%\n"
                                                           "P1931SR - 19x3mm slots-41%\nP2031 - 2MM Round-41%\n"
                                                           "P2332HEX - 23mm Hexagon-44%\nP2563SR - 25x6.3mm slots-43%\n"
                                                           "P3247 - 3.2mm Round-41%\nP4763 - 4.7mm Round-51%\n"
                                                           "P4769 - 4.7mm Square-47%\nP5512SD - 5.5mm Square-19%\n"
                                                           "P7995 - 7.9mm Round-62%\nP9511HEX - 11.9mm Hexagon-64%")




