import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://lishi.tianqi.com/wuhan/202310.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Cookie': 'Hm_lvt_ab6a683aa97a52202eab5b3a9042a8d2=1699498188; Hm_lpvt_ab6a683aa97a52202eab5b3a9042a8d2=1699498595'
}

def get_page(url, headers):
    html = requests.get(url, headers=headers)
    if html.status_code == 200:
        html.encoding = html.apparent_encoding
        return html.text
    else:
        return None

date_box = []
max_temp = []
min_temp = []
weh = []
wind = []
week_box = []

html = get_page(url, headers)
bs = BeautifulSoup(html, 'html.parser')

# 使用更稳健的选择方法
data = bs.find_all('div', class_='thrui')

date_pattern = re.compile('class="th200">(.*?)</')
temp_pattern = re.compile('class="th140">(.*?)</')

time_data = re.findall(date_pattern, str(data))

for item in time_data:
    week = item[10:]
    week_box.append(week)
    date_box.append(item[:10])

temp_data = re.findall(temp_pattern, str(data))

# 添加调试语句
print("len(temp_data):", len(temp_data))

for i in range(30):
    # 添加条件判断以避免IndexError
    if i * 4 < len(temp_data):
        max_temp.append(temp_data[i * 4])
        min_temp.append(temp_data[i * 4 + 1])
        weh.append(temp_data[i * 4 + 2])
        wind.append(temp_data[i * 4 + 3])
    else:
        # 如果超出范围，打印提示信息
        print(f"Index {i} out of range for temp_data")

# 创建DataFrame
datas = pd.DataFrame({'日期': date_box, '星期': week_box, '最高温度': max_temp, '最低温度': min_temp, '天气': weh, '风向': wind})
print(datas)
