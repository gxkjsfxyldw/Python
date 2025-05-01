import requests
import pandas as pd	#存储文件使用pandas，然后转成csv文件
import re #正则表达式
import time
import csv
from bs4 import BeautifulSoup #网页解析
import os
from urllib import request #请求网址
#url请求文件头
#url请求文件头
header = {'Content-Type':'text/html; charset=utf-8','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

#登录cookies
Cookie ={'Cookie':'bid="Ve97+drkyB0"; _pk_id.100001.4cf6=7d2077ac91aa48b6.1587438804.4.1588662770.1588658408.; __utma=30149280.1613092148.1587438805.1588658406.1588661961.4; __utmz=30149280.1588661961.4.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/register; __utma=223695111.1833454126.1587438805.1588647865.1588661970.3; __utmz=223695111.1588661970.3.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmc=30149280; __utmc=223695111; ap_v=0,6.0; dbcl2="216329483:06LrWaIzDT8"; ck=HZXS; __gads=ID=369d779cb978645d:T=1588661961:S=ALNI_MZdsAeUdj6gWs8JpwAfB1eTEoH-Ug; push_noty_num=0; push_doumail_num=0; __utmb=30149280.2.10.1588661961; __utmv=30149280.21632; ll="118159"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1588661970%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utmb=223695111.0.10.1588661970; __yadk_uid=V77VrOv8zfO8Tm9PgpNHSXWfbgF1VUs5; _vwo_uuid_v2=D5AFDEF6D6D19CE9970308A4FCCCF763F|5d52a48a9e6857a6d8d9375f99b5c9d2'}

url_1 = 'https://movie.douban.com/subject/35087486/comments?start='
url_2 = '&limit=20&status=P&sort=new_score'
i = 1
while True:
    #拼接url
    url = url_1+str(i*20)+url_2
    print(url)
    try:
        # request请求
        html = requests.get(url, headers=header, cookies=Cookie)
        # beautifulsoup解析网址
        soup = BeautifulSoup(html.content, 'lxml')
        # 评论时间
        comment_time_list = soup.find_all('span', attrs={'class': 'comment-time'})
        # 设置循环终止变量
        if len(comment_time_list) == 0:
            break
        # 评论用户名
        use_name_list = soup.find_all('span', attrs={'class': 'comment-info'})
        # 评论文本
        comment_list = soup.find_all('span', attrs={'class': 'short'})
        # 评分
        rating_list = soup.find_all('span', attrs={'class': re.compile(r"allstar(\s\w+)?")})
        for jj in range(len(comment_time_list)):
            data1 = [(comment_time_list[jj].string,
                      use_name_list[jj].a.string,
                      comment_list[jj].string,
                      rating_list[jj].get('class')[0],
                      rating_list[jj].get('title'))]
            data2 = pd.DataFrame(data1)
            data2.to_csv('douban_movie1.csv', header=False, index=False, mode='a+', encoding="utf-8-sig")

    except:
        print("something is wrong")
    print('page ' + str(i + 1) + ' has done')
    i = i + 1
    time.sleep(2)
    
























