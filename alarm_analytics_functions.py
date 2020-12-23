import xlwt
import pandas as pd
import openpyxl
from xlwt import Workbook

def rnc_log_read(result_file_location, result_file_name):
    file_path = f'{result_file_location}{result_file_name}'
    df = pd.DataFrame(columns=['Network Element', 'Alarming Object', 'Severity', 'Event Time', 'Insert Time',
                               'Specific Problem', 'Probable Cause', 'Event Type'])
    df.to_csv(f'E:/Robi RPA/Alarm Analytics/roc_pending_and_in_progress_list.csv')
    # print(file_path)

    try:
        result_data = open(f"{file_path}", "r")
        result_data = result_data.read().splitlines()
        key1 = 'Date & Time (Local)'
        key2 = 'S'
        key3 = 'Specific Problem'
        key4 = 'MO (Cause/AdditionalInfo)'
        key5 = '> alt'
        parsing_flag = ''
        parsing_cmds = []
        key1_pos = ''
        key2_pos = ''
        key3_pos = ''
        key4_pos = ''
        ne = ''
        mo_list = []

        i = 0
        row = 0

        length = len(result_data)

        while row < length-1:
            if key5 in result_data[row]:
                ne = result_data[row]
                ne = ne.split('>')[0]
                print(ne)

            if key1 in result_data[row]:
                parsing_flag = 1

            if parsing_flag == 1:
                line = result_data[row]
                parsing_cmds.append(line)
            row = row+1
        print(parsing_cmds)

        length = len(parsing_cmds)
        print(length)
        while i < length-1:

            if  key1 in parsing_cmds[i]:
                key1_pos = parsing_cmds[i].index(key1)
                key2_pos = parsing_cmds[i].index(key2)
                key3_pos = parsing_cmds[i].index(key3)
                key4_pos = parsing_cmds[i].index(key4)
                i += 2

            print(i)
            value = parsing_cmds[i]
            event_time = value[key1_pos:len(key1)]
            insert_time = event_time
            alarm_state = value[key2_pos]
            sp = value[key3_pos:key4_pos]
            key4_value = value[key4_pos:]
            a = key4_value.split('(')
            mo = a[0]
            mo_list.append(sp)
            cause = a[1]

            print(event_time)
            print(alarm_state)
            print(sp)
            print(mo)
            print(cause)
            print("---------------------")

            df = df.append({'Network Element': f'{ne}', 'Alarming Object': f'{mo}', 'Severity': f'{alarm_state}',
                            'Event Time': f'{event_time}', 'Insert Time': f'{insert_time}',
                               'Specific Problem': f'{sp}', 'Probable Cause': {cause}, 'Event Type' :'hhh'},
                   ignore_index=True)


            i += 1

        # df.to_excel('E:/Robi RPA/Alarm Analytics/pandas_to_excel.xlsx', sheet_name='new_sheet_name', index=False)
        repeated = []
        record_type = []
        print(df)
        print(mo_list)
        length = len(mo_list)
        print(length)
        count = ''
        i = 0
        for d in mo_list:

            count = 0
            k = 0
            while k< length:
                if i == k:
                    k +=1
                    continue
                if d == mo_list[k]:
                    count += 1
                k += 1
            i += 1
            repeated.append(count)
            if count == 0:
                record_type.append("Alarm")
            else:
                record_type.append("Repeated Alarm")


        # print(de)
        # print(bb)
        df['Repeated'] = repeated
        df['Record Type'] = record_type
        df['Record Type'] = record_type
        df.to_excel('E:/Robi RPA/Alarm Analytics/pandas_to_excel.xlsx', sheet_name='new_sheet_name', index=False)

        # for team in mo_list:
        #     # if we have not seen team before, create k/v pairing
        #     # setting value to 0, if team already in dict this does nothing
        #     d.setdefault(team, 0)
        #     # increase the count for the team
        #     d[team] += 1
        # for team, count in d.items():
        #     print("{} {}".format(team, count))

        # for team in [ele for ind, ele in enumerate(mo_list, 1) if ele not in mo_list[ind:]]:
        #     count = 0
        #     for ele in mo_list:
        #         if team == ele:
        #             count += 1
        #
        #     print("{} {}".format(team, count))



    except Exception as e:
        # self.log.log_info(msg=f'output file can not possible parse{e}')
        print(e)