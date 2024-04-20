from tkinter import *
from tkinter.ttk import *


class App:
    def __init__(self):
        self.windos = Tk()
        self.windos.title("✽万年历 ✽")
        self.windos.geometry("430x400")
        self.lis1 = ["周一", "周二", "周三", "周四", "周五", "周六", "周天"]
        self.images = []
        self.creat_image_lis()
        self.creat_res()
        self.windos.mainloop()

    def func1(self):
        self.get_total_days(self.a, self.b)
        print(self.lis1[self.get_week(self.a, self.b) - 1])
        self.print_days(self.a, self.b)

    def creat_image_lis(self):
        for i in range(1, 13):
            self.images.append("res/%s.png" % i)

    def view_image(self):
        self.ima = PhotoImage(file=self.images[self.b - 1])
        self.L3.config(image=self.ima)

    def go(self, *args):

        self.T1.delete(0.0, END)
        try:
            self.a = int(self.C1.get())
            self.b = int(self.C2.get())
            self.func1()

        except Exception:
            self.T1.insert(END, "请输入年份和月份")

    def run_game(self):
        a1 = Apps()
        if self.windos.quit():  # 如果主程序关闭
            Apps.windows.quit()  # 子程序关闭

    def creat_res(self):
        self.L1 = Label(self.windos, text="年份:")
        self.L2 = Label(self.windos, text="月份:")
        self.L3 = Label(self.windos)
        self.T1 = Text(self.windos)
        self.T1.place(x=10, y=10, width=280, height=150)
        self.B1 = Button(self.windos, text="显示", command=self.go)
        self.B1.place(x=300, y=80)
        self.B2 = Button(self.windos, text="退出", command=self.windos.quit)
        self.B2.place(x=300, y=130)
        self.B3 = Button(self.windos, text="娱乐", command=self.run_game)
        self.B3.place(x=300, y=180)
        self.temp1 = StringVar()
        self.temp2 = StringVar()
        self.C1 = Combobox(self.windos, values=[x for x in range(2010, 2099)])
        self.C2 = Combobox(self.windos, values=[x for x in range(1, 13)])
        self.C1.place(x=300, y=30, width=60, height=30)
        self.C2.place(x=375, y=30, width=50, height=30)
        self.L1.place(x=300, y=0, width=70, height=30)
        self.L2.place(x=370, y=0, width=50, height=30)
        self.L3.place(x=10, y=170, width=280, height=220)

    def leap_year(self, a):
        if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
            return True
        else:
            return False

    def year_days(self, a, b):
        if b in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif b in (4, 6, 9, 11):
            return 30
        else:
            if self.leap_year(a) == True:
                return 29
            else:
                return 28

    def get_total_days(self, a, b):
        total_days = 0
        for m in range(1800, a):
            if self.leap_year(m) == True:
                total_days += 366
            else:
                total_days += 365
        for i in range(1, b):
            total_days += self.year_days(a, i)
        return total_days

    # 获得每月1日为星期几。星期日返回0，星期一返回1，星期二返回2，其他以此类推，星期六返回6。
    def get_week(self, a, b):
        # 返回当月1日是星期几，由1800.01.01是星期三推算
        return (self.get_total_days(a, b) + 3) % 7

    def print_days(self, a, b):
        print("%s年 %s月" % (self.a, self.b))
        self.T1.insert(END, "%s年 %s月" % (self.a, self.b) + "\n")
        print(" 周一 周二 周三 周四 周五 周六 周日")
        self.T1.insert(END, " 周一 周二 周三 周四 周五 周六 周日" + "\n")
        self.i = self.get_week(self.a, self.b)
        # print(self.a,self.b) #2018 6
        # print(self.i) #5
        s = 0
        lis1 = [x for x in range(1, self.year_days(self.a, self.b) + 1)]
        if self.i == 0:
            self.i = 7
        for m in range(1, self.i):
            lis1.insert(0, "  ")
        for i in lis1:
            print("%03s" % i, end="  ")
            self.T1.insert(END, "%03s" % i + "  ")
            s += 1
            if s % 7 == 0:
                self.T1.insert(END, "\n")
                print("\n")


if __name__ == '__main__':
    ap = App()
