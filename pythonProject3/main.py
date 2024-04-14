import requests
from lxml import etree
import csv


def getHtml(url,headers):
    response = requests.get(url,headers=headers)
    content = response.text
    return content

def getData():
    tree = etree.HTML(content)
    li_list = tree.xpath('.//ul[@class = "resblock-list-wrapper"]/li')
    for li in li_list:
        name = li.xpath()


def saveData():
    pass

def main():
    pass

if __name__ == '__main__':
    main()
