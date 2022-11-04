import xlrd

'''
通过xlrd模块读取Excel数据
通过pymysql模块连接数据库
组装数据、执行插入操作
关闭数据库连接
'''

data = xlrd.open_workbook("2022-sanguo.xls")
sheet = data.sheet_by_index(0)
introList = [] #空列表存储单元格对象

#简介类
class Introduction:
    pass

for i in range(sheet.nrows):
    if i > 2: #表格从正式数据开始，从1开始会有异常
        obj = Introduction() #构建简介对象
        obj.name = sheet.cell(i, 0).value #姓名
        obj.gender = sheet.cell(i, 1).value #性别
        obj.age = sheet.cell(i, 2).value #年龄
        obj.job = sheet.cell(i, 3).value #职业
        obj.attack = sheet.cell(i, 4).value #攻击力
        obj.ishot = sheet.cell(i, 5).value #是否热门
        introList.append(obj)

print(introList)

#导入操作 pip install pymysql
from mysqlhelper import *

#1. 链接到数据
db = dbhelper('127.0.0.1',3306,"root","root","test")
#2. 插入语句
sql = "insert into intro(name,gender,age,job,attack,ishot) values (%s,%s,%s,%s,%s,%s)"
val = [] #空列表存储元祖
for item in introList:
    val.append((item.name,item.gender,item.age,item.job,item.attack,item.ishot))
print(val)  
db.executemanydata(sql,val)
