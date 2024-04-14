import requests
import re
import json
def start():
    for i in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start='+str(i)+'&filter='
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
        response = requests.get(url, headers=headers)
        text = response.text
        regix = '<div class="item">.*?<div class="pic">.*?<em class="">(.*?)</em>.*?<img.*?src="(.*?)" class="">.*?div class="info.*?class="hd".*?class="title">(.*?)</span>.*?class="other">(.*?)</span>.*?<div class="bd">.*?<p class="">(.*?)<br>(.*?)</p>.*?class="star.*?<span class="(.*?)"></span>.*?span class="rating_num".*?average">(.*?)</span>'
        results = re.findall(regix, text, re.S)
        for item in results:
            dic = {
                '电影名称': item[2] + ' ' + re.sub('&nbsp;', '', item[3]),
                '电影图片': re.findall('/public/(.*?).jpg', item[1])[0] + '.jpg',
                '导演和演员': re.sub('&nbsp;', '', item[4].strip()),
                '评分': item[7] + '分',
                '排名': item[0]
            }
            print(dic)
            file = item[1]
            filename = re.findall('/public/(.*?).jpg', str(item[1]))[0]
            file_image(file, filename)
            file_data(dic)
def file_image(file, filename):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
    r = requests.get(file, headers=headers)
    with open(filename + '.jpg', 'wb') as f:
        f.write(r.content)
def file_data(dic):
    with open('douban_film.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(dic, ensure_ascii=False) + '\n')
if __name__ == '__main__':
    start()

