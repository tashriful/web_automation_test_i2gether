import pandas as pd

def bmc_plan_format_check(excel_file_location):
    # fetching excel data
    excel_all_data = pd.read_excel(excel_file_location, header = 1)
    # extracting all columns header row name
    columns_headers_row = excel_all_data.columns.ravel()

    # extracting Start MSISDN', 'End MSISDN' only
    # data = pd.DataFrame(excel_all_data, columns=['Start MSISDN', 'End MSISDN'])
    target_header = ['MME','TAC', 'TAC H', 'TAC-LB' ,'TAC-HB', 'FQDN', 'HI' ,'Interface', 'Priority',
 'Weight', 'Description', 'LAC' ,'LAC H' ,'TAL ID' ,'TAI' ,'Description.1' ,'RNC',
 'LAI', 'MSC', 'VLR No', 'Perf Moc', 'Unnamed: 21', 'TAI Group Name',
 'Perf Moc.1', 'Unnamed: 24' ,'TAI Group Name.1', 'Begin TAI', 'End TAI',
 'MME.1', 'Unnamed: 29']

    # print(columns_headers_row)
    # print(target_header)

    if all(item in columns_headers_row for item in target_header):
        return True
    else:
        return False

def list_output_status_check(result_file_location, result_file_name):
    file_path = f'{result_file_location}{result_file_name}'
    print(file_path)


    try:
        result_data = open(f"{file_path}", "r")
        result_data = result_data.read().splitlines()

        prevLine = ""
        laivlr = ''
        for row in result_data:
            # print(row)
            if 'MML Command-----LST LAIVLR:' in row:
                laivlr = True

            if '---    END' in row:
                # print(len(prevLine))
                if prevLine != "No matching result is found" and len(prevLine) != 0:
                    if laivlr == True:
                        laivlr = False
                        continue
                    print("defined")
                    return False
                # else:
                #     print("undefined")


            prevLine = row
    except Exception as e:
        # self.log.log_info(msg=f'output file can not possible parse{e}')
        print(e)


def lst_output_status_check(result_file_location, result_file_name):
    file_path = f'{result_file_location}{result_file_name}'
    try:
        result_data = open(f"{file_path}", "r")
        result_data = result_data.read().splitlines()

        prevLine = ""
        laivlr = ''
        command = ''
        cmd_stat = {}
        for row in result_data:
            # print(row)
            if 'MML Command-----LST LAIVLR:' in row:
                laivlr = True
            if 'MML Command-----' in row:
                # print(row)
                command = row.split('-----')
                command = command[1]
                command = command.split(':')
                command = command[0]
                command = command.split(' ')
                command = command[1]
                print(command)
            if 'NE : NE' in row:
                ne = row.split('=')
                ne = ne[1]
                ne = ne.split(',')
                ne = ne[0]
                print(ne)

            if '---    END' in row:

                if prevLine != "No matching result is found":
                    # if laivlr == True:
                    #     laivlr = False
                    #     continue
                    print("defined")
                    cmd_stat[f'{command}-{ne}'] = 'Defined'

                    # return False
                else:
                    print("undefined")
                    cmd_stat[f'{command}-{ne}'] = 'Not Defined'

            prevLine = row
        print(cmd_stat)
    except Exception as e:
        print("false" + "e")

    #     read_file = open(f"{file_path}", "r")
    #     result_data = read_file.read().splitlines()
    #     print(len(result_data))
    #     l = len(result_data)
    #     indentifier1 = "---------------------"
    #     indentifier2 = "---    END"
    # except:
    #     print("An exception in Reading file File Path: " + file_path)
    # print("testing")
    # i = 0  # loop initializing
    # print(i)
    # print(l)
    # list = []
    # while (i + 2) < l:
    #     if result_data[i] == indentifier1:  # identifying preheader syntax
    #         print("first ")
    #         print(i)
    #         i = i + 1  # moving onto next index to find list by tab separator
    #         elements = result_data[i].strip().split("\t")  # finding header
    #         list.append(elements)
    #         print(elements, len(elements))
    #         i = i + 2  # skiping blank line after header
    #         while (i + 2) < l:
    #
    #             if result_data[i + 2] == indentifier2:  # identifying tab separated block
    #                 print("last")
    #                 print(i)
    #                 break
    #             elements = result_data[i].strip().split("\t")
    #             list.append(elements)
    #             print(elements, len(elements))
    #             i = i + 1
    #
    #         print(result_data[i])
    #     i = i + 1
    #     print(i)
    # return list


def consistency_status_check(result_file_location, result_file_name, write_status):
    file_path = f'{result_file_location}{result_file_name}'
    try:
        result_data = open(f"{file_path}", "r")
        result_data = result_data.read().splitlines()
        print(len(result_data))
        l = len(result_data)
        print(l)
        i = 0
        command = ''
        location = f'C:/Users/123/Downloads/Tac Define/'
        file_name = 'add_Command_report.txt'
        write_mode = 'a'

        try:
            # file_handle = open(f"{location}{file_name}", 'w')
            # file_handle.write(f'################################   List Of Unsuccessful ADD COMMAND  ############################\n\n\n')
            # file_handle.close()
            file_handle = open(f"{location}{file_name}", 'w')
            while i < l:
                if 'omo@' in result_data[i]:
                    # command = f'{result_data[i-1]}{result_data[i]}'
                    command = f'{result_data[i - 1]}{result_data[i]}'
                    # print(command)
                if result_data[i] == '---    END':
                    # print(result_data[i-2])
                    retcode_row  = result_data[i-2]
                    if 'RETCODE = 0' in retcode_row:
                        print("true")
                    else:
                        print("false")
                        command = f"""{command}\n"""
                        file_handle.write(command)

                i = i+1
            file_handle.close()

        except Exception as e:
            print(e)
    except Exception as e:
        print(e)


def mme_get(loc):
    data = pd.read_excel(loc, 'Sheet1')
    # print(data)
    i = 1
    mme_name = []
    try:
        previous_mme = ''
        while i < len(data):
            if data.iloc[i, 0] == '' or pd.isna(data.iloc[i, 0]) or data.iloc[i, 0] == "MME":
                i = i+1
                continue
            mme = data.iloc[i, 0]
            if previous_mme == mme:
                i = i+1
                continue
            mme_name.append(mme)
            i = i + 1
            previous_mme = mme
        return mme_name



    except IOError as e:
        # self.log.log_critical(msg=f'{e}')
        return False
