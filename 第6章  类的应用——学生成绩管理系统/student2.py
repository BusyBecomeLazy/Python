import os
 
class Student: #定义一个学生类
  def __init__(self):
    self.name = ''
    self.ID =''
    self.score1 = 0
    self.score2 = 0
    self.score3 = 0
    self.sum = 0
  def sumscore(self):  #计算总分
     self.sum=self.score1 + self.score2 + self.score3
#------------ 
 
def searchByID(stulist, ID): #按学号查找看是否学号已经存在
  for item in stulist:
     if item.ID == ID:
         return True
 
def Add(stulist,stu): #添加一个学生信息
     if searchByID(stulist, stu.ID) == True:
         print("学号已经存在！")
         return False
     stulist.append(stu)
     print(stu.name,stu.ID, stu.score1, stu.score2, stu.score3, stu.sum)
     print("是否要保存学生信息？")
     nChoose = input("Choose Y/N")
     if nChoose == 'Y' or nChoose == 'y':
         file_object = open("students.txt", "a")
         file_object.write(stu.ID)
         file_object.write(" ")
         file_object.write(stu.name)
         file_object.write(" ")
         file_object.write(str(stu.score1))
         file_object.write(" ")
         file_object.write(str(stu.score2))
         file_object.write(" ")
         file_object.write(str(stu.score3))
         file_object.write(" ")
         file_object.write(str(stu.sum))
         file_object.write("\n")
         file_object.close()
         print("保存成功！")
 
def Search(stulist, ID): #搜索一个学生信息
 print("学号\t姓名\t语文\t数学\t英语\t总分")
 count = 0
 for item in stulist:
     if item.ID == ID:
         print(item.ID, '\t' ,item.name,'\t', item.score1,'\t',item.score2, '\t', item.score3, '\t',item.sum)
         break
     count = count + 1
 if count == len(stulist):
     print("没有该学生学号！")
 
def Del(stulist, ID): #删除一个学生信息
 count = 0
 for item in stulist:
      if item.ID == ID:
           stulist.remove(item)
           print("删除成功！")
           break
      count +=1
 if count == len(stulist):
     print("没有该学生学号！")
 file_object = open("students.txt", "w")  #覆盖写入
 for stu in stulist:
     print (stu.ID, stu.name, stu.score1,stu.score2, stu.score3, stu.sum)
     file_object.write(stu.ID)
     file_object.write(" ")
     file_object.write(stu.name)
     file_object.write(" ")
     file_object.write(str(stu.score1))
     file_object.write(" ")
     file_object.write(str(stu.score2))
     file_object.write(" ")
     file_object.write(str(stu.score3))
     file_object.write(" ")
     file_object.write(str(stu.sum))
     file_object.write("\n")
 # print("删除保存成功！")
 file_object.close()
     
def Change(stulist, ID):  #修改学生信息
  count = 0
  for item in stulist:
     if item.ID == ID:
        stulist.remove(item)
        file_object = open("students.txt", "w")
        for stu in stulist:
          #print li.ID, li.name, li.score
          file_object.write(stu.ID)
          file_object.write(" ")
          file_object.write(stu.name)
          file_object.write(" ")
          file_object.write(str(stu.score1))
          file_object.write(" ")
          file_object.write(str(stu.score2))
          file_object.write(" ")
          file_object.write(str(stu.score3))
          file_object.write(" ")
          file_object.write(str(stu.sum))
          file_object.write("\n")
        file_object.close()
  #输入这个被修改学生的新信息
  stu = Student()
  stu.name = input("请输入学生的姓名")
  stu.ID = input("请输入学生的ID")
  stu.score1 = int(input("请输入学生语文成绩"))
  stu.score2 = int(input("请输入学生数学成绩"))
  stu.score3 = int(input("请输入学生英语成绩"))
  stu.sumscore()
  Add(stulist,stu) #添加一个stu学生信息到文件中
             
def display(stulist): #显示所有学生信息
    print("学号\t姓名  语文 数学 英语 总分")
    for item in stulist:
        #print(item.ID, '\t' ,item.name,'\t', item.score1,'\t',item.score2, '\t', item.score3, '\t',item.sum)
        print("%5s %5s %3d  %3d  %3d  %4d"%(item.ID,item.name,item.score1,item.score2,item.score3,item.sum))
def Sort(stulist): #按学生成绩排序
     insertSort(stulist)     
     display(stulist)
 
def insertSort(stulist): 
 for i in range(len(stulist)-1): 
    for j in range(i+1,len(stulist)): 
        if stulist[i].sum<stulist[j].sum:
            temp = stulist[i] 
            stulist[i] = stulist[j] 
            stulist[j] = temp 
 
def Init(stulist): #初始化函数
     print("初始化......")
     if os.path.exists('students.txt'):          
         file_object = open('students.txt', 'r')
         for line in file_object:
             stu = Student()
             line = line.strip("\n")
             s = line.split(" ")            #按空格分隔形成列表
             stu.ID = s[0]
             stu.name = s[1]
             stu.score1 = int(s[2])
             stu.score2 = int(s[3])
             stu.score3 = int(s[4])
             stu.sum = int(s[5])
             stulist.append(stu)
         file_object.close()
         print("初始化成功！")
     main()
 
def main(): #主函数 该程序的入口函数
  while True:
     print("*********************")
     print("--------菜单---------")
     print("增加学生信息--------1")
     print("查找学生信息--------2")
     print("删除学生信息--------3")
     print("修改学生信息--------4")
     print("所有学生信息--------5")
     print("按照分数排序--------6")
     print("退出程序------------0")
     print("*********************")
     
     nChoose = input("请输入你的选择：")
     if nChoose == "1":
         stu = Student()
         stu.name = input("请输入学生的姓名")
         stu.ID = input("请输入学生的ID")
         stu.score1 = int(input("请输入学生语文成绩"))
         stu.score2 = int(input("请输入学生数学成绩"))
         stu.score3 = int(input("请输入学生英语成绩"))
         stu.sumscore()
         Add(stulist,stu) 
     if nChoose == '2':
         ID = input("请输入学生的ID")
         Search(stulist, ID)
     
     if nChoose == '3':
         ID = input("请输入学生的ID")
         Del(stulist, ID)       
     if nChoose == '4':
         ID = input("请输入学生的ID")
         Change(stulist, ID)
     
     if nChoose == '5':
         display(stulist)
     
     if nChoose == '6':
         Sort(stulist) 
     
     if nChoose == '0':
         break
       
#主程序 
if __name__ == '__main__':
   stulist =[]
   Init(stulist)
