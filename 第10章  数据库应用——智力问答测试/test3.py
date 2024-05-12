import sqlite3			# 导入SQLite驱动
# 连接到SQLite数据库，数据库文件是test2.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test2.db')
cursor = conn.cursor()# 创建一个Cursor:
cursor.execute("delete from exam")
# 执行一条SQL语句，创建user表:
#cursor.execute('CREATE TABLE [exam] ([question] VARCHAR(80)  NULL,[Answer_A] VARCHAR(1)  NULL,[Answer_B] VARCHAR(1)  NULL,[Answer_C] VARCHAR(1)  NULL,[Answer_D] VARCHAR(1)  NULL,[right_Answer] VARCHAR(1)  NULL)')
# 继续执行一条SQL语句，插入一条记录:
cursor.execute("insert into exam (question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values ('哈雷慧星的平均周期为', '54年', '56年', '73年', '83年', 'C')")
cursor.execute("insert into exam (question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values ('夜郎自大中“夜郎”指的是现在哪个地方？', '贵州', '云南', '广西', '福建', 'A')")
cursor.execute("insert into exam (question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values ('在中国历史上是谁发明了麻药', '孙思邈', '华佗', '张仲景', '扁鹊', 'B')")
cursor.execute("insert into exam (question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values ('京剧中花旦是指', '年轻男子', '年轻女子', '年长男子', '年长女子', 'B')")
cursor.execute("insert into exam (question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values ('篮球比赛每队几人？', '4', '5', '6', '7', 'B')")
cursor.execute("insert into exam (question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values ('在天愿作比翼鸟，在地愿为连理枝。讲述的是谁的爱情故事？', '焦钟卿和刘兰芝', '梁山伯与祝英台', '崔莺莺和张生', '杨贵妃和唐明皇', 'D')")
# 通过rowcount获得插入的行数:
print(cursor.rowcount)  #1
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()

conn = sqlite3.connect('test2.db')
cursor = conn.cursor()
# 执行查询语句:
cursor.execute('select * from exam')
# 获得查询结果集:
values = cursor.fetchall()
print('k:',len(values))
for k in range(len(values)):
    print(k,values[k][0])
print(values[0])
print(values)
cursor.close()
conn.close()

import tkinter
from tkinter import *
from tkinter.messagebox import *
def callNext():
    global k
    global score
    useranswer=r.get()
    print (r.get())                     #获取被选中单选按钮变量值
    if useranswer==values[k][5]:
        showinfo("恭喜","恭喜你对了！")
        score+=10
    else:
        showinfo("遗憾","遗憾你错了！")    
    k=k+1
    if k>=len(values):
        showinfo("提示","题目做完了")
        return
    #显示下一题
    timu["text"]=values[k][0]
    radio1["text"]=values[k][1]
    radio2["text"]=values[k][2]
    radio3["text"]=values[k][3]
    radio4["text"]=values[k][4]
    r.set('E')
    
def callResult():
    showinfo("你的得分",str(score))


root=tkinter.Tk()
root.title('Python智力问答游戏')
root.geometry("500x200")
r=tkinter.StringVar()						#创建StringVar对象
r.set('E') 							#设置初始值为'E'，初始没选中
k=0
score=0
timu=tkinter.Label(root,text=values[k][0])                      #题目
timu.pack()
f1 = Frame(root)						#创建第1个Frame组件
f1.pack()
radio1=tkinter.Radiobutton(f1,variable=r,value='A',text=values[k][1])
radio1.pack()
radio2=tkinter.Radiobutton(f1,variable=r,value='B',text=values[k][2])
radio2.pack()
radio3=tkinter.Radiobutton(f1,variable=r,value='C',text=values[k][3])
radio3.pack()
radio4=tkinter.Radiobutton(f1,variable=r,value='D',text=values[k][4])
radio4.pack()
f2 = Frame(root)						#创建第2个Frame组件
f2.pack()
Button(f2,text = '下一题',command=callNext).pack(side = LEFT)
Button(f2,text = '结  果',command=callResult).pack(side = LEFT)
root.mainloop()


