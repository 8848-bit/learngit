import xlrd #Python第三方模块，用来读取Excel表格数据

"""xlrd读取Excel步骤
    读取工作薄
    读取工作表
    获取工作内容
"""
data = xlrd.open_workbook("data1.xlsx")  #打开文档
print(data.sheet_loaded(0)) #查看索引为0的工作表是否加载
data.unload_sheet(0) #卸载索引为0的工作表
print(data.sheet_loaded(0))
print(data.sheet_loaded(1))

#操作表

#print(data.sheets()) #获取全部sheet
#print(data.sheets()[0]) 
#print(data.sheet_by_index(0)) #根据索引获取工作表
#print(data.sheet_by_name('Sheet1')) #根据名称获取工作表
#print(data.sheet_names()) #获取所有工作表的名字
#print(data.nsheets) #获取所有工作表的数量

#操作excel行

#sheet = data.sheet_by_index(0) #获取第一个工作表
#print(sheet.nrows) #获取sheet下的有效行数
#print(sheet.row(0)) #该行单元格对象组成的列表
#print(sheet.row_types(1)) #获取单元格的数据类型
#print(sheet.row(0)[0].value) #得到单元格的value
#print(sheet.row_values(0)) #得到指定行单元格的value
#print(sheet.row_len(0)) #得到单元格的长度

#操作excel列
#sheet = data.sheet_by_index(0)
#print(sheet.ncols)
#print(sheet.col(0)) #该列单元格对象组成的列表
#print(sheet.col(0)[0].value)
#print(sheet.col_values(0)) #返回该列所有单元格的value组成的列表
#print(sheet.col_types(0))

#操作Excel单元格
#sheet = data.sheet_by_index(0)
#print(sheet.cell_type(0,0))
#print(sheet.cell(0,0).ctype) #获取单元格的数据类型（1表示文本，2表示数字，3表示date日期，4表示，5表示布尔）
#print(sheet.cell(0,0).value)
#print(sheet.cell_value(0,0))


