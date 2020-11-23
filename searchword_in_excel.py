import xlrd
sheet_data = []
wb = xlrd.open_workbook(r'C:\Users\123\Downloads\Roaming Complain Inspection\Global_Title_Number_Ranges_2020-10-21.xlsx')
p = wb.sheet_names()
for y in p:
   sh = wb.sheet_by_name(y)
   for rownum in range(sh.nrows):
      # print(sh.row_values(rownum))
      for i in sh.row_values(rownum):
          if i == 'JAPAN':
              print(sh.row_values(rownum))
