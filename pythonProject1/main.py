from tkinter import *
from urllib import request
from urllib import parse
import json


def translate_Word(en_str):
    URL = 'http://fanyi.baidu.com/v2transapi'
    Form_Data = {'from': 'en', 'to': 'zh', 'query': en_str, 'transtype': 'hash'}
    data = parse.urlencode(Form_Data).encode('utf-8')

    try:
        response = request.urlopen(URL, data)
        html = response.read().decode('utf-8')
        translate_results = json.loads(html)

        # Check if 'trans_result' key exists in the response
        if 'trans_result' in translate_results:
            translate_results = translate_results['trans_result'][0]['dst']
            print("翻译的结果是：%s" % translate_results)
            return translate_results
        else:
            print("翻译失败，请检查API响应")
            return None

    except Exception as e:
        print(f"发生异常：{e}")
        return None


def leftClick(event):
    en_str = Entry1.get()
    vText = translate_Word(en_str)
    if vText is not None:
        Entry2.delete(0, END)
        Entry2.insert(0, vText)


if __name__ == "__main__":
    root = Tk()
    root.title("单词翻译器")
    root['width'] = 250
    root['height'] = 130

    Label(root, text='输入要翻译的内容：', width=15).place(x=1, y=1)
    Entry1 = Entry(root, width=20)
    Entry1.place(x=110, y=1)

    Label(root, text='翻译的结果：', width=18).place(x=1, y=20)
    Entry2 = Entry(root, width=20)
    Entry2.place(x=110, y=20)

    Button1 = Button(root, text='翻译', width=8)
    Button1.place(x=40, y=80)
    Button1.bind("<Button-1>", leftClick)

    Button2 = Button(root, text='清空', width=8)
    Button2.place(x=110, y=80)

    root.mainloop()

