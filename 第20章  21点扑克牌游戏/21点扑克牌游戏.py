from tkinter import *
from tkinter.messagebox import *
import random
class Card(Button):   #块类  
    '''构造函数

    '''
    def __init__(self,x,y,face,suitType,master,bm):
        Button.__init__(self,master)
        self.X=x
        self.Y=y
        self.face=face           #牌面大小，值为0,1,…12（代表A,2,3,4,5,6,7,8,9,10,J,Q,K）
        self.suitType=suitType   #牌面花色，值为0~3 （代表草花、方块、红桃、黑桃）        
        #self.bind("<ButtonPress>",btn_MouseDown)
        #self.bind("<ButtonRelease>",btn_Realse)
        self.place(x=self.X*18,y=self.Y*20+150)
        if (face < 10):
            self.count = face + 1  #self.count是点数
        else:  #J,Q,K
            self.count = 10
        self.faceup =  False
        self.img=bm
        if self.faceup:   #牌面是否向上
           self["image"]=bm
        else:
           self["image"]=back
    def DrawCard(self,x,y):  #在指定位置显示扑克牌
        self.place(x=x,y=y)
        self["image"]=self.img
    def RemoveCard(self):     #移到窗口外
        self.place(x=-100,y=-100)
        

def callback1(event): #发牌
    global TopCard,ipcard,idcard
    global dealerAce,playerAce,dealerCount,playerCount
    dealerAce = 0           #庄家A牌个数 
    playerAce = 0           #玩家A牌个数 
    dealerCount = 0         #庄家点数 
    playerCount = 0         #玩家点数
    if(TopCard>0):
        for i in range(0,TopCard) :
            Deck[i].RemoveCard()   #已发过的牌移到窗口外
    #画玩家第一张牌面
    Deck[TopCard].DrawCard(200, 300)     #绘制到屏幕的坐标为（200，300）
    playerCount = playerCount + Deck[TopCard].count
    if (Deck[TopCard].face == 0):
        playerCount += 10
        playerAce += 1
    TopCard += 1
      
    #画庄家第一张牌面
    Deck[TopCard].DrawCard(200, 10)        #绘制到屏幕的坐标为（200，10）
    dealerCount += Deck[TopCard].count
    if (Deck[TopCard].face == 0): 
        dealerCount += 10
        dealerAce += 1 
    TopCard += 1
    #***********************************
    #画玩家第二张牌面
    Deck[TopCard].DrawCard(265, 300)
    playerCount += Deck[TopCard].count

    if (Deck[TopCard].face == 0 and playerAce == 0):
        playerCount += 10
        playerAce += 1
        
    TopCard += 1

    #画庄家第二张牌面
    Deck[TopCard].DrawCard(265, 10)
    dealerCount += Deck[TopCard].count

    if (Deck[TopCard].face == 0 and dealerAce == 0):
        dealerCount += 10
        dealerAce += 1
    TopCard += 1

    ipcard = 2
    idcard = 2
    if (TopCard >= 52):
       showinfo(title="提示",message="一副牌完了！！")
       return
    label1["text"] = "玩家"+str(playerCount)
    label2["text"] = "庄家"+str(dealerCount)
    bt1["state"] = DISABLED 
    bt2["state"] = NORMAL
    bt3["state"] = NORMAL

def callback2(event):#要牌
    global TopCard,ipcard
    global dealerAce,playerAce,dealerCount,playerCount
    Deck[TopCard].DrawCard(200 + 65 * ipcard, 300)
    playerCount += Deck[TopCard].count
    if (Deck[TopCard].face == 0):
        playerCount += 10
        playerAce += 1 
    TopCard += 1
    if (TopCard >= 52):
       showinfo(title="提示",message="一副牌完了！！")
       return
    ipcard += 1
    label1["text"] = "玩家"+str(playerCount)
    if (playerCount > 21):
        if (playerAce >= 1):
            playerCount -= 10
            playerAce -= 1
            label1["text"] = "玩家"+str(playerCount)
        else:
            label1["text"] = "玩家"+str(playerCount)
            showinfo(title="提示",message="玩家Player loss!")
            bt1["state"] = NORMAL
            bt2["state"] = DISABLED
            bt3["state"] = DISABLED 
            
                     
def callback3(event):#停牌
    dealerPlay()     #庄家选牌
#庄家游戏过程中，为简化起见，仅仅判断庄家（电脑）牌的点数是否超过18点，不到则继续要牌。dealerPlay()实现庄家选牌并判断玩家输赢。
def dealerPlay():#庄家选牌
    #实现庄家选牌
    global TopCard,idcard
    global dealerAce,playerAce,dealerCount,playerCount
    while True:
        if (dealerCount < 18):
            Deck[TopCard].DrawCard(200 + 65 * idcard, 10);
            dealerCount += Deck[TopCard].count
            if (dealerCount > 21 and dealerAce >= 1):
                dealerCount -= 10
                dealerAce -= 1;
            if (Deck[TopCard].face == 0 and dealerCount <= 11):
                dealerCount += 10
            TopCard += 1;
            if (TopCard >= 52):
                showinfo(title="提示",message="一副牌完了！！")
                return
            idcard += 1
        else:
             break
    label2["text"] = "庄家"+str(dealerCount)
    if (dealerCount <= 21):     #庄家未超过21点
        if (playerCount > dealerCount):    #玩家点数超过庄家点数
            showinfo(title="提示",message="玩家Player win!");
        else:
            showinfo(title="提示",message="庄家 win!")
    else:                      #庄家超过21点,玩家赢
        showinfo(title="提示",message="玩家Player win!")
    bt1["state"] = NORMAL
    bt2["state"] = DISABLED
    bt3["state"] = DISABLED
    

win = Tk()#创建窗口对象
win.title("21点扑克牌--夏敏捷")#设置窗口标题
win.geometry("995x550")
imgs= [PhotoImage(file='image\\'+str(i)+'.gif')for i in range(1,53)]
back=PhotoImage(file='image\\0.gif')
Deck=[]
TopCard=0
dealerAce = 0           #庄家A牌个数 
playerAce = 0           #玩家A牌个数 
dealerCount = 0         #庄家点数 
playerCount = 0         #玩家点数
ipcard=0
idcard=0
bt1 = Button(win, text = '发牌', width = 60, height = 60)
bt1.place(x= 100,y=400, width = 60, height = 60)

bt2 = Button(win, text = '要牌', width = 60, height = 60)
bt2.place(x= 200,y=400, width = 60, height = 60)

bt3 = Button(win, text = '停牌', width = 60, height = 60)
bt3.place(x= 300,y=400, width = 60, height = 60)
bt1.focus_set() #将焦点设置到bt上
bt1.bind("<ButtonPress>", callback1)
bt2.bind("<ButtonPress>", callback2)
bt3.bind("<ButtonPress>", callback3)
bt1["state"] = NORMAL
bt2["state"] = DISABLED
bt3["state"] = DISABLED 
label1 = Label(win, text = '玩家', width = 60, height = 60)
label1.place(x= 0,y=300, width = 60, height = 60)
label2 = Label(win, text = '电脑', width = 60, height = 60)
label2.place(x= 0,y=50, width = 60, height = 60)
list=[i for i in range(0,53)]
for i in range(0,4) :#0--3（代表梅花、方块、黑桃、红桃）
    for j in range(0,13):#0--12（代表A,2,3,4,5,6,7,8,9,10,J,Q,K）
        card=Card((j+1)+2*i,0,j,i,win,imgs[i + 4 * j])
        Deck.append(card)
random.shuffle(Deck)  #将列表中元素打乱，洗牌目的

win.mainloop()
