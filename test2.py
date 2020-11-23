base_location = r'E:/Number_series_define/'

result_file_location = f'C:/Users/123/Downloads/New folder/'
result_file_name = f'msc.rst'
mscList = ['DG05_MSOFTX', 'DG06_MSOFT', 'DG10_MSOFT', 'CG11_MSOFT', 'CG12_MSOFT']
spsList = ['SPS01_SPS', 'SPS02_SPS', 'VLSP01_SPS', 'ALSP01_SPS']
msc_flag = []
sps_flag = []
config_status = ''
matching_result = ''
cutted_row = []
status= []
abc = []


def aa(row):
    atu = row
    print(cutted_row)
    status.clear()
    for row in atu:

        if "GT name  =  VLHS01_MSISDN_" in row:
            status.append(True)
        if "GT address information" in row:
            status.append(True)
        if "Load share DSP group name  =  SPS01_SPS02_LDSH" in row:
            status.append(True)
    print(status)
    return status


file_path = f'{result_file_location}{result_file_name}'
try:
    read_file = open(f"{file_path}", "r")
    result_data = read_file.read().splitlines()
    for row in result_data:
        cutted_row.append(row)
        if '---    END' == row:
            abc.append(aa(cutted_row))
            # print(abc)
            cutted_row.clear()



except Exception as e:
    print(e)