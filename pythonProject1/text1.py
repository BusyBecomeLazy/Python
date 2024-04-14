import urllib.request
from bs4 import BeautifulSoup

# 设置请求头模拟浏览器请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 发送HTTP请求，获取网页内容
url = 'https://www.douban.com/'

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        web_content = response.read()

    soup = BeautifulSoup(web_content, 'html.parser')

    # 使用 CSS 选择器查找热门话题容器
    hot_topics_container = soup.select_one('div.mod.hot-topics')

    if hot_topics_container:
        hot_topic_titles = hot_topics_container.find_all('a', class_='lnk-hot-topic')

        if hot_topic_titles:
            for title in hot_topic_titles:
                print(title.text)
        else:
            print("未找到热门话题标题")
    else:
        print("未找到热门话题容器")

except Exception as e:
    print(f"发生错误：{e}")
