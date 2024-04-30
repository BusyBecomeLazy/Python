from tkinter import *
from tkinter.messagebox import *
import socket
import threading
import os

root = Tk()
root.title("网络五子棋V2.1--服务器端")
#五子棋--夏敏捷2016-2-11,仨个小时 网络版
imgs= [PhotoImage(file='D:\\python\\bmp\\BlackStone.gif'), PhotoImage(file='D:\\python\\bmp\\WhiteStone.gif')]
turn=0       #轮到那方走棋 ，0黑方1是白方
Myturn=-1    #第一次确定自己的角色

def callexit(event):#退出
    pos="exit|"
    sendMessage(pos)
    os._exit(0) 
def callpos(event):#走棋
    global turn
    global Myturn
    if Myturn==-1:  #第一次确定自己的角色（白方还是黑方）
        Myturn=turn
    else:
        if(Myturn!=turn):
           showinfo(title="提示",message="还没轮到自己走棋")
           return 
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
        
        pos=str(x)+","+str(y)
        sendMessage("move|"+pos)
        print("服务器走的位置",pos)
        label1["text"]="服务器走的位置"+pos
        
        #输出输赢信息
        if win_lose( )==True:
            if turn==0 :
                showinfo(title="提示",message="黑方你赢了")
                sendMessage("over|黑方你赢了")
            else:
                showinfo(title="提示",message="白方你赢了")
                sendMessage("over|白方你赢了")
        #换下一方走棋
        if turn==0 :
            turn=1
        else:
            turn=0



def drawOtherChess(x,y):#画对方棋子
        global turn
        img1= imgs[turn]
        cv.create_image((x*40+20,y*40+20),image=img1)
        cv.pack()
        map[x][y]=str(turn)
                
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
    #print ("a=",a)
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
    for j in range(0,15):#0--14 
       for i in range(0,15):#0--14
           print (map[i][j],end=' ')
       print ('w')

#接收消息 
def receiveMessage():
    global s
    while True:
        #接收客户端发送的消息
        global addr
        data, addr = s.recvfrom(1024)
        data=data.decode('utf-8')
        a=data.split("|")                          #分割数据
        if not data:
            print('client has exited!')
            break
        elif a[0] == 'join':                      #连接服务器请求
            print('client 连接服务器!')
            label1["text"]='client 连接服务器成功，请你走棋！'
        elif a[0] == 'exit':                      #对方退出信息
            print('client 对方退出!')
            label1["text"]='client 对方退出，游戏结束！'
        elif a[0] == 'over':        #对方赢信息
            print('对方赢信息!')
            label1["text"]=data.split("|")[0] 
            showinfo(title="提示",message=data.split("|")[1] )
        elif a[0] == 'move':        #客户端走的位置信息
            print('received:',data,'from',addr)
            p=a[1].split(",")
            x=int(p[0]);
            y=int(p[1]);
            print(p[0],p[1])
            label1["text"]="客户端走的位置"+p[0]+p[1]
            drawOtherChess(x,y)        #画对方棋子                    
    s.close()
 
#发送消息 
def sendMessage(pos):
    global s
    global addr
    s.sendto(pos.encode(),addr)


#启动线程接收客户端的消息
def startNewThread( ):
        #启动一个新线程来接收客户器端的消息
        #thread.start_new_thread(function,args[,kwargs])函数原型，
        #其中function参数是将要调用的线程函数，args是传递给线程函数的参数，它必须是个元组类型，而kwargs是可选的参数
        #receiveMessage函数不需要参数，就传一个空元组
        thread=threading.Thread(target=receiveMessage,args=())
        thread.setDaemon(True);
        thread.start();    

    
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
cv.bind("<Button-1>", callpos)
cv.pack()
label1=Label(root,text="服务器端....")
label1.pack()
button1=Button(root,text="退出游戏")
button1.bind("<Button-1>", callexit)
button1.pack()
#创建UDP SOCKET
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('localhost',8000))
addr=('localhost',8000)
startNewThread()       ## 启动线程接收客户端的消息receiveMessage();
root.mainloop()


