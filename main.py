# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

import json
# from utils.logger import Logger
# from apps.IRCM_database import IgwDb
# from apps.GMSC_telnet import TelnetGMSC
# from apps.IGW import IGW
# from workflow import config
from mme_list_commands import MmllistCommands


import sys

# base_location = config.base_location
#
# log = Logger.get_instance()
# log.log_start()

# db_class_instance = IgwDb()
# igw = IGW()
# telnet = TelnetGMSC()
mmlList_obj = MmllistCommands()



# p = PrepareMME2GScripts()
# q = PrepareMME3GScripts()
# r = TacDefine()
# p.read_workorder('',4,0)
# p.read_mme('VL_vUSN03')
# p.mme_commands()
mmlList_obj.planfile_format_get()



