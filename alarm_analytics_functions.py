
def rnc_log_read(result_file_location, result_file_name):
    file_path = f'{result_file_location}{result_file_name}'
    # print(file_path)


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
        prev_row = ''
        date_start = ''
        i = 0
        row = 0
        val = ''
        line = ''
        length = len(result_data)

        while row<length-1:
            if key1 in result_data[row]:
                parsing_flag = 1
            val2 = result_data[row][:4]
            # print(val)



            if parsing_flag == 1:
                next_line = result_data[row + 1]

                if val2.isdigit() == True:
                    date_start = 1

                if date_start !=1:
                    parsing_cmds.append(result_data[row])



                # parsing_cmds.append(line)
                if date_start == 1:
                    # print(result_data[row])
                    val = next_line[:4]
                    # print(val)


                    if val.isdigit() == False:
                        line = result_data[row]+ next_line
                        # print(line)
                        row = row+1
                        # break


                    parsing_cmds.append(line)

            # prev_row = result_data[row]

            # print(prev_row)
            # print(result_data[row])
            # print(next_line)
            # print("-----------")
            # print(row)
            row = row+1
        for i in parsing_cmds:
            print(i)

        # for row in result_data:
        #     if key1 in row:
        #         parsing_flag = 1
        #     val = row[:4]
        #     # print(val)
        #     if parsing_flag == 1:
        #         if val.isdigit() == True:
        #             date_start = 1
        #         if date_start == 1:
        #             val = row[:4]
        #             if val.isdigit() == False:
        #                 row = prev_row + row
        #         parsing_cmds.append(row)
        #     prev_row = row
        #     # next_line = next(row)
        #     # print(prev_row)
        #     # print(next_line)
        #
        # # print(parsing_cmds)
        #
        #

        # length = len(parsing_cmds)
        # print(length)
        # while i< length-1:
        #     # print(i)
        #     if  key1 in parsing_cmds[i]:
        #         # key1_pos = parsing_cmds[i].index(key1)
        #         # print(key1_pos)
        #         # key2_pos = parsing_cmds[i].index(key2)
        #         # print(key2_pos)
        #         # key3_pos = parsing_cmds[i].index(key3)
        #         # print(key3_pos)
        #         # key4_pos = parsing_cmds[i].index(key4)
        #         # print(key4_pos)
        #         # i += 2
        #         print("uu")
        #
        #
        #     #
        #     #
        #     value = parsing_cmds[i]
        #     # key1_value = value[0:len(key1)]
        #     # key2_value = value[key2_pos]
        #     # key3_value = value[key3_pos:key4_pos]
        #     # key4_value = value[key4_pos:]
        #     # a = key4_value.split('(')
        #     # print(a)
        #     # mo = a[0]
        #     # cause = a[1]
        #     # #
        #     # print(key1_value)
        #     # print(key2_value)
        #     # print(key3_value)
        #     # print(key4_value)
        #     # print(mo)
        #     # print(cause)
        #     # print("---------------------")
        #     i += 1



    except Exception as e:
        # self.log.log_info(msg=f'output file can not possible parse{e}')
        print(e)