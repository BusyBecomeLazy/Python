from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p >
<p class="story">Once upon a time there were three little sisters; and their names were
Elsie,
 and
;
and they lived at the bottom of a well.</p >
<p class="story">...</p >
"""

# 创建BeautifulSoup对象
soup = BeautifulSoup(html_doc, 'html.parser')

# 格式化输出
formatted_html = soup.prettify()

# 打印结果
print(formatted_html)