base_location = r'E:/Number_series_define/'

result_file_location = f'C:/Users/123/Downloads/New folder/'
result_file_name = f'msc.rst'
mscList = ['DG05_MSOFTX', 'DG06_MSOFT', 'DG10_MSOFT', 'CG11_MSOFT', 'CG12_MSOFT']
spsList = ['SPS01_SPS', 'SPS02_SPS', 'VLSP01_SPS', 'ALSP01_SPS']
msc_flag = []
sps_flag = []

matching_result = ''



def msc_command(row,k):

    row = row
    k = k
    print(myLine[k+2])
    if "No matching result is found" in myLine[k+2]:
        return "not match"
    else:
        return "match"








def msc_configuration_check(row):
    row = row


    if "GT name  =  VLHS01_MSISDN_" in row:

        return "true"
    if "GT address information" in row:

        return "true"
    if "Load share DSP group name  =  SPS01_SPS02_LDSH" in row:

        return "true"
    else:
        return "false"







def sps_configuration_check(row,k):
    row = row
    k = k

    if "GT name  =  E.164_8801848535" in row:
        sps_flag.append("true")
    if "SCCP addressing policy name  =  VLHSS01_ALHSS01" in row:
        sps_flag.append("true")
    if "Address message  =  8801848535" in row:
        sps_flag.append("true")
    k = k+1
    return sps_flag,k






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
    myLine=[]
    node = ''
    for row in result_data:
        myLine.append(row)

    k = 0
    for row in myLine:
        if 'NE :' in row:
            node = node_checker(row)
            # print(node)
        if "RETCODE = 0" in row:
            matching_result = msc_command(row,k)
            row = myLine[k+2]
            print(matching_result)
            print(node)
    # while "---    END" not in row:
        if matching_result != "not match":
            row = myLine[k]
            if node == "msc":
                value = msc_configuration_check(row)
                if "---    END" not in row:
                    if value == "true":
                        msc_flag.append(value)
                    print(msc_flag)


            elif node == "sps":
                value = sps_configuration_check(row)
                if value == "true":
                    sps_flag.append(value)
                print(msc_flag)






        k = k + 1
        print(k)








except Exception as e:
    print(e)