from tkinter import *
from tkinter.messagebox import *
root = Tk()
root.title(" 五子棋--夏敏捷2016-2-11,仨个小时")

imgs= [PhotoImage(file='D:\\python\\bmp\\BlackStone.gif'), PhotoImage(file='D:\\python\\bmp\\WhiteStone.gif')]
turn=0
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
        cv.create_image((x*40+20,y*40+20),image=img1)
        cv.pack()
        map[x][y]=str(turn)
        k=win_lose( )
        print (k)
        print_map( ) #输出map地图
        if win_lose( )==True:
            if turn==0 :
                showinfo(title="提示",message="黑方你赢了")
            else:
                showinfo(title="提示",message="白方你赢了")
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
   #End Function
def print_map( ):#输出map地图
    for i in range(0,15):#0--14 
       for j in range(0,15):#0--14
           print (map[i][j],end=' ')
       print ('w')
    
#map = [[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
#       [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
#       [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
#       [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
#       [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
#       [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],]

#map =  [[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]] * 15错误

map =  [[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]for y in range(15)]
cv = Canvas(root, bg = 'green', width = 610, height = 610)
drawQiPan( )
cv.bind("<Button-1>", callback)
cv.pack()

root.mainloop()
