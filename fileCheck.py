base_location = r'E:/Number_series_define/'

result_file_location = f'C:/Users/123/Downloads/'
result_file_name = f'msc.rst'
mscList = ['DG05_MSOFTX', 'DG06_MSOFT', 'DG10_MSOFT', 'CG11_MSOFT', 'CG12_MSOFT']
spsList = ['SPS01_SPS', 'SPS02_SPS', 'VLSP01_SPS', 'ALSP01_SPS']


def msc_command():
    try:
        myLine = []
    result_data = open(f"{file_path}", "r")
    # result_data = result_data.read().splitlines()
    while True:
        # read line
        line = result_data.readline()
        # in python 2, print line
        # in python 3
        print(line)
        # check if line is not empty
        if not line:
            break
    result_data.close()

    # for row in result_data:
    #     myLine.append(row)
    # k = 0
    # length = len(myLine)
    #
    # for row in myLine:
    #     if "RETCODE = 0" in row:
    #         print("yes ret")
    #
    # k = k + 1
    # print(k)

def node_checker(row):
    row = row
    x = row.split(":")
    x = x[1].strip()
    for msc in mscList:
        if x in msc:
            status = "msc"
            return status
    for sps in spsList:
        if x in sps:
            status = "sps"
            return status

# def get_last_overall_allow(self, result_file_name):
file_path = f'{result_file_location}{result_file_name}'
try:
    result_data = open(f"{file_path}", "r")
    result_data = result_data.read().splitlines()

    for row in result_data:

        # check = all(item in columns_headers_row for item in target_header)
        if 'NE :' in row:
            node = node_checker(row)
        if "RETCODE = 0" in row:
            match = maching_checker(node,k)





except Exception as e:
    print(e)




