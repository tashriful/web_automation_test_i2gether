from datetime import date

# from short_code_functions import short_code_lst
from short_code_functions import bmc_plan_format_check
from short_code_functions import plan_file_mail_body
from short_code_functions import vmsc_lst_mail_body
from short_code_functions import legecy_lst_mail_dict
from short_code_functions import vmsc_lst_mail_dict
from short_code_functions import legecy_add_mail_dict
from short_code_functions import vmsc_add_mail_dict
from short_code_functions import lst_mail_body
from short_code_functions import lst_callprichk_mail_body
from short_code_functions import vmsc_add_mail_body
from short_code_functions import prepare_mail_body
from short_code_functions import legecy_add_mail_body
from short_code_functions import add_mail_body
from short_code_functions import short_code_lst
from short_code_functions import prepare_add_mail_body
from short_code_functions import mail_header
from short_code_functions import vmsc_consistency_mail_dict

current_date = date.today()

wo = "WO0000000163009"
mail_header_data = {
    "subject": f'Subject: Short_Code_Define_WO({wo})_Rejection_Notification_Date({current_date}',
    "activity_name": "Short Code Define",
    "wo_num": f'{wo}'
}
loc = "E:/Robi RPA/Short Code Define/short_code2.xlsx"
plan_format_status, vmsc_fragment, legecy_fragment = bmc_plan_format_check(loc)
plan_mail_data = plan_file_mail_body(vmsc_fragment, legecy_fragment)

loc = f'E:/Robi RPA/Short Code Define/'
file = f'vmsc.rst'
file2 = f'legecyLst_main.rst'
file3 = f'addlog.txt'
file4 = f'vmscAdd.rst'
file5 = f'legecyAdd.rst'
code = '10654'
description = 'Ship Aichi MSL'
route_name = 'DG06_DG10'



# cnacld_vmsc_lst_status, callprichk_vmsc_lst_status = vmsc_lst_mail_dict(loc, file, code, route_name, description)
# print(cnacld_vmsc_lst_status)
# print(callprichk_vmsc_lst_status)
# exit(-6)
# cnacld_legecy_lst_status = legecy_lst_mail_dict(loc, file2, code, route_name, description)
# print(cnacld_legecy_lst_status)
# exit(-4)
# mail_header = mail_header(mail_header_data)
# cnacld_vmsc_add_status, callprichk_vmsc_add_status = vmsc_add_mail_dict(loc, file4)
# print(cnacld_vmsc_add_status)
# print(callprichk_vmsc_add_status)
# cnacld_legecy_add_status = legecy_add_mail_dict(loc, file5)
# print(cnacld_legecy_add_status)
# exit(-8)

cnacld_vmsc_consistency_status, callprichk_vmsc_consistency_status = vmsc_consistency_mail_dict(loc, file)
print(cnacld_vmsc_consistency_status)
print(callprichk_vmsc_consistency_status)
cnacld_legecy_consistency_status, callprichk_legecy_consistency_status = vmsc_consistency_mail_dict(loc, file2)
print(cnacld_legecy_consistency_status)
print(callprichk_legecy_consistency_status)
exit(-3)


# if cnacld_lst_status.get('Python') != None:
#     print("The key is present.\n")
#
# else:
#     print("The key does not exist in the dictionary.")

a = f'{cnacld_legecy_lst_status["DG06_MSOFT"] if "DG06_MSOFT" in cnacld_legecy_lst_status.keys() else "N/A"}'
print(a)
# exit(-66)
# vmsc_lst_status = vmsc_lst_mail_body(loc, file)
lst_mail_body = lst_mail_body(cnacld_vmsc_lst_status, cnacld_legecy_lst_status, callprichk_vmsc_lst_status, callprichk_legecy_lst_status, code)
print(lst_mail_body)
# lst_callprichk_mail_body = lst_callprichk_mail_body(callprichk_vmsc_lst_status, callprichk_legecy_lst_status)
# print(lst_callprichk_mail_body)
exit(-3)
# # print(lst_mail_body)
# exit(-99)
mail_body = prepare_mail_body(mail_header_data, "ok", "yes", plan_mail_data, lst_mail_body, "unsuccessful", "reject")
# print(mail_body)


vmsc_add_status = vmsc_add_mail_body(loc, file4)
legecy_add_status = legecy_add_mail_body(loc, file3)
# print(vmsc_add_status)
# print(legecy_add_status)
add_mail_body = add_mail_body(vmsc_add_status, legecy_add_status, code)
# print(add_mail_body)
add_mail_body = prepare_add_mail_body(mail_header_data, "ok", "yes", plan_mail_data, lst_mail_body, add_mail_body,
                                      "successful", "accept")
print(add_mail_body)

defined, undefined = short_code_lst()
print(defined)
print(undefined)
