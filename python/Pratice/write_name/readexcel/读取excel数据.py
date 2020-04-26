'''
从Excel中读取文件
'''

import xlrd

file_name = r'C:\Users\ljd\Desktop\0001.xlsx'
file = xlrd.open_workbook(file_name)

# 输出Excel中表的个数
print(file.nsheets)

# 读取某张表
sheet = file.sheet_by_name("Sheet1")
# 获取表的行数
nrows = sheet.nrows
# 获取表的列数
ncols = sheet.ncols
print("nrows: %d, ncols: %d" % (nrows, ncols))

# 获取第一行第一列的数据
cell_value = sheet.cell_value(0, 0)
print(cell_value)

# 获取第一行的数据
row_value = sheet.row_values(0)
print(row_value)