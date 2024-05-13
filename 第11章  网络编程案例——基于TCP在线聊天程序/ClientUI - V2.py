# _*_ coding:utf-8 _*_
# Filename:ClientUI.py
# Python在线聊天客户端  2016-2-12

import tkinter
import tkinter.font as tkFont 
import socket
import threading
import time
import sys
        
#接收消息
def receiveMessage():
    try:
        #建立Socket连接
        clientSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        clientSock.connect((local, port))
        flag = True
    except:
        flag = False
        chatText.insert(tkinter.END,'您还未与服务器端建立连接，请检查服务器端是否已经启动')
        return
        
    buffer = 1024
    clientSock.send('Y'.encode())
    while True:
        try:
            if flag == True:
                #连接建立，接收服务器端消息
                serverMsg = clientSock.recv(buffer).decode('utf-8')
                if serverMsg == 'Y':
                    chatText.insert(tkinter.END,'客户端已经与服务器端建立连接......')
                elif serverMsg == 'N':
                    chatText.insert(tkinter.END,'客户端与服务器端建立连接失败......')
                elif not serverMsg:
                    continue
                else:
                    theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    chatText.insert(tkinter.END, '服务器端 ' + theTime +' 说：\n')
                    chatText.insert(tkinter.END, '  ' + serverMsg)
            else:
                break
        except EOFError as msg:
            raise msg
            clientSock.close()
            break
              
#发送消息
def sendMessage():
    #得到用户在Text中输入的消息
    message = inputText.get('1.0',tkinter.END)
    #格式化当前的时间
    theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    chatText.insert(tkinter.END, '客户端器 ' + theTime +' 说：\n')
    chatText.insert(tkinter.END,'  ' + message + '\n')
    if flag == True:
        #将消息发送到服务器端
        clientSock.send(message.encode());
    else:
        #Socket连接没有建立，提示用户
        chatText.insert(tkinter.END,'您还未与服务器端建立连接，服务器端无法收到您的消息\n')
    #清空用户在Text中输入的消息
    inputText.delete(0.0,message.__len__()-1.0)

#关闭消息窗口并退出
def close():
    sys.exit()
    
#启动线程接收服务器端的消息
def startNewThread():
    #启动一个新线程来接收服务器端的消息
    #receiveMessage函数不需要参数，就传一个空元组
    thread=threading.Thread(target=receiveMessage,args=())
    thread.setDaemon(True);
    thread.start() 

#主程序   
local = '127.0.0.1'
port = 5505
global clientSock;
flag = False
root = tkinter.Tk()
root.title('Python在线聊天-客户端V2.0')
#窗口面板,用4个面板布局
frame = [tkinter.Frame(),tkinter.Frame(),tkinter.Frame(),tkinter.Frame()]

#显示消息Text右边的滚动条
chatTextScrollBar = tkinter.Scrollbar(frame[0])
chatTextScrollBar.pack(side=tkinter.RIGHT,fill=tkinter.Y)

#显示消息Text，并绑定上面的滚动条
ft = tkFont.Font(family='Fixdsys',size=11)
chatText = tkinter.Listbox(frame[0],width=70,height=18,font=ft)
chatText['yscrollcommand'] = chatTextScrollBar.set
chatText.pack(expand=1,fill=tkinter.BOTH)
chatTextScrollBar['command'] = chatText.yview()
frame[0].pack(expand=1,fill=tkinter.BOTH)

#标签，分开消息显示Text和消息输入Text
label = tkinter.Label(frame[1],height=2)
label.pack(fill=tkinter.BOTH)
frame[1].pack(expand=1,fill=tkinter.BOTH)

#输入消息Text的滚动条
inputTextScrollBar = tkinter.Scrollbar(frame[2])
inputTextScrollBar.pack(side=tkinter.RIGHT,fill=tkinter.Y)

#输入消息Text，并与滚动条绑定
ft = tkFont.Font(family='Fixdsys',size=11)
inputText = tkinter.Text(frame[2],width=70,height=8,font=ft)
inputText['yscrollcommand'] = inputTextScrollBar.set
inputText.pack(expand=1,fill=tkinter.BOTH)
inputTextScrollBar['command'] = chatText.yview()
frame[2].pack(expand=1,fill=tkinter.BOTH)

#发送消息按钮
sendButton=tkinter.Button(frame[3],text=' 发 送 ',width=10,command=sendMessage)
sendButton.pack(expand=1,side=tkinter.BOTTOM and tkinter.RIGHT,padx=15,pady=8)

#关闭按钮
closeButton=tkinter.Button(frame[3],text=' 关 闭 ',width=10,command=close)
closeButton.pack(expand=1,side=tkinter.RIGHT,padx=15,pady=8)
frame[3].pack(expand=1,fill=tkinter.BOTH)

startNewThread()
root.mainloop()
    


