import xlrd
import pandas as pd


def plan_file_format():
    loc = ("C:/Users/123/Downloads/Tac Define/tac2.xlsx")
    data = pd.read_excel(loc, 'Sheet1')
    i = 1
    j = 0
    output = []
    # print(self.data.columns)
    g = data.columns.get_loc("ADD DNSN for S11")
    # print(g)
    while i < len(data) - 1:
        if data.iloc[i, g] == '' or pd.isna(data.iloc[i, g]):
            break
        fqdn = data.iloc[i, g + 4]
        hsindex = data.iloc[i, g + 5]
        mme = data.iloc[i, 0]

        result = f"""LST DNSN:FQDN="{fqdn}",HSINDEX={hsindex},ENTITY=SGW,INTYPE=S11;"""
        output.append(result)
        print(result)
        i += 1
    return output








def plan_file():

    # Give the location of the file
    loc = ("C:/Users/123/Downloads/Tac Define/tac2_change_format.xlsx")

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)


    # Extracting number of rows
    print(sheet.nrows)

    my_dict = {}
    for i in range(sheet.nrows):
        for j in range(sheet.ncols):
            if sheet.cell_value(i, j) == 'ADD DNSN for S11':
                k = 0
                for k in range(sheet.ncols):
                    if sheet.cell_value(i + 1, k) == "MME":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['mme'] = True


                    if sheet.cell_value(i + 1, k) == "TAC H":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['tac_h'] = True


                    if sheet.cell_value(i + 1, k) == "FQDN":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['fqdn'] = True
                    else:
                        my_dict['fqdn'] = False

                    if sheet.cell_value(i + 1, k) == "HI":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['hi'] = True
                    else:
                        my_dict['hi'] = False

                    if sheet.cell_value(i + 1, k) == "Interface":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['interface'] = True
                    else:
                        my_dict['interface'] = False

                    if sheet.cell_value(i + 1, k) == "Priority":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['priority'] = True
                    else:
                        my_dict['priority'] = False

                    if sheet.cell_value(i + 1, k) == "Weight":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['weight'] = True
                    else:
                        my_dict['weight'] = False

                    if sheet.cell_value(i + 1, k) == "Description":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['description'] = True
                    else:
                        my_dict['description'] = False

                    if sheet.cell_value(i + 1, k) == "TAL ID":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['tal_id'] = True
                    else:
                        my_dict['tal_id'] = False

                    if sheet.cell_value(i + 1, k) == "TAI":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['tai'] = True
                    else:
                        my_dict['tai'] = False

                    if sheet.cell_value(i + 1, k) == "Description":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['description2'] = True
                    else:
                        my_dict['description2'] = False

                    if sheet.cell_value(i + 1, k) == "LAI":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['lai'] = True
                    else:
                        my_dict['lai'] = False

                    if sheet.cell_value(i + 1, k) == "VLR No":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['vl_rno'] = True
                    else:
                        my_dict['vlr_no'] = False

                    if sheet.cell_value(i + 1, k) == "TAI Group Name":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['tai_group_name'] = True
                    else:
                        my_dict['tai_group_name'] = False

                    if sheet.cell_value(i + 1, k) == "Begin TAI":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['begin_tai'] = True
                    else:
                        my_dict['begin_tai'] = False

                    if sheet.cell_value(i + 1, k) == "MME":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['performance_mme'] = True
                    else:
                        my_dict['performance_mme'] = False

                    if sheet.cell_value(i + 1, k) == "End TAI":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['end_tai'] = True
                            break
                    else:
                        my_dict['end_tai'] = False

            if sheet.cell_value(i, j) == 'ADD DNSN for S10 & Gn':
                for k in range(sheet.ncols):
                    if sheet.cell_value(i + 1, k) == "MME":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['s10_mme'] = True
                    else:
                        my_dict['s10_mme'] = False

                    if sheet.cell_value(i + 1, k) == "FQDN":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['s10_fqdn'] = True
                    else:
                        my_dict['s10_fqdn'] = False

                    if sheet.cell_value(i + 1, k) == "HI":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['s10_hi'] = True
                    else:
                        my_dict['s10_hi'] = False

                    if sheet.cell_value(i + 1, k) == "Interface":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['s10_interface'] = True
                    else:
                        my_dict['s10_interface'] = False

                    if sheet.cell_value(i + 1, k) == "Priority":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['s10_priority'] = True
                    else:
                        my_dict['s10_priority'] = False

                    if sheet.cell_value(i + 1, k) == "Weight":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['s10_weight'] = True
                    else:
                        my_dict['s10_weight'] = False

                    if sheet.cell_value(i + 1, k) == "Description":
                        if sheet.cell_value(i + 1, k) != '':
                            my_dict['s10_description'] = True
                            break
                    else:
                        my_dict['s10_description'] = False
    return my_dict
    # my_dict.clear()
    # print(my_dict)

def prepare_mailbody(planFile_data, header_data ):
    mail_header = f"""<table width="1077" border="1">
    <tbody>
        <tr>
            <td>Activity Name</td>
            <td colspan="10">
                <center>
                    {header_data['activity_name']}
                </center>
            </td>
        </tr>
        <tr>
            <td>WO Number</td>
            <td colspan="10">
                <center>{header_data['wo_num']}</center>
            </td>
        </tr>
        <tr>
            <td>WO Source</td>
            <td colspan="10">
                <center>{header_data['wo_source']}</center>
            </td>
        </tr>
        <tr>
            <td>Date</td>
            <td colspan="10">
                <center>{header_data['date']}</center>
            </td>
        </tr>
        <tr>
            <td>Plan Format</td>
            <td colspan="10">
                <center>OK/Not OK</center>
            </td>
        </tr>"""
    mail_body = f"""<tr>
            <td rowspan="13">Plan Data</td>
            <td colspan="5">S11 Interface: MME : Value given/Value not given</td>
            <td colspan="5">S10 &amp; Gn Interface: MME : Value given/Value not given</td>
        </tr>
        <tr>
            <td colspan="5">S11 Interface: TAC H : Value given/Value not given</td>
            <td colspan="5">S10 &amp; Gn Interface: FQDN : Value given/Value not given</td>
        </tr>
        <tr>
            <td colspan="5">S11 Interface: FQDN : Value given/Value not given</td>
            <td colspan="5">S10 &amp; Gn Interface: HI : Value given/Value not given</td>
        </tr>
        <tr>
            <td colspan="5">S11 Interface: HI : Value given/Value not given</td>
            <td colspan="5">S10 &amp; Gn Interface: Interface : Value given/Value not given</td>
        </tr>
        <tr>
            <td colspan="5">S11 Interface: Interface : Value given/Value not given</td>
            <td colspan="5">S10 &amp; Gn Interface: Priority : Value given/Value not given</td>
        </tr>
        <tr>
            <td colspan="5">S11 Interface: Priority : Value given/Value not given</td>
            <td colspan="5">S10 &amp; Gn Interface: Weight : Value given/Value not given</td>
        </tr>
        <tr>
            <td colspan="5">S11 Interface: Weight : Value given/Value not given</td>
            <td colspan="5">S10 &amp; Gn Interface: Description : Value given/Value not given</td>
        </tr>
        <tr>
            <td colspan="5">S11 Interface: Description : Value given/Value not given</td>
            <td colspan="5">ADD Perfobj: TAI Group Name : Value given/Value not given</td>
        </tr>
        <tr>
            <td colspan="5">S11 Interface: TAL ID : Value given/Value not given</td>
            <td colspan="5">ADD Perfobjrule: Begin TAI : Value given/Value not given</td>
        </tr>
        <tr>
            <td colspan="5">S11 Interface: TAI : Value given/Value not given</td>
            <td colspan="5">ADD Perfobjrule: End TAI : Value given/Value not given</td>
        </tr>
        <tr>
            <td colspan="5">S11 Interface: Description : Value given/Value not given</td>
            <td colspan="5">ADD Perfobjrule: MME : Value given/Value not given</td>
        </tr>
        <tr>
            <td colspan="5">S11 Interface: LAI : Value given/Value not given</td>
            <td colspan="5">&nbsp;</td>
        </tr>
        <tr>
            <td colspan="5">S11 Interface: VLR No : Value given/Value not given</td>
            <td colspan="5">&nbsp;</td>
        </tr>
        """
    mail_header += mail_body
    mail_last_part = f"""<td><b>WO Status</b></td>
                    <td colspan="12">
                        <center>Reject</center>
                    </td>
                </tr>
            </tbody>
            </table>
    """
    mail_header += mail_last_part
    mail_body = mail_header
    return mail_body
