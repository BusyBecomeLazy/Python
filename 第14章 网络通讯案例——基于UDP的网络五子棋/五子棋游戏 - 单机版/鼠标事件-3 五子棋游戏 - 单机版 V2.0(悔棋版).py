from tkinter import *
from tkinter.messagebox import *
root = Tk()
root.title(" 五子棋--夏敏捷2016，右键可以悔棋，欢迎使用")
#五子棋--夏敏捷2016-2-11,仨个小时，右键可以悔棋，欢迎使用
imgs= [PhotoImage(file='D:\\python\\bmp\\BlackStone.gif'), PhotoImage(file='D:\\python\\bmp\\WhiteStone.gif')]
turn=0  #0黑方，1白方
back=[]
def callback(event):#走棋
    global turn
    #print ("clicked at", event.x, event.y,turn)
    x=(event.x)//40  #换算棋盘坐标
    y=(event.y)//40
    print ("clicked at", x, y,turn)   
    if map[x][y]!=" ":
       showinfo(title="提示",message="已有棋子")
    else:
        img1= imgs[turn]
        id=cv.create_image((x*40+20,y*40+20),image=img1)
        back.append((id,x,y))        #保存下过的棋子的图形对象id，便于删除
        print(back)
        cv.pack()
        map[x][y]=str(turn)
        k=win_lose( )
        print (k)
        #print_map( )            #输出map地图
        if checkWin(x,y):       #win_lose( )==True:
            if turn==0 :
                showinfo(title="提示",message="黑方你赢了")
            else:
                showinfo(title="提示",message="白方你赢了")
        #换下一方走棋
        if turn==0 :
            turn=1
        else:
            turn=0
def huiqi(event):   #悔棋
    global turn
    if  len(back)==0:
        showinfo(title="提示",message="已没有任何棋子了！！")
        return
    m=back.pop()
    id=m[0]         #即得到刚走的棋子的图形对象id
    x=m[1]
    y=m[2]
    map[x][y]=' '   #修改地图信息,' '代表此处无棋子
    cv.delete(id)   #删除棋子
    #cv.move(id,10,10)
    #换下一方走棋
    if turn==0 :
        turn=1
    else:
        turn=0
    
    

def drawQiPan( ):#画棋盘
    for i in range(0,15):
        cv.create_line(20,20+40*i,580,20+40*i,width=2)
    for i in range(0,15):
        cv.create_line(20+40*i,20,20+40*i,580,width=2)
    cv.pack()
    
def win_lose( ):#输赢判断
    #扫描整个棋盘，判断是否连成五颗
    a = str(turn)
    print ("a=",a)
    for i in range(0,11):#0--10
        # 判断X= Y轴上是否形成五子连珠
        for j in range(0,11):#0--10
            if map[i][j] == a and map[i + 1][j + 1] == a and map[i + 2][j + 2] == a and map[i + 3][j + 3] == a and map[i + 4][j + 4] == a :
                print("X=  Y轴上形成五子连珠")
                return True


    for i in range(4,15):# 4 To 14
        # 判断X= -Y轴上是否形成五子连珠
        for j in range(0,11):#0--10
            if map[i][j] == a and map[i - 1][j + 1] == a and map[i - 2][j + 2] == a and map[i - 3][j + 3] == a and map[i - 4][j + 4] == a :
                print("X= -Y轴上形成五子连珠")
                return True

    for i in range(0,15):#0--14
        # 判断Y轴上是否形成五子连珠
        for j in range(4,15):# 4 To 14
            if map[i][j] == a and map[i][j - 1] == a and map[i][j - 2] == a and map[i][j - 3] == a and map[i][j - 4] == a :
                print("Y轴上形成五子连珠")
                return True

    for i in range(0,11):#0--10
        # 判断X轴上是否形成五子连珠
        for j in range(0,15):#0--14
            if map[i][j] == a and map[i + 1][j] == a and map[i + 2][j] == a and map[i + 3][j] == a and map[i + 4][j] == a :
                print("X轴上形成五子连珠")
                return True
    return False
#-------------------------
'''checkWin()判断这个棋子是否和其他的棋子连成5子即输赢判断。
它是以（x,y）为中心横向、纵向、斜方向的判断来统计相同个数实现。
'''
def checkWin(x,y):
    flag = False
    #保存共有相同颜色多少棋子相连
    count = 1
    #判断横向是否有5个棋子相连，特点 纵坐标 是相同，
    #即map[x][y]中y值是相同
    color = map[x][y]
    #通过循环来做棋子相连的判断
    #横向的判断
    i = 1
    while  color == map[x + i][y + 0] :
         count=count+1 
         i=i+1 
    i = 1
    while  color == map[x - i][y - 0] :
         count=count+1 
         i=i+1 
    if  count >= 5  :
        flag = True

    # 纵向的判断
    i2 = 1 
    count2 = 1
    while color == map[x + 0][y + i2]:
        count2=count2+1 
        i2=i2+1 
    i2 = 1 
    while  color == map[x - 0][y - i2]:
        count2=count2+1
        i2=i2+1
    if count2 >= 5:
        flag = True

    #斜方向的判断（右上 + 左下）
    i3 = 1
    count3 = 1
    while color == map[x + i3][y - i3]:
        count3=count3+1
        i3=i3+1
    i3 = 1
    while color == map[x - i3][y + i3]:
        count3=count3+1
        i3=i3+1
    if count3 >= 5:
        flag = True
    
    # 斜方向的判断（右下 +左上）
    i4 = 1
    count4 = 1
    while color == map[x + i4][y + i4]:
        count4=count4+1
        i4=i4+1
    i4 = 1
    while color == map[x - i4][y - i4]:
        count4=count4+1
        i4=i4+1
    if count4 >= 5:
        flag = True
    return flag
#-----------------


def print_map( ):                 #输出map地图
    for i in range(0,15):#0--14 
       for j in range(0,15):#0--14
           print (map[i][j],end=' ')
       print ('w')
    


map =  [[" "for y in range(15)]for x in range(15)]
cv = Canvas(root, bg = 'green', width = 610, height = 610)
drawQiPan( )
cv.bind("<Button-1>", callback)    #绑定鼠标左键事件，下棋功能
cv.bind("<Button-3>", huiqi)       #绑定鼠标右键事件，悔棋功能
cv.pack()

root.mainloop()
