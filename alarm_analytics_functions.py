
def rnc_log_read(result_file_location, result_file_name):
    file_path = f'{result_file_location}{result_file_name}'
    print(file_path)


    try:
        result_data = open(f"{file_path}", "r")
        result_data = result_data.read().splitlines()
        key1 = 'Date & Time (Local)'
        key2 = 'S'
        key3 = 'Specific Problem'
        key4 = 'MO (Cause/AdditionalInfo)'
        parsing_flag = ''
        parsing_cmds = []
        key1_pos = ''
        key2_pos = ''
        key3_pos = ''
        key4_pos = ''
        next_line = ''
        i = 0
        length = len(result_data)
        for row in range(length):
            if key1 in result_data[row]:
                parsing_flag = True
            if parsing_flag == True:
                if key4_pos in row:

                # if next_line[0].isdigit() == False:
                #     print("atu")

                parsing_cmds.append(row)
            # next_line = result_data[row+1]
            print(result_data[row])
            print(row)
            # print(next_line)



        # length = len(parsing_cmds)
        # print(length)
        # while i< length-1:
        #     # print(i)
        #     if  key1 in parsing_cmds[i]:
        #         key1_pos = parsing_cmds[i].index(key1)
        #         # print(key1_pos)
        #         key2_pos = parsing_cmds[i].index(key2)
        #         # print(key2_pos)
        #         key3_pos = parsing_cmds[i].index(key3)
        #         # print(key3_pos)
        #         key4_pos = parsing_cmds[i].index(key4)
        #         # print(key4_pos)
        #         i += 2
        #
        #
        #
        #
        #     value = parsing_cmds[i]
        #     key1_value = value[key1_pos:len(key1)]
        #     key2_value = value[key2_pos]
        #     key3_value = value[key3_pos:key4_pos]
        #     # key4_value = value[key4_pos:len(key4)]
        #     # if parsing_cmds[i].endswith(')') == True:
        #     print(key1_value)
        #     print(key2_value)
        #
        #     print(key3_value)
        #     # print(key4_value)
        #     print("---------------------")
        #     i += 1



    except Exception as e:
        # self.log.log_info(msg=f'output file can not possible parse{e}')
        print(e)