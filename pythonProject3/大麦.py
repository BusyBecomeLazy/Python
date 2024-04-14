from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os
import time
import csv

# 设置Selenium的选项和初始化WebDriver
option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ['enable-automation'])
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)

# 设置初始值和打开网页
i = 0
items = []

def get_element_text(xpath):
    try:
        return driver.find_element(by=By.XPATH, value=xpath).text
    except Exception as e:
        print(f"Error while getting element text: {e}")
        return ""

def save_image(src, index):
    try:
        r = requests.get(src)
        r.raise_for_status()
        path = fr"D:\demo\图{index}.jpg"  # 此处路径需要更改为你的图片文件夹路径
        with open(path, 'wb') as f:
            f.write(r.content)
        print(f'保存成功: {path}')
    except Exception as e:
        print(f"Error while saving image: {e}")

# 循环遍历多个页面（假设需要爬取前3页）
for page in range(1, 4):
    # 在URL中添加参数以访问不同页码
    page_url = f"https://search.damai.cn/search.htm?spm=a2oeg.home.category.ditem_0.4e2523e1PJPX0w&ctl=%E8%AF%9D%E5%89%A7%E6%AD%8C%E5%89%A7" \
               f"&order=1&cty=%E6%AD%A6%E6%B1%89&pageIndex={page}"
    driver.get(page_url)

    # 等待页面加载完成
    wait = WebDriverWait(driver, 20)  # 将等待时间调整为20秒
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='items']/div[@class='items-wrap']")))

    for j in range(1, 11):
        flag = None
        flag_condition = get_element_text(f"/html/body/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[{i + 1}]/div/div[2]")[0]
        if flag_condition != '艺':
            flag = [3, 2, 5]
        else:
            flag = [4, 3, 6]

        item = {
            'title': get_element_text(f"/html/body/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[{i + 1}]/div/div[1]/a"),
            'time': get_element_text(f"/html/body/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[{i + 1}]/div/div[{flag[0]}]"),
            'place': get_element_text(f"/html/body/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[{i + 1}]/div/div[{flag[1]}]"),
            'amount': get_element_text(f"/html/body/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[{i + 1}]/div/div[{flag[2]}]/span"),
            'href': driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[{i + 1}]/a").get_attribute('href')
        }
        img = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[{i + 1}]/a/img")

        time.sleep(5)
        i += 1
        t = img.get_attribute('src')
        save_image(t, i)

        items.append(item)

# 保存为CSV文件
csv_file_path = "damai_info.csv"
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Title', 'Time', 'Place', 'Amount', 'Href'])
    for item in items:
        csv_writer.writerow([item['title'], item['time'], item['place'], item['amount'], item['href']])

# 打印演出信息
print(items)
print(f"演出信息已保存为CSV文件: {csv_file_path}")

driver.quit()
