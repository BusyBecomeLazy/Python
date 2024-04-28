#!/usr/bin/env python
# -*- coding: utf-8 -*-
#latest edit: 2016-2-16 
  
#to ensure the utf8 encoding environment
import sys
import random
 
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

