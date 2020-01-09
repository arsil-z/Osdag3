from design_type.connection.shear_connection import ShearConnection
from utils.common.component import *
from utils.common.component import Bolt, Plate, Weld
from Common import *
from utils.common.load import Load
import yaml
import os
import shutil
import logging

class CleatAngleConnectionInput(ShearConnection):

    def __init__(self, connectivity, supporting_member_section, supported_member_section, fu, fy, shear_load,
                 bolt_diameter, bolt_type, bolt_grade, cleat_angle_section):

        super(CleatAngleConnectionInput, self).__init__(connectivity, supporting_member_section,
                                                        supported_member_section, fu, fy, shear_load, bolt_diameter,
                                                        bolt_type, bolt_grade)
        self.cleat_angle = Angle(designation=cleat_angle_section, material=self.material)

    def input_values(self, existingvalues={}):

        options_list = []

        if KEY_CONN in existingvalues:
            existingvalue_key_conn = existingvalues[KEY_CONN]
        else:
            existingvalue_key_conn = ''

        if KEY_SUPTNGSEC in existingvalues:
           existingvalue_key_suptngsec = existingvalues[KEY_SUPTNGSEC]
        else:
            existingvalue_key_suptngsec = ''

        if KEY_SUPTDSEC in existingvalues:
            existingvalue_key_suptdsec = existingvalues[KEY_SUPTDSEC]
        else:
            existingvalue_key_suptdsec = ''

        if KEY_MATERIAL in existingvalues:
            existingvalue_key_mtrl = existingvalues[KEY_MATERIAL]
        else:
            existingvalue_key_mtrl = ''

        if KEY_SHEAR in existingvalues:
            existingvalue_key_versh = existingvalues[KEY_SHEAR]
        else:
            existingvalue_key_versh = ''


        if KEY_D in existingvalues:
            existingvalue_key_d = existingvalues[KEY_D]
        else:
            existingvalue_key_d = ''

        if KEY_TYP in existingvalues:
            existingvalue_key_typ = existingvalues[KEY_TYP]
        else:
            existingvalue_key_typ = ''

        if KEY_GRD in existingvalues:
            existingvalue_key_grd = existingvalues[KEY_GRD]
        else:
            existingvalue_key_grd = ''

        if KEY_CLEATHT in existingvalues:
            existingvalue_key_cleatht = existingvalues[KEY_CLEATHT]
        else:
            existingvalue_key_cleatht = ''

        if KEY_CLEATSEC in existingvalues:
            existingvalue_key_cleatsec = existingvalues[KEY_CLEATSEC]
        else:
            existingvalue_key_cleatsec = ''

        t16 = (KEY_MODULE, KEY_DISP_CLEAT_ANGLE, TYPE_MODULE, None, None)
        options_list.append(t16)

        t1 = (None, DISP_TITLE_CM, TYPE_TITLE, None, None)
        options_list.append(t1)

        t2 = (KEY_CONN, KEY_DISP_CONN, TYPE_COMBOBOX, existingvalue_key_conn, VALUES_CONN)
        options_list.append(t2)

        t3 = (KEY_IMAGE, None, TYPE_IMAGE, None, None)
        options_list.append(t3)

        t4 = (KEY_SUPTNGSEC, KEY_DISP_COLSEC, TYPE_COMBOBOX, existingvalue_key_suptngsec, VALUES_COLSEC)
        options_list.append(t4)

        t5 = (KEY_SUPTDSEC, KEY_DISP_BEAMSEC, TYPE_COMBOBOX, existingvalue_key_suptdsec, VALUES_BEAMSEC)
        options_list.append(t5)

        t6 = (KEY_MATERIAL, KEY_DISP_MATERIAL, TYPE_COMBOBOX, existingvalue_key_mtrl, VALUES_MATERIAL)
        options_list.append(t6)

        t7 = (None, DISP_TITLE_FSL, TYPE_TITLE, None, None)
        options_list.append(t7)

        t8 = (KEY_SHEAR, KEY_DISP_SHEAR, TYPE_TEXTBOX, existingvalue_key_versh, None)
        options_list.append(t8)

        t9 = (None, DISP_TITLE_BOLT, TYPE_TITLE, None, None)
        options_list.append(t9)

        t10 = (KEY_D, KEY_DISP_D, TYPE_COMBOBOX, existingvalue_key_d, VALUES_D)
        options_list.append(t10)

        t11 = (KEY_TYP, KEY_DISP_TYP, TYPE_COMBOBOX, existingvalue_key_typ, VALUES_TYP)
        options_list.append(t11)

        t12 = (KEY_GRD, KEY_DISP_GRD, TYPE_COMBOBOX, existingvalue_key_grd, VALUES_GRD)
        options_list.append(t12)

        t13 = (None, DISP_TITLE_CLEAT, TYPE_TITLE, None, None)
        options_list.append(t13)

        t14 = (KEY_CLEATHT, KEY_DISP_CLEATHT, TYPE_TEXTBOX, existingvalue_key_cleatht,None)
        options_list.append(t14)

        t15 = (KEY_CLEATSEC, KEY_DISP_CLEATSEC, TYPE_COMBOBOX, existingvalue_key_cleatsec, VALUES_CLEATSEC)
        options_list.append(t15)

        return options_list
