import xlwt #Python第三方模块，用来写入Excel表格数据

'''
单元格格式和样式设置
'''

titlestyle = xlwt.XFStyle() #初始化样式
titlefont = xlwt.Font()
titlefont.name = "宋体"
titlefont.bold = True #加粗
titlefont.height = 11*20 #字号
titlefont.colour_index = 0x12
titlestyle.font = titlefont

#单元格对齐方式
cellalign = xlwt.Alignment()
cellalign.horz = 0x02
cellalign.vert = 0x01
titlestyle.alignment = cellalign

'''
xlwt写入Excel步骤
    创建工作薄
    创建工作表
    填充工作内容
    保存文件
'''

#创建工作簿
wb = xlwt.Workbook()

#创建工作表
ws = wb.add_sheet("CNY")

#填充标题
ws.write_merge(0,1,0,5,"三国演义人物简介",titlestyle)

#填充数据
data = (("姓名", "性别", "年龄", "职业", "攻击力", "是否热门英雄"), 
        ("吕布", "男", "22", "战士", "5000", "是")
)
#填充索引和值
for i,item in enumerate(data):
    for j,val in enumerate(item):
        ws.write(i+2, j, val)

#创建第二个工作表
wsimage = wb.add_sheet("image")
#写入图片
wsimage.insert_bitmap("2022.bmp",0,0)

#保存文件
wb.save("2022-sanguo.xls")