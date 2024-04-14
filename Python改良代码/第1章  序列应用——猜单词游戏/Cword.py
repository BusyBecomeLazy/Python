import random

WORDS = {"python", "jumble", "easy", "difficult", "answer", "continue", "phone", "position", "position", "game"}
WORD = WORDS
while True:
    print(
        """
    欢迎来到猜单词游戏!!
    1.开始游戏
    2.退出游戏
    3.查看本次游戏单词
    """)
    index = input("请输入你的选择：")
    index = int(index)
    if index == 1:
        print("\n游戏开始！")
        count = 1
        while WORDS:
            word = WORDS.pop()
            Yword = word
            Cword = ""

            while word:
                # 根据word长度，产生word的随机位置
                Sword = random.randrange(len(word))
                # 将Sword位置字母组合到乱序后单词
                Cword += word[Sword]
                # 通过切片，将position位置字母从原单词中删除
                word = word[:Sword] + word[Sword + 1:]

            print("第" + str(count) + "题：", Cword)
            C1word = input("\n请输入正确顺序的单词：")
            while C1word != Yword:
                print("\n单词不正确！")
                C1word = input("\n请继续猜测：")

            if C1word == Yword:
                print("\n恭喜你回答正确!")

            count += 1
        print("恭喜你完成一轮学习！！")

    elif index == 2:
        break

    elif index == 3:
        print("本次游戏单词有：", WORD)

