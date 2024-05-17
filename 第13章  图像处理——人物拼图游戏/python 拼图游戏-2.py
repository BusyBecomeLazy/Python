from tkinter import *
from tkinter.messagebox import *
import random


root = Tk('拼图2017')
root.title(" 拼图--夏敏捷2017-10-5")
# 载入外部图像 
Pics = []
for i in range(9):
   filename="woman_"+str(i)+".png"
   Pics.append(PhotoImage(file=filename))
# 定义常量
# 画布的尺寸
WIDTH = 312 
HEIGHT = 450 
# 图像块的边长 
IMAGE_WIDTH = WIDTH // 3
IMAGE_HEIGHT = HEIGHT // 3 

# 棋盘行列数
ROWS = 3
COLS = 3 
# 移动步数
steps = 0 
#  保存所有图像块的列表
board = [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]]

# 图像块类
class Square:  
    def __init__(self, orderID):
        self.orderID = orderID 
    def draw(self, canvas, board_pos):
        img = Pics[self.orderID]
        canvas.create_image(board_pos, image=img) 
# 初始化拼图板
def init_board(): 
    # 打乱图像块坐标
    L=list(range(8))
    L.append(None)      
    random.shuffle(L)
    # 填充拼图板 
    for i in range(ROWS): 
      for j in range(COLS):
           idx = i * ROWS + j 
           orderID = L[idx]
           if orderID is None:
               board[i][j] = None
           else:
               board[i][j] = Square(orderID) 
# 重置游戏 
def play_game():
    global steps 
    steps = 0
    init_board()
 
# 绘制游戏界面各元素
def drawBoard(canvas):
    # 画黑框 
    canvas.create_polygon((0, 0, WIDTH, 0, WIDTH, HEIGHT, 0, HEIGHT),width=1,outline='Black')
    # 画目标图像 
    #canvas.draw_image(baymax, [WIDTH/2, WIDTH/2], [WIDTH, WIDTH], [50, WIDTH+50], [98, 98])
      # 画步数 
    #canvas.draw_text("步数："+str(steps), [400, 680], 22, "White") 
    # 画图像块 
    # 代码写在这里
    for i in range(ROWS):
         for j in range(COLS):
             if board[i][j] is not None:
                  board[i][j].draw(canvas, (IMAGE_WIDTH*(j+0.5),IMAGE_HEIGHT*(i+0.5) )) 
def mouseclick(pos):
    global steps 
    # 将点击位置换算成拼图板上的坐标
    r = int(pos.y // IMAGE_HEIGHT)
    c = int(pos.x // IMAGE_WIDTH)
    print(r,c)
    if r < 3 and c < 3:   # 点击位置在拼图板内才移动图片
        if board[r][c] is None: # 点到空位置上什么也不移动
            return
        else: 
            # 依次检查当前图像块的上,下,左,右是否有空位置，如果有就移动当前图像块
            current_square = board[r][c] 
            if r - 1 >= 0 and board[r-1][c] is None:     # 判断上面
                board[r][c] = None 
                board[r-1][c] = current_square
                steps += 1 
            elif c + 1 <= 2 and board[r][c+1] is None:    # 判断右面
                board[r][c] = None 
                board[r][c+1] = current_square
                steps += 1 
            elif r + 1 <= 2 and board[r+1][c] is None:    # 判断下面
                board[r][c] = None 
                board[r+1][c] = current_square
                steps += 1 
            elif c - 1 >= 0 and board[r][c-1] is None:    # 判断左面
                board[r][c] = None 
                board[r][c-1] = current_square
                steps += 1
            #print(board)
            label1["text"]=str(steps)
            cv.delete('all')  #清除canvas画布上的内容
            drawBoard(cv)
    if win():
       showinfo(title="恭喜",message="你成功了！")
            
def win():
   for i in range(ROWS):
         for j in range(COLS):
            if board[i][j] is not None  and   board[i][j].orderID!=i * ROWS + j:
                return False
   return True
            
def callBack2():
   print("重新开始")
   play_game()
   cv.delete('all')  #清除canvas画布上的内容
   drawBoard(cv)


# 设置窗口
cv = Canvas(root, bg = 'green', width =WIDTH, height = HEIGHT)
b1=Button(root,text="重新开始",command=callBack2,width=20)
label1=Label(root,text="0" ,fg="red",width=20)
label1.pack()
cv.bind("<Button-1>", mouseclick)
cv.find
cv.pack()
b1.pack()
play_game()
drawBoard(cv)
root.mainloop()








