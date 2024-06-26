
import pandas as pd
 
movies = pd.read_csv(r'movies.csv')
ratings = pd.read_csv(r'ratings.csv')
 
data = pd.merge(movies,ratings,on = 'movieId')#通过两数据框之间的movieId连接
data[['userId','rating','movieId','title']].sort_values('userId').to_csv(r'merged.csv',index=False)
 
'''采用python字典来表示每位用户评论的电影和评分'''
file = open(r'merged.csv','r',encoding='UTF-8')#记得读取文件时加‘r’， encoding='UTF-8'
##读取data.csv中每行中除了名字的数据
data = {}##存放每位用户评论的电影和评分
for line in file.readlines():
    #注意这里不是readline()
    line = line.strip().split(',')
    #如果字典中没有某位用户，则使用用户ID来创建这位用户
    if not line[0] in data.keys():
        data[line[0]] = {line[3]:line[1]}
    #否则直接添加以该用户ID为key字典中
    else:
        data[line[0]][line[3]] = line[1]
 
#print(data)
 
from math import pow, sqrt
def Euclidean(user1,user2):
    #取出两位用户评论过的电影和评分
    user1_data=data[user1]
    user2_data=data[user2]
    distance = 0
    #找到两位用户都评论过的电影，并计算欧式距离
    for key in user1_data.keys():
        if key in user2_data.keys():
            #注意，distance越大表示两者越相似
            distance += pow(float(user1_data[key])-float(user2_data[key]),2)
 
    return 1/(1+sqrt(distance))#这里返回值越大，相似度越大
 
def top10_similar(userID):
    res = []
    for userid in data.keys():
        if not userid == userID:
            sim = Euclidean(userID, userid)
            res.append((userid, sim))
    res.sort(key=lambda val:val[1], reverse=True)
    
    return res[:10]
    
RES = top10_similar('1')
print(RES)
 
 
'''根据最相似用户推荐电影'''
def recommend(user, k=5):
    recomm = []
    most_sim_user = top10_similar(user)[0][0]
    items = data[most_sim_user]
    for item in items.keys():
        if item not in data[user].keys():
            recomm.append((item, items[item]))
    recomm.sort(key=lambda val:val[1], reverse=True)
    print(recomm[:k])
    return recomm[:k]
        
RECOM = recommend('1')

print(RECOM)
