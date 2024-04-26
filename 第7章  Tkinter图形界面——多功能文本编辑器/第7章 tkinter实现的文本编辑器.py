from tkinter import * 
import os
 
filename = ''
 
def author():
    showinfo(title="作者",message="xmj")
 
def about():
    showinfo(title="关于",message="用Tkinter编写记事本功能")
 
def myopenfile():
    global filename
    filename = filedialog.askopenfilename(title='打开文件', filetypes=[('文本文件', '.txt')] )
    if filename == '':
        filename = None
    else:
        root.title('FileName:'+os.path.basename(filename))
        textPad.delete(1.0,END)
        f = open(filename,'r')
        textPad.insert(1.0,f.read())
        f.close()
 
def mynew():
    global filename
    root.title('未命名文件')
    filename = None
    textPad.delete(1.0,END)
 
def mysave():
    global filename
    try:
        f = open(filename,'w')
        msg = textPad.get(1.0,END)
        f.write(msg)
        f.close()
    except:
        saveas()
 
 
def mysaveas():
    f = filedialog.asksaveasfilename(initialfile= '未命名.txt', defaultextension='.txt')
    global filename
    filename = f
    if filename=="":
        return
    fh = open(f,'w')
    msg = textPad.get(1.0,END)
    fh.write(msg)
    fh.close()
    root.title('FileName:'+os.path.basename(f))
 
def cut():
    textPad.event_generate('<<Cut>>')
 
def copy():
    textPad.event_generate('<<Copy>>')
 
def paste():
    textPad.event_generate('<<Paste>>')
 
def redo():
    textPad.event_generate('<<Redo>>')
 
def undo():
    textPad.event_generate('<<Undo>>')
 
def selectAll():
    textPad.tag_add('sel','1.0',END)
 
def search():
    def dosearch():
        myentry = entry1.get()             #获取查找的内容--string型
        whatever = str(textPad.get(1.0,END))
        # print textPad.index('zxc')
        # print myentry
        # print "%d个"%(whatever.count(myentry))    #计算substr在S中出现的次数
        messagebox.showinfo("查找结果：","you searched %s, there are %d in the text"%(myentry,whatever.count(myentry)))
        # print whatever.find(myentry)
 
        # teIndex = textPad.index(myentry)
        # textPad.linestart(teIndex)
        # textPad.mark_set('insert', teIndex)
        # textPad.mark_set(myentry,CURRENT + '+5c')
        # textPad.mark_set(myentry,CURRENT + ' wordstart')
    topsearch = Toplevel(root)
    topsearch.geometry('300x30+200+250')
    label1 = Label(topsearch,text='Find')
    label1.grid(row=0, column=0,padx=5)
    entry1 = Entry(topsearch,width=20)
    entry1.grid(row=0, column=1,padx=5)
    button1 = Button(topsearch,text='查找',command=dosearch)
    button1.grid(row=0, column=2)
     
 
root = Tk()
root.title('Tkinter编写记事本')
root.geometry("800x500+100+100")
 
# 创建一个顶级菜单
menubar = Menu(root)   

# 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中 
filemenu = Menu(menubar)
filemenu.add_command(label='新建', accelerator='Ctrl + N', command= mynew)
filemenu.add_command(label='打开', accelerator='Ctrl + O',command = myopenfile)
filemenu.add_command(label='保存', accelerator='Ctrl + S', command=mysave)
filemenu.add_command(label='另存为', accelerator='Ctrl + Shift + S',command=mysaveas)
menubar.add_cascade(label='文件',menu=filemenu)

# 创建一个下拉菜单“操作”，然后将它添加到顶级菜单中
editmenu = Menu(menubar)
editmenu.add_command(label='撤销', accelerator='Ctrl + Z', command=undo)
editmenu.add_command(label='重做', accelerator='Ctrl + y', command=redo)
editmenu.add_separator()
editmenu.add_command(label = "剪切",accelerator = "Ctrl + X",command=cut)
editmenu.add_command(label = "复制",accelerator = "Ctrl + C", command=copy)
editmenu.add_command(label = "粘贴",accelerator = "Ctrl + V", command= paste)
editmenu.add_separator()
editmenu.add_command(label = "查找",accelerator = "Ctrl+ F", command=search)
editmenu.add_command(label = "全选",accelerator = "Ctrl + A", command= selectAll)
menubar.add_cascade(label = "操作",menu = editmenu)

# 创建一个下拉菜单“about”，然后将它添加到顶级菜单中
aboutmenu = Menu(menubar)
aboutmenu.add_command(label = "作者", command=author)
aboutmenu.add_command(label = "关于", command = about)
menubar.add_cascade(label = "about",menu=aboutmenu)
 
#toolbar
toolbar = Frame(root, height=25,bg='grey')
shortButton = Button(toolbar, text='打开',command = myopenfile)
shortButton.pack(side=LEFT, padx=5, pady=5)
 
shortButton = Button(toolbar, text='保存', command = mysave)
shortButton.pack(side=LEFT)
toolbar.pack(expand=NO,fill=X)
 
#Status Bar
status = Label(root, text='Ln20',bd=1, relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM, fill=X)
 
#linenumber&text
lnlabel =Label(root, width=2, bg='antique white')
lnlabel.pack(side=LEFT, fill=Y)
 
textPad = Text(root, undo=True)
textPad.pack(expand=YES, fill=BOTH)
 
scroll = Scrollbar(textPad)
textPad.config(yscrollcommand= scroll.set)
scroll.config(command = textPad.yview)
scroll.pack(side=RIGHT,fill=Y)


# 显示菜单
root.config(menu = menubar)
#快捷键绑定
root.bind_all("<Control-f>", lambda event: search())
root.bind_all("<Control-s>", lambda event: mysave())
root.bind_all("<Control-n>", lambda event: mynew())
root.bind_all("<Control-a>", lambda event: selectAll())
root.bind_all("<Control-o>", lambda event: myopenfile())

root.mainloop()
