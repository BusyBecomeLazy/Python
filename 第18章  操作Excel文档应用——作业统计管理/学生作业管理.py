import os  
  
def file_name(file_dir):   
    for root, dirs, files in os.walk(file_dir):  
        print(root) #当前目录路径  
        #print(dirs) #当前路径下所有子目录  
        print(files) #当前路径下所有非目录子文件
  
def file_name2(file_dir):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):
         
        for file in files:
            
            if os.path.splitext(file)[1] == '.docx':  
                L.append(os.path.join(root, file))
    print(L)
    return L

import os
import xlrd
import xlwt
#file_dir=r"K:\夏敏捷Python书稿 课件和代码（已发过）\通识课作业--夏敏捷2018 2019\2018上作业 Python\作业2"

def listdir(path, list_name):  
    for file in os.listdir(path):       
        if  os.path.splitext(file)[1]=='.doc' or  os.path.splitext(file)[1]=='.docx':  
            list_name.append(file)



def get_upnum(list_name):
    wb = xlrd.open_workbook('test.xlsx')		# 打开文件
    sheetNames = wb.sheet_names()			# 查看包含的工作表  
    #print(sheetNames) 					#输出所有工作表的名称，['sheet_test']
    # 获得工作表的两种方法  
    table = wb.sheet_by_index(0)  
    table = wb.sheet_by_name('Sheet1')		        # 通过名称'sheet1'获取对应的Sheet

    nrows = table.nrows    #表格的行数
    ncols = table.ncols     #表格的列数
    student={}
    for i in range(1,nrows):    
        xuehao = table.cell(i,0).value    #获取单元格的值
        stuname = table.cell(i,1).value    #获取单元格的值
        student[xuehao]=0
        for filename in list_name:
            if xuehao in filename and stuname in filename:
                student[xuehao]=1
    print("输出未交学生的学号")
    #输出未交学生的学号
    for  key,values  in student.items():
        if values==0:
            print(key,end=",")
    print()
    return student

def save_up(all_zuoye):
    wb = xlrd.open_workbook('test.xlsx')		# 打开文件
    sheetNames = wb.sheet_names()			# 查看包含的工作表  
    table = wb.sheet_by_name('Sheet1')		        # 通过名称'sheet1'获取对应的Sheet
    nrows = table.nrows    #表格的行数
    ncols = table.ncols     #表格的列数
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('sheet_test', cell_overwrite_ok=True)  #单元格可重复写
    sheet.write(0, 0, '学号')
    sheet.write(0, 1, '姓名')
    n=2
    num={}
    for zuoye_i in zuoye:
        #sheet.write(0, 2, '作业1')
        sheet.write(0, n, zuoye_i)
        student=all_zuoye[zuoye_i]
        for i in range(1,nrows):    
            xuehao = table.cell(i,0).value    #获取单元格的值
            stuname = table.cell(i,1).value    #获取单元格的值
            sheet.write(i, 0, xuehao)
            sheet.write(i, 1, stuname)
            sheet.write(i, n, student[xuehao])
            if xuehao in num:
                 num[xuehao]=num[xuehao]+student[xuehao]#统计次数
            else:
                 num[xuehao]=student[xuehao]
        n=n+1
    #写入次数
    sheet.write(0, n, '总次数')
    for i in range(1,nrows):
        xuehao = table.cell(i,0).value    #获取单元格的值
        sheet.write(i, n, num[xuehao]) 

    book.save('test2.xls')   #不支持xlsx格式


root=r"K:\夏敏捷Python书稿 课件和代码（已发过）\通识课作业--夏敏捷2018 2019\2018上作业 Python"
zuoye=["作业1","作业2","作业3"]
all_zuoye={}
for zuoye_i in zuoye:
   list_name=[]
   file_dir=os.path.join(root, zuoye_i)   
   if os.path.isdir(file_dir):
       listdir(file_dir, list_name)
       print(zuoye_i)
       all_zuoye[zuoye_i]=get_upnum(list_name)
print(all_zuoye)
save_up(all_zuoye)

