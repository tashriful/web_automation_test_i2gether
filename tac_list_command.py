result_file_location = f'C:/Users/123/Downloads/Tac Define/'
result_file_name = f'tac_20201031205046_itautobot_172.rst'


# def get_last_overall_allow(self, result_file_name):
file_path = f'{result_file_location}{result_file_name}'
try:
    result_data = open(f"{file_path}", "r")
    result_data = result_data.read().splitlines()


    prevLine = ""
    for row in result_data:
        print(row)
        if '---    END' in row:

            if prevLine  == "No matching result is found":
                tac_defined_status = False
                print("defined")
                break
            else:
                tac_defined_status = True
                print("undefined")

        prevLine = row
except Exception as e:

    print("false" + "e")
