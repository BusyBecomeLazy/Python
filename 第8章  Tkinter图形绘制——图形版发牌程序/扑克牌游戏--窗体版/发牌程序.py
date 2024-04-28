#import tkinter
#top = tkinter.Tk()
#label = tkinter.Label(top,text='Hello World')
#label.pack()
#tkinter.mainloop()
from tkinter import *

root = Tk()
# 创建一个Canvas，设置其背景色为白色 
cv = Canvas(root, bg = 'white', width = 500, height = 650) 
rt = cv.create_rectangle(10,10,110,110,outline='red',stipple='gray12',fill='green')

# 重新设置rt的坐标（相当于移动一个item） 
#cv.coords(rt,(40,40,200,100))
imgs= [PhotoImage(file='D:\\python\\bmp\\'+str(i)+'.gif') for i in range(3)]
for i in range(0,3):
   print(i)
   #img=PhotoImage(file='D:\\python\\bmp\\'+str(i)+'.gif')
   img=imgs[i]
   cv.create_image((100+20*i,200),image=img)
   print(str(i)+'.gif')
img1=PhotoImage(file='D:\\python\\bmp\\'+str(0)+'.gif')
p1=cv.create_image((400,100),image=img1)
cv.coords(p1,(400,300))
cv.coords(rt,(400,300,10,10))
cv.pack()
root.mainloop() 

