from math import *
user_A='15'
def load_data():
    f = open('ratings.csv')
    data={}
    n=1
    for line in f:
        (user,movie,rating,ts) = line.split(',')
        n=n+1
        if n>2000:
            break
        if user=='userId':   #首行是标题
            continue
        #if  user=='92':
        #    print(user,movie,rating,ts)
        #Python 字典 setdefault() 函数和 get()方法 类似,
        #如果键不存在于字典中，将会添加键并将值设为默认值。
        data.setdefault(user,{}) 
        data[user][movie] = float(rating)
    return data
def calculate():
    list = load_data()
    user_diff = {}
    for movies in list[user_A]:
        #print("000",movies)
        for people in list.keys():
            user_diff.setdefault(people,{})
            for item in list[people].keys():
                if item == movies:
                    diff = pow(list[user_A][movies] - list[people][item],2)
                    user_diff[people][item] = diff
    print("0000")
    #print(user_diff)
    return user_diff
def people_rating():
    user_diff = calculate()
    rating = {}
    for people in user_diff.keys():
       
        sumSq = 0
        b = 0
        for score in user_diff[people].values():            
            sumSq+=score
            b+=1
        sim = float(1/(1+ sqrt(sumSq)))
        if b>1:
             rating.setdefault(people,{})
             rating[people] = sim
    print("和所有用户的相似度")
    #print(rating)
    #for key,values in rating.items():
        #print(key,values)
    return rating
def top_list():
    list = people_rating()
    items = list.items()
    top = [[v[1],v[0]] for v in items]
    top.sort(reverse=True)
    print(top[0:10])
    return top

def find_same():
    list = load_data()
    print(list[user_A].items())
    print(list['12'].items())
    print("-----3333")
    for k,v in list[user_A].items():
            for kk,vv in list['12'].items():
                if k == kk:
                    print(k,v,kk,vv)
    print("-----4444")

def find_rec():
    rec_list = top_list()
    
    first = rec_list[1][1]
    second = rec_list[2][1]
    
    if first==user_A:
       first = rec_list[3][1]
    if second==user_A:
       second = rec_list[3][1]   
    all_list = load_data()
    print("最相近用户:",first,second)
    film=[]
    print("推荐影片:")
    for k,v in all_list[first].items():
        if k not in all_list[user_A].keys() and v == 5:
            print (k,end=",")
            film.append(k)

    for k,v in all_list[second].items():
        if k not in all_list[user_A].keys() and v == 5:
            print (k,end=",")
            film.append(k)
    print()
    f = open('movies.csv',encoding='utf-8')
    for line in f:
        #print(line)
        try:
            (movieId,title,genres) = line.split(',')
            if  movieId in film:
                print(movieId,title,genres)
        except:
            continue

find_same()
find_rec()
