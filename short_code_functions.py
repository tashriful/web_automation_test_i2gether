import pandas as pd
def short_code_lst():
    result_file_location = f'C:/Users/123/Downloads/Robi RPA/Short Code Define/'
    result_file_name = f'defined.rst'

    # def get_last_overall_allow(self, result_file_name):
    file_path = f'{result_file_location}{result_file_name}'
    try:
        result_data = open(f"{file_path}", "r")
        result_data = result_data.read().splitlines()

        prevLine = ""
        for row in result_data:
            # print(row)
            if '---    END' in row:

                if prevLine != "No matching result is found":
                    tac_defined_status = False
                    print("defined")
                    break
                else:
                    tac_defined_status = True
                    print("undefined")

            prevLine = row
    except Exception as e:

        print("false" + "e")

def legecy_short_code_lst():
    result_file_location = f'C:/Users/123/Downloads/Robi RPA/Short Code Define/'
    result_file_name = f'legecy.rst'

    # def get_last_overall_allow(self, result_file_name):
    file_path = f'{result_file_location}{result_file_name}'
    try:
        result_data = open(f"{file_path}", "r")
        result_data = result_data.read().splitlines()

        prevLine = ""
        ne_name = ''
        for row in result_data:
            # print(row)
            if 'NE :' in row:
                ne_name = row
                ne_name = ne_name.split(' : ')
                ne_name = ne_name[1]
                print(ne_name)
            if '---    END' in row:

                if prevLine != "No matching result is found":
                    if ne_name == 'CGDR01_MSOFT':
                        print("atu")
                        continue
                    print("defined")
                    break
                else:
                    tac_defined_status = True
                    print("undefined")

            prevLine = row
    except Exception as e:

        print("false" + "e")

def bmc_plan_format_check(loc):
    # fetching excel data
    # encoding = 'ISO-8859-1'
    try:
        excel_all_data = pd.read_excel(loc, sheet_name='Short Code', header=1,  converters={'Code': str})
        # extracting all columns header row name
        columns_headers_row = excel_all_data.columns.ravel()
        data = pd.DataFrame(excel_all_data, columns=['Code', 'Description', 'Add'])
        # print(data)
        length = len(data)
        i = 2
        j = ''
        vmsc_first_index = 0
        # print(df['Code'])
        vmsc_fragment = ''
        while i < length:
            # a = df['Code'].iloc[i]
            # print(a)
            # i = i+1
            if data['Code'].isnull().iloc[i] or data['Code'].iloc[i] == '':
                # print(df.loc[i, 'Code'])
                vmsc_fragment = data.iloc[vmsc_first_index:i - 1]
                # print(i)
                j = i
            i = i + 1
        # print(vmsc_fragment)
        j = j + 3
        legecy_first_index = j
        legecy_fragment = ''
        while j < length:
            # print(df.loc[j, 'Code'])
            # print(j)
            if j == length - 1:
                # print(df.loc[j, 'Code'])
                legecy_fragment = data.iloc[legecy_first_index:j + 1]
                # print(f'atu{j}')
            j = j + 1

        # print(legecy_fragment)
        # virtual_frag = len(fragment)
        # l_f2 = len(fragment2)
        # k = 1
        # while k < l_f2:
        #     print(fragment.values[1][0])
        #     print(fragment2.values[1][1])
        #     k = k + 1
        target_header = ['Code', 'Description', 'Add']
        # print(columns_headers_row)
        # print(target_header)
        if all(item in columns_headers_row for item in target_header):
            return True, vmsc_fragment, legecy_fragment
        else:
            return False, vmsc_fragment, legecy_fragment
    except Exception as e:
        print("Plan format file  read not matched")

def plan_file_mail_body(vmsc_fragment, legecy_fragment):
    length = len(vmsc_fragment)
    i = 0
    plan_mail = ''
    colspan = ''
    while i < length:
        code = vmsc_fragment.values[i][0]
        # print(code)
        row = legecy_fragment[legecy_fragment['Code'] == code].index[0]
        # print(row)
        description = vmsc_fragment.values[i][1]
        # print(description)
        code_length = len(code)
        # print(code_length)
        vmsc_rtna = 'DG06_DG10'
        route_names = legecy_fragment.loc[row, 'Description']
        route_names = route_names.split(' // ')
        dg06_route = route_names[0]
        dg06_route = dg06_route.replace(" ", "")
        dg06_route = dg06_route.split(':')
        dg06_route = dg06_route[1]
        # print(dg06_route)
        dg10_route = route_names[1]
        dg10_route = dg10_route.replace(" ", "")
        dg10_route = dg10_route.split(':')
        dg10_route = dg10_route[1]
        colspan = length+1
        # print(dg10_route)
        plan_mail += f"""<tr>
<td width="86">
<p>{code}</p>
</td>
<td width="211">
<p>{description}</p>
</td>
<td width="187">
<p>{code_length}</p>
</td>
<td width="160">
<p>{vmsc_rtna}</p>
</td>
<td width="159">
<p>{dg06_route}</p>
</td>
<td width="204">
<p>{dg10_route}</p>
</td>
</tr>"""

        i = i +1
    plan_mail_header = f"""<tr>
<td rowspan="{colspan}" width="124">
<p><strong>Plan Data</strong></p>
</td>
<td width="92">
<p><strong>Short Code</strong></p>
</td>
<td width="230">
<p><strong>Description</strong></p>
</td>
<td width="188">
<p><strong>MINL/MAXL</strong></p>
</td>
<td width="176">
<p><strong>VMSC-RTANA</strong></p>
</td>
<td width="179">
<p><strong>DG06-RTANA</strong></p>
</td>
<td width="209">
<p><strong>DG10-RTANA</strong></p>
</td>
</tr>"""
    plan_mail_header += plan_mail
    return plan_mail_header

def vmsc_lst_mail_body(loc, file):
    file_path = f'{loc}{file}'
    vmsc_lst_status = {}
    try:
        result_data = open(f"{file_path}", "r")
        result_data = result_data.read().splitlines()

        prevLine = ""
        for row in result_data:
            # print(row)
            if 'MML Command-----' in row:
                cmd_name = row
                cmd_name = cmd_name.split('-----')
                cmd_name = cmd_name[1]
                cmd_name = cmd_name.split(':')
                cmd_name = cmd_name[0]
                # print(cmd_name)
            if 'NE :' in row:
                ne_name = row
                ne_name = ne_name.split(' : ')
                ne_name = ne_name[1]
                # print(ne_name)
            if '---    END' in row:

                if prevLine == "No matching result is found":
                    tac_defined_status = False
                    # print("not defined")
                    vmsc_lst_status[f'{ne_name} :{cmd_name}'] = 'Not Defined'

                else:
                    vmsc_lst_status[f'{ne_name} :{cmd_name}'] = 'Defined'
            prevLine = row
        # print(vmsc_lst_status)
        return vmsc_lst_status
    except Exception as e:

        print("false" + "e")

def legecy_lst_mail_body(loc, file):
    file_path = f'{loc}{file}'
    legecy_lst_status = {}
    try:
        result_data = open(f"{file_path}", "r")
        result_data = result_data.read().splitlines()

        prevLine = ""
        for row in result_data:
            # print(row)
            if 'MML Command-----' in row:
                cmd_name = row
                cmd_name = cmd_name.split('-----')
                cmd_name = cmd_name[1]
                cmd_name = cmd_name.split(':')
                cmd_name = cmd_name[0]
                # print(cmd_name)
            if 'NE :' in row:
                ne_name = row
                ne_name = ne_name.split(' : ')
                ne_name = ne_name[1]
                # print(ne_name)
            if '---    END' in row:

                if prevLine == "No matching result is found":
                    tac_defined_status = False
                    print("not defined")
                    legecy_lst_status[f'({ne_name}) :> {cmd_name}'] = 'Not Defined'

                else:
                    tac_defined_status = True
                    print("defined")
                    legecy_lst_status[f'({ne_name}) :> {cmd_name}'] = 'Defined'

            prevLine = row
        # print(legecy_lst_status)
        return legecy_lst_status
    except Exception as e:

        print("false" + "e")

def lst_mail_body(vmsc_lst_status, legecy_lst_status, short_code):

    df = pd.DataFrame(list(vmsc_lst_status.items()), columns=['command', 'status'])
    df2 = pd.DataFrame(list(legecy_lst_status.items()), columns=['command', 'status'])
    # print(df)
    # print(df2)
    length = len(df)
    i = 0
    val = ''
    while i < length:
        code = df.values[i][0]
        code2 = df.values[i][1]
        try:
            code3 = df2.values[i][0]
        except Exception as e:
            code3 = ''
        try:
            code4 = df2.values[i][1]
        except Exception as e:
            code4 = ''

        val += f"""<tr>
    <td width="92">
    <p>{short_code}</p>
    </td>
    <td width="230">
    <p>{code}</p>
    </td>
    <td width="188">
    <p>{code2}</p>
    </td>
    <td width="188">
    <p>{code3}</p>
    </td>
    <td width="188">
    <p>{code4}</p>
    </td>
    </tr>"""

        # print(f'{code} {code2} {code3} {code4}')
        i = i + 1
    rowspan = length+1

    lst_mail_header = f"""<tr>
<td rowspan="{rowspan}" width="124">
<p><strong>Plan Verification</strong></p>
</td>
<td width="92">
<p><strong>Short Code</strong></p>
</td>
<td width="230">
<p><strong>VMSC-Commands</strong></p>
</td>
<td width="188">
<p><strong>Status</strong></p>
</td>
<td width="176">
<p><strong>GMSC Commands</strong></p>
</td>
<td width="179">
<p><strong>Status</stron></p>
</td>
</tr>"""

    lst_mail_header += val
    # print(val)
    return lst_mail_header

def vmsc_add_mail_body(loc, file):
    file_path = f'{loc}{file}'
    vmsc_add_status = {}
    try:
        result_data = open(f"{file_path}", "r")
        result_data = result_data.read().splitlines()
        ne_name = ''
        cmd_name = ''
        prevLine = ""
        retcode_status = ''
        for row in result_data:
            # print(row)
            if 'ADD ' in row:
                if '%%/*' in row:
                    continue
                cmd_name = row
                cmd_name = cmd_name.split(':')
                cmd_name = cmd_name[0]
                print(cmd_name)
                # print(cmd_name)

            if '+++' in row:
                ne_name = prevLine
                print(ne_name)

            if 'RETCODE' in row:
                retcode_status = row
                print(retcode_status)
                vmsc_add_status[f'{ne_name} :{cmd_name}'] = retcode_status
            prevLine = row

        return vmsc_add_status
    except Exception as e:

        print("false" + "e")



def prepare_mail_body(mail_header_data, plan_format_status, ne_assebility, plan_mail_data, lst_mail_data, lst_status, wo_status):

    mail_header = f"""<table width="1200" border=1px solid black>
    <tbody>
    <tr>
    <td colspan="7" width="1200">
    <p><strong>Subject: {mail_header_data['subject']}</strong></p>
    </td>
    </tr>
    <tr>
    <td width="124">
    <p><strong>Activity Name</strong></p>
    </td>
    <td colspan="6" width="1076">
    <p>{mail_header_data["activity_name"]}</p>
    </td>
    </tr>
    <tr>
    <td width="124">
    <p><strong>WO Number</strong></p>
    </td>
    <td colspan="6" width="1076">
    <p>{mail_header_data["wo_num"]}</p>
    </td>
    </tr>
    <tr>
    <td width="124">
    <p><strong>Plan Format</strong></p>
    </td>
    <td colspan="6" width="1076">
    <p>{plan_format_status}</p>
    </td>
    </tr>
    <tr>
    <td width="124">
    <p><strong>Accessibility to NE</strong></p>
    </td>
    <td colspan="6" width="1076">
    <p>{ne_assebility}</p>
    </td>
    </tr>"""
    mail_header += plan_mail_data
    mail_header += lst_mail_data
    mail_footer = f"""<tr>
    <td width="124">
    <p><strong>Summary</strong></p>
    </td>
    <td colspan="6" width="1076">
    <p>Plan Verification: {lst_status}</p>
    </td>
    </tr>
    <tr>
    <td width="124">
    <p><strong>WO Status</strong></p>
    </td>
    <td colspan="6" width="1076">
    <p>{wo_status}</p>
    </td>
    </tr>
    </tbody>
    </table>"""

    mail_header += mail_footer

    return mail_header






    