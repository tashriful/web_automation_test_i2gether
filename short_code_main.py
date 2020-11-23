from short_code_functions import short_code_lst
from short_code_functions import bmc_plan_format_check
from short_code_functions import plan_file_mail_body
from  short_code_functions import vmsc_lst_mail_body
from short_code_functions import legecy_lst_mail_body
from short_code_functions import lst_mail_body
from short_code_functions import vmsc_add_mail_body
a = 'ytee'
b = 'jdhdhd'

at = {}
at[a] = 'yyy'
# print(at)
import pandas as pd
import xlrd

# short_code_lst()
# exit()
# import os
# os.rename(r'C:\Users\123\Downloads\Robi RPA\Short Code Define\defined.rst',r'C:\Users\123\Downloads\Robi RPA\Short Code Define\defined.txt')
# exit(-63)
# legecy_short_code_lst()
# exit(-44)
loc = "C:/Users/123/Downloads/Robi RPA/Short Code Define/short_code2.xlsx"
plan_format_status, vmsc_fragment, legecy_fragment = bmc_plan_format_check(loc)
print(plan_format_status)
mail_header = f"""<table width="1200" border=1px solid black>
<tbody>
<tr>
<td colspan="7" width="1200">
<p><strong>Subject: Short_Code_Define_WO(XXX)_Rejection_Notification_Date(YYY)</strong></p>
</td>
</tr>
<tr>
<td width="124">
<p><strong>Activity Name</strong></p>
</td>
<td colspan="6" width="1076">
<p>Short Code Define</p>
</td>
</tr>
<tr>
<td width="124">
<p><strong>WO Number</strong></p>
</td>
<td colspan="6" width="1076">
<p>XXX</p>
</td>
</tr>
<tr>
<td width="124">
<p><strong>Plan Format</strong></p>
</td>
<td colspan="6" width="1076">
<p>Ok/Not Ok</p>
</td>
</tr>
<tr>
<td width="124">
<p><strong>Accessibility to NE</strong></p>
</td>
<td colspan="6" width="1076">
<p>Yes/No</p>
</td>
</tr>"""
plan_mail = plan_file_mail_body(vmsc_fragment, legecy_fragment)
plan_footer = f"""<tr>
<td width="124">
<p><strong>Summary</strong></p>
</td>
<td colspan="6" width="1076">
<p>Plan Verification: Unsuccessful</p>
</td>
</tr>
<tr>
<td width="124">
<p><strong>WO Status</strong></p>
</td>
<td colspan="6" width="1076">
<p>Reject</p>
</td>
</tr>
<tr>
<td width="124">
<p><strong>Attachment</strong></p>
</td>
<td colspan="6" width="1076">
<p>Plan, LST Script, LOG</p>
</td>
</tr>
</tbody>
</table>"""
mail_header += plan_mail
mail_header += plan_footer
# print(mail_header)
# print(plan_mail)
# mail += plan_mail
# print(mail)
# exit(-33)

loc = f'C:/Users/123/Downloads/Robi RPA/Short Code Define/'
file = f'vmsc.rst'
file2 = f'legecy_lst.rst'
file3 = f'addlog.txt'
legecy_lst_status = legecy_lst_mail_body(loc, file2)
# print(legecy_lst_status)
vmsc_lst_status = vmsc_lst_mail_body(loc, file)
lst_mail_body = lst_mail_body(vmsc_lst_status, legecy_lst_status)
# print(lst_mail_body)

prepare_mail_body()


vmsc_add_status = vmsc_add_mail_body(loc, file3 )
print(vmsc_add_status)





exit(-8)














df = pd.read_excel (loc, sheet_name='Short Code', header = 1)
# print (df)
l = len(df)
# print(l)
code = df.loc[0, 'Code']
i = 2
f_first_index = 0
# print(df['Code'])
fragment = ''
while i < l:
    # a = df['Code'].iloc[i]
    # print(a)
    # i = i+1
    if df['Code'].isnull().iloc[i] or df['Code'].iloc[i] == '' :
        # print(df.loc[i, 'Code'])
        fragment = df.iloc[f_first_index:i - 1]
        # print(i)
        j = i
    i = i + 1
# print(fragment)
j = j+3
j_first_index = j
fragment2 = ''
while j< l:
    # print(df.loc[j, 'Code'])
    # print(j)
    if j == l-1:
        # print(df.loc[j, 'Code'])
        fragment2 = df.iloc[j_first_index:j+1]
        # print(f'atu{j}')
    j = j+1

# print(fragment2)
l_f1 = len(fragment)
l_f2 = len(fragment2)
k = 0
while k < l_f2:
    code = fragment.values[k][0]
    print(code)

    row = fragment2[fragment2['Code'] == code].index[0]
    print(row)
    legecy_code = fragment2.loc[row, 'Code']
    print(legecy_code)
    route = fragment2.loc[row, 'Description']
    print(route)
    break
    # i, c = pd.np.where(fragment2 == code)
    # print(f'{i}{c}')
    # print(fragment2.values[0])
    # print(rt, " on plan file Row ",row )
    # rt_flag = True
#
#
    k = k+1

