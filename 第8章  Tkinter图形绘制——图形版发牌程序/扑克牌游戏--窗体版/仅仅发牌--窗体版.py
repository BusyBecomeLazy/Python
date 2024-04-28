#!/usr/bin/env python
# -*- coding: utf-8 -*-
#latest edit: 2016-2-16 
  
#to ensure the utf8 encoding environment
import sys
import random
from tkinter import * 
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
 
 
n=52
def gen_pocker(n):
    x=100
    while(x>0):
       x=x-1
       p1=random.randint(0,n-1)
       p2=random.randint(0,n-1)
       t=pocker[p1]
       pocker[p1]=pocker[p2]
       pocker[p2]=t 
    return pocker
 
def getColor(x):
    color=["黑桃","红桃","草花","方块"]
    c=int(x/13)
    if c<0 or c>=4:
        return "ERROR!"
    return color[c]
 
 
def getValue(x):
    value=x % 13
    if value==0:
        return 'A'
    elif value>=1 and value<=9:
        return str(value+1)
    elif value==10:
        return 'J'
    elif value==11:
        return 'Q'
    elif value==12:
        return 'K'
 
def getPuk(x):
    return getColor(x)+getValue(x)
 
(a,b,c,d)=([],[],[],[])
 
pocker=[i for i in range(n)]
pocker=gen_pocker(n)
print(pocker)
 
for x in range(13):
    m=x*4
    a.append(getPuk(pocker[m]))
    b.append(getPuk(pocker[m+1]))
    c.append(getPuk(pocker[m+2]))
    d.append(getPuk(pocker[m+3]))
a.sort()
b.sort()
c.sort()
d.sort()
print("牌手1",end=":")
for x in a:
    print (x,end=" ")
print("\n牌手2",end=": ")
for x in b:
    print (x,end=" ")
print("\n牌手3",end=": ")   
for x in c:
    print (x,end=" ")
print("\n牌手4",end=": ")  
for x in d:
    print (x,end=" ")


def callback(event):
    print ("clicked at", event.x, event.y)
    

(player1,player2,player3,player4)=([],[],[],[])
(p1,p2,p3,p4)=([],[],[],[])
root = Tk()
# 创建一个Canvas，设置其背景色为白色 
cv = Canvas(root, bg = 'white', width = 800, height = 650)
imgs=[]
for i in range(1,5):
    for j in range(1,14):
        imgs.insert((i-1)*13+(j-1),PhotoImage(file='D:\\python\\images\\'+str(i)+'-'+str(j)+'.gif'))
#imgs=[PhotoImage(file='D:\\python\\image\\'+str(i+1)+'.gif') for i in range(52)]
##for i in range(0,52): 
##   img=imgs[pocker[i]]   
##   #print(str(pocker[i])+'.gif')
##   
##   id=cv.create_image((100+20*i,200),image=img)
##   #id.bind("<Button-1>", callback)

##for x in range(0,13):
##    m=x*4
##    img=imgs[pocker[m]]
##    player1.append(cv.create_image((200+20*x,100),image=img))
##    img=imgs[pocker[m+1]]
##    player2.append(cv.create_image((100,150+20*x),image=img))
##    img=imgs[pocker[m+2]]
##    player3.append(cv.create_image((200+20*x,500),image=img))
##    img=imgs[pocker[m+3]]
##    player4.append(cv.create_image((560,150+20*x),image=img))
for x in range(13):         #13轮
    m=x*4
    p1.append( pocker[m] )
    p2.append( pocker[m+1] )
    p3.append( pocker[m+2] )
    p4.append( pocker[m+3] )
p1.sort()
p2.sort()
p3.sort()
p4.sort()
for x in range(0,13):    
    img=imgs[p1[x]]
    player1.append(cv.create_image((200+20*x,100),image=img))
    img=imgs[p2[x]]
    player2.append(cv.create_image((100,150+20*x),image=img))
    img=imgs[p3[x]]
    player3.append(cv.create_image((200+20*x,500),image=img))
    img=imgs[p4[x]]
    player4.append(cv.create_image((560,150+20*x),image=img))
print("player1:",player1)
print("player2:",player2)
print("player3:",player3)
print("player4:",player4) 
cv.pack()
root.mainloop() 
