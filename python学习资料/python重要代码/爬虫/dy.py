# 我们用到的库
import requests
import bs4
import re
import pandas as pd


def get_data(url): #模拟用户点击网页
    '''
    功能：访问 url 的网页，获取网页内容并返回
    参数：
        url ：目标网页的 url
    返回：目标网页的 html 内容
    '''
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

    try: #异常机制

        r = requests.get(url, headers=headers)#模拟网页点击地址 url headers网页标头
        r.raise_for_status()#它能够判断返回的Response类型状态是不是200。如果
                            #是200，他将表示返回的内容是正确的，如果不是200，他就会产生一个HttpError的异常。
        return r.text #返回打开网页的文本信息

    except requests.HTTPError as e: #下面的都是异常终止的
        print(e)
        print("HTTPError")
    except requests.RequestException as e:
        print(e)
    except:
        print("Unknown Error !")


def parse_data(html):
    '''
    功能：提取 html 页面信息中的关键信息，并整合一个数组并返回
    参数：html 根据 url 获取到的网页内容
    返回：存储有 html 中提取出的关键信息的数组
    '''
    bsobj = bs4.BeautifulSoup(html, 'html.parser')#*******************
    info = []

    # 获取电影列表
    tbList = bsobj.find_all('table', attrs={'class': 'tbspan'}) #第一页

    # 对电影列表中的每一部电影单独处理
    for item in tbList: #第一页中的每个电影

        movie = []
        link = item.b.find_all('a')[1]#table里面第二个a也就是下载地址
        
        # 获取电影的名称
        name = link["title"]

        # 获取详情页面的 url
        url = 'https://www.dy2018.com' + link["href"]#模拟用户打开网页 前面部分的是固定的

        # 将数据存放到电影信息列表里
        movie.append(name) #电影名字
        movie.append(url) #电影地址

        try:
            # 访问电影的详情页面，查找电影下载的磁力链接
            temp = bs4.BeautifulSoup(get_data(url), 'html.parser')
            tbody = temp.find_all('tbody')#网页的一个标签

            # 下载链接有多个（也可能没有），这里将所有链接都放进来
            for i in tbody:
                download = i.a.text
                if 'magnet:?xt=urn:btih' in download:
                    movie.append(name)#电影名字
                    movie.append(url)#电影地址
                    movie.append(download)#电影下载地址
                    # print(movie)
                    info.append(movie)
                    break

        except Exception as e:
            print(e)
    return info


def save_data(data):
    '''
    功能：将 data 中的信息输出到文件中/或数据库中。
    参数：data 将要保存的数据
    '''
    filename = '动作片1.csv'#需要爬的第几页

    dataframe = pd.DataFrame(data)#保存到pd的表中
    dataframe.to_csv(filename, mode='a', index=False, sep=',', header=False)


def main():
    # 循环爬取多页数据
    for page in range(1, 114):
        print('正在爬取：第' + str(page) + '页......')
        # 根据之前分析的 URL 的组成结构，构造新的 url
        if page == 1:
            index = 'index'
        else:
            index = 'index_' + str(page)

        url = 'https://www.dy2018.com/2/' + index + '.html'

        # 依次调用网络请求函数，网页解析函数，数据存储函数，爬取并保存该页数据
        html = get_data(url) #模拟用户 打开网页
        movies = parse_data(html) #获取网页信息
        save_data(movies)#保存获取到信息

        print('第' + str(page) + '页完成！')

if __name__ == '__main__':
    print('爬虫启动成功！')
    main()
    print('爬虫执行完毕！')
