import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time


headers = {'User-Agent': 'Mozilla/5.0',}
cookiesDit = {'existmag':'all'}
proxies = {"https": 'http://127.0.0.1:1080/pac?auth=6sZoXM8Q3lZyeXZMnVP-&t=201909182318551455'}

testUrl = 'https://avbebe.com/archives/63682'

def download(url):
    # request = Session()
    request = requests
    request.proxies = proxies
    html=request.get(url, headers=headers, cookies=cookiesDit)
    print(html.text)

    # soup = BeautifulSoup(html.text, "html.parser")
    # tag = soup.find_all('div', attrs={'class': 'listInfo'})
    # print(str(tag[0]))

    # r = requests.get(url)
    # with open("", "wb") as f:
    #     f.write(r.content)


def getHTMLText(url):
    # driver = webdriver.PhantomJS(executable_path='D:\\phantomjs-2.1.1-windows\\bin\\phantomjs')  # phantomjs的绝对路径
    # time.sleep(2)
    # driver.get(url)  # 获取网页
    # time.sleep(2)
    # return driver.page_source
    request = requests
    request.proxies = proxies
    html=request.get(url, headers=headers, cookies=cookiesDit)
    print(html.text)
    return html.text

def fillUnivlist(html):
    soup = BeautifulSoup(html, 'html.parser')  # 用HTML解析网址
    tags = soup.find_all('script', attrs={'type': 'text/javascript'})
    print("========")
    if (len(tags)>0):
        for tag in tags:
            print(tag)
    else:
        print('empty')
    return 0


def main():
    download(testUrl)
    # url = 'http://sports.qq.com/articleList/rolls/'  # 要访问的网址
    html = getHTMLText(testUrl)  # 获取HTML
    fillUnivlist(html)

if __name__ == '__main__':
    main()


# python获取完整网页内容（即包括js动态加载的）：selenium+phantomjs
# https://blog.csdn.net/Trisyp/article/details/78845488?utm_medium=distribute.pc_relevant.none-task-blog-baidujs-1
