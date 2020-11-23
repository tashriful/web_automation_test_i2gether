from formatFunctions import plan_file
from formatFunctions import prepare_mailbody

a = plan_file()
# print(f'{a}')
wo = '000xxxhhgaaaaa'
mail_data = {}
body_data_dist ={
    "activity_name": "New TAC Define in MME",
    "wo_num": {wo},
    "date": "0",
    "wo_source": "BMC",
    "plan_format": "BMC"
}
a = plan_file()
print(a)
prepare_mailbody(a, body_data_dist)


