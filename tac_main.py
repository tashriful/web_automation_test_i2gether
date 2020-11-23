from tac_functions import bmc_plan_format_check
from tac_functions import list_output_status_check
from tac_functions import mme_get
from tac_functions import consistency_status_check

excel_file_location = f'C:/Users/123/Downloads/Tac Define/tac.xlsx'
result_file_location = f'C:/Users/123/Downloads/Tac Define/'
result_file_name = f'dummy.rst'
add_file_name = f'addcommand.txt'
virtual_mme_name = ['CTG_BD02_vUSN01', 'DH_D03_vUSN02','DH_VL01_vUSN03' , '10.17.214.162','DH_PB03_vUSN04','CTG_AL03_vUSN05', 'CTG_AK09_vUSN06']
legacy_mme_name = ['DHK_PUB_USN03','AKHTER_USN2','CG_BD_USN04','PUBAIL_SGSN']

# plan_format_status = bmc_plan_format_check(excel_file_location)
# print(plan_format_status)

# a = mme_get(excel_file_location)
# print(a)
# if all(item in a for item in virtual_mme_name):
#     print("virtual")
#
# if all(item in a for item in legacy_mme_name):
#     print("legacy")
#
a = list_output_status_check(result_file_location,result_file_name)
print(a)
if not a:
    print("undefined")

# a = consistency_status_check(result_file_location,add_file_name, True)
# print(a)





