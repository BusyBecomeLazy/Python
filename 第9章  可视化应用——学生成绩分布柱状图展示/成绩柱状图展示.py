import xlrd 
wb = xlrd.open_workbook('marks.xlsx')     # 打开文件
sheetNames = wb.sheet_names()        # 查看包含的工作表  
print(sheetNames)                    #输出所有工作表的名称，['sheet_test']
# 获得工作表的两种方法  
sh = wb.sheet_by_index(0)   
sh = wb.sheet_by_name('Sheet1')      # 通过名称'sheet_test'获取对应的Sheet
# 单元格的值  
cellA1 = sh.cell(0,0)  
cellA1Value = cellA1.value   
print(cellA1Value)                    
# 第一行的值，课程名  
courseList = sh.row_values(0)
print(courseList[2:])                #打印出所有课程名


course=input("请输入需要展示的课程名:")
m=courseList.index(course)
# 第m列的值
columnValueList = sh.col_values(m)   #['math', 95.0, 94.0, 93.0, 96.0]
print(columnValueList)
scoreList = columnValueList[1:]
print('最高分:',max(scoreList))
print('最低分:',min(scoreList))
print('平均分:',sum(scoreList)/len(scoreList) )

import matplotlib.pyplot as plt
import numpy as np
#x = scoreList
#plt.hist(x,bins=10,color='green',normed=True)

y = [0,0,0,0,0]
for score in scoreList:
    if score>=90:
        y[0]+=1
    elif score>=80:
        y[1]+=1
    elif score>=70:
        y[2]+=1
    elif score>=60:
        y[3]+=1
    else:
        y[4]+=1
y=[20,10,30,25,15]
x1=['>=90','80~89分','70~79分','60~69分','60分以下']
x=[1,2,3,4,5]
plt.xlabel("分数段")
plt.ylabel("人数")
plt.rcParams['font.sans-serif'] = ['SimHei'] 	  #指定默认字体  
plt.xticks(x,x1)                                  #设置x坐标
rects=plt.bar(left=x,height=y,color='green',width=0.5) 
plt.title(course+"成绩分析")
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x()+rect.get_width()/2.0, 1.03*height, "%s" %float(height))
plt.show()
