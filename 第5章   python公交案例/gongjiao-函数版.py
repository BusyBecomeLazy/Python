import math

rote = {}     #线路信息的字典
rotename=[]   #线路名的的列表
print(rote.values())

def readRote(): #读取线路信息的函数   
   fp=open("gongjiao.txt",'r', encoding='gbk')
   #UnicodeDecodeError: 'gbk' codec can't decode byte 0xbf in position 2: illegal multibyte sequence
   fileContent=""
   while True:
      line=fp.readline()
      if line=="":    # 或者 if not line
         break
      fileContent+=line+'\n';
      list1=line.split("%")     #按%分割
      #print((list1[0]))
      rotename.append(list1[0])

      rote[list1[0]]=list1[1:-1]      #list[:-1]  #增加键对
   fp.close()
   #print(fileContent)
   print(rote.values())    #print(rote['Y807x'])
   print(rote['1s'])
   print(rote['1x'])
   #print(rotename)
   
def findRote():        #线路查询功能
   findRoteName = input("请输入查询线路名")
   if findRoteName in rote:
      print(rote[findRoteName])
   else:
      print("输入的有错误！没有你要查询的线路")
      
def findStation():        #站点查询功能
   stationName = input("请输入查询站点名")
   print('经过此站点的线路有： ',end=' ')
   #遍历字典
   for key,value in rote.items():
      if(stationName in value):
          print(key,end='; ')
   print()

def huanRote():        #换乘查询功能
   startStationName =input("请输入起始站点名")#"火车站"
   endStationName =input("请输入终点名")#"绿城广场" 
   canGo=False
   #遍历value值（线路经过的站点）
   #for value in rote.values():
   for key,value in rote.items():
       if (startStationName in value) and (endStationName in value):
           canGo=True
           print("公交可直达线路",key)
   if canGo==False:
       print("公交不可直达")
       #换乘
       S=[]    #经过起点的线路
       D=[]    #经过终点的线路
       for key,value in rote.items():
           if (startStationName in value):
               S.append(key)
       for key,value in rote.items():
           if (endStationName in value):
               D.append(key)         
       #判断线路之间是否有相同站点
       for key1 in S:
         for key2 in D:
            if  hasSameStation(key1,key2):
               sameStationName=hasSameStation(key1,key2)
               n1=stationNum(startStationName,sameStationName,key1)
               n2=stationNum(endStationName,sameStationName,key2)
               print("经过key1线路"+key1+n1+"站到"+hasSameStation(key1,key2)+"换成key2线路"+key2+n2+"站到达"+endStationName)

#判断线路之间是否有相同站点
def hasSameStation(key1,key2):
    for stationName in rote[key1]:
        if stationName in  rote[key2]:
            return stationName
    return False
#两个站点之间的站数
def stationNum(Station1,Station2,roteName):
    for i in range(len(rote[roteName])):
        stationName=rote[roteName][i]
        if  Station1==stationName:
            i1=i
        if  Station2==stationName:
            i2=i
    return str(int(math.fabs(i1-i2)))         
   
def main(): #主函数 
    readRote()
    while True:
         print( "*********************")
         print( u"--------菜单---------")
         print( u"线路查询------------1")
         print( u"站点查询------------2")
         print( u"换乘查询------------3")
         print( u"添加线路信息--------4")
         print( u"删除线路信息--------5")
         print( u"修改线路信息--------6")
         print( u"退出程序------------0")
         print( "*********************")
         
         nChoose = input("请输入你的选择：")
         if nChoose == "1":
            findRote()
         elif nChoose == "2":
            findStation()
         elif nChoose == "3":
            huanRote()
         elif nChoose == "4":
             #添加线路信息
             fp=open("gongjiao.txt",'a', encoding='gbk')
             addRoteName = input("请输入添加线路名")
             addRoteContent = input("请输入添加线路经过的站点及运行时间,%分割\n")
             fp.write(addRoteName+"%"+addRoteContent+"\n")
             fp.close()       
   
main()#该程序的入口函数

