base_location = r'E:/Number_series_define/'

result_file_location = f'C:/Users/123/Downloads/New folder/'
result_file_name = f'msc.rst'
mscList = ['DG05_MSOFTX', 'DG06_MSOFT', 'DG10_MSOFT', 'CG11_MSOFT', 'CG12_MSOFT']
spsList = ['SPS01_SPS', 'SPS02_SPS', 'VLSP01_SPS', 'ALSP01_SPS']
msc_flag = []
sps_flag = []
config_status = ''
matching_result = ''


# def get_last_overall_allow(self, result_file_name):
def aa():
    file_path = f'{result_file_location}{result_file_name}'
    try:
        result_data = open(f"{file_path}", "r")
        result_data = result_data.read().splitlines()
        k = 0
        for row in result_data:


            if "GT name  =  VLHS01_MSISDN_" in row:
                msc_flag.append("true")
                print("1")
            if "GT address information" in row:
                msc_flag.append("true")
                print("2")
            if "Load share DSP group name  =  SPS01_SPS02_LDSH" in row:
                msc_flag.append("true")
                print("3")
            if "---    END" in row:
                return msc_flag











    except Exception as e:
        print(e)


a = aa()
print(a)



