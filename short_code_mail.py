from datetime import date

# from short_code_functions import short_code_lst
from short_code_functions import bmc_plan_format_check
from short_code_functions import plan_file_mail_body
from  short_code_functions import vmsc_lst_mail_body
from short_code_functions import legecy_lst_mail_body
from short_code_functions import lst_mail_body
from short_code_functions import vmsc_add_mail_body
from short_code_functions import prepare_mail_body

current_date = date.today()



wo = "WO0000000163009"
mail_header_data ={
    "subject" : f'Subject: Short_Code_Define_WO({wo})_Rejection_Notification_Date({current_date}',
    "activity_name": "Short Code Define",
    "wo_num": f'{wo}'
}
loc = "C:/Users/123/Downloads/Robi RPA/Short Code Define/short_code2.xlsx"
plan_format_status, vmsc_fragment, legecy_fragment = bmc_plan_format_check(loc)
plan_mail_data = plan_file_mail_body(vmsc_fragment, legecy_fragment)


loc = f'C:/Users/123/Downloads/Robi RPA/Short Code Define/'
file = f'vmsc.rst'
file2 = f'legecy_lst.rst'
file3 = f'addlog.txt'
code = '10651'
legecy_lst_status = legecy_lst_mail_body(loc, file2)
# print(legecy_lst_status)
vmsc_lst_status = vmsc_lst_mail_body(loc, file)
lst_mail_body = lst_mail_body(vmsc_lst_status, legecy_lst_status, code)
# # print(lst_mail_body)
# exit(-99)
mail_body = prepare_mail_body(mail_header_data, "ok", "yes", plan_mail_data, lst_mail_body, "unsuccessful", "reject")
print(mail_body)
vmsc_add_status = vmsc_add_mail_body(loc, file3 )
# print(vmsc_add_status)
