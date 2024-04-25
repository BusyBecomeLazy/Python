from tkinter import *
# -*- coding: UTF-8 -*-
from urllib import request
from urllib import parse
import json
def translate_Word(en_str):
    # simulation browse load host url,get cookie
    # http://fanyi.baidu.com/v2transapi?from=en&to=zh&query=hello%20world&transtype=hash
    URL = 'http://fanyi.baidu.com/v2transapi'
    #en_str=input("请输入要翻译的内容:")
    #创建Form_Data字典，存储向服务器发送的Data
    #Form_Data={'from':'en','to':'zh','query':en_str,'transtype':'hash'}
    Form_Data = {}
    Form_Data['from'] = 'en'
    Form_Data['to'] = 'zh'
    Form_Data['query'] = en_str                      #要翻译数据
    Form_Data['transtype'] = 'hash'
    data = parse.urlencode(Form_Data).encode('utf-8')    #使用urlencode方法转换标准格式
    response = request.urlopen(URL,data)              #传递Request对象和转换完格式的数据
    html = response.read().decode('utf-8')              #读取信息并解码
    translate_results = json.loads(html)                #使用JSON
    print(translate_results)                         #打印出JSON数据
    translate_results = translate_results['trans_result']['data'][0]['dst']    #找到翻译结果
    print("翻译的结果是：%s" % translate_results)     #打印翻译信息
    return  translate_results
def leftClick(event):				        #翻译按钮事件函数
   print( "x轴坐标:", event.x)
   print( "y轴坐标:", event.y)
   en_str=Entry1.get()		                        #获取要翻译的内容
   print(en_str)
   vText=translate_Word(en_str)
   label_val_q.config(Entry2,text=vText)		#修改提示标签文字

if __name__ == "__main__":
    root = Tk()
    root.title("单词翻译器")
    root['width']=250;root['height']=130
    Label(root,text = '输入要翻译的内容：',width=15).place(x=1,y=1)    #绝对坐标（1，1）
    Entry1=Entry(root,width=20)
    Entry1.place(x=110,y=1)                           #绝对坐标（110，1）
    Label(root,text = '翻译的结果：',width=18).place(x=1,y=20)     #绝对坐标（1，20）
    Entry2=Entry(root,width=20)
    Entry2.place(x=110,y=20)                   #绝对坐标（110，20）
    Button1=Button(root,text = '翻译',width=8)
    Button1.place(x=40,y=80)    #绝对坐标（40，80）
    Button2=Button(root,text = '清空',width=8)
    Button2.place(x=110,y=80)   #绝对坐标（110，80）
    #给Label绑定鼠标监听事件
    Button1.bind("<Button-1>",leftClick)                  #翻译按钮
    Button1.bind("<Button-1>",leftClick)                  #清空按钮
    root.mainloop()
