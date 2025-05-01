from urllib import request
from lxml import etree
import json
import re
import ssl


# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context


def get_headers():
    """
    返回请求头信息
    :return:
    """
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/65.0.3325.181 Safari/537.36"
    }
    return headers


def get_url_content(url):
    """
    获取指定url的请求内容
    :param url:
    :return:
    """
    content = ''
    headers = get_headers()
    res = request.Request(url, headers=headers)
    try:
        resp = request.urlopen(res, timeout=10)
        content = resp.read().decode('utf-8')
    except Exception as e:
        print('exception: %s' % e)
    return content


def parse_content(content):
    """
    解析网页
    :param content:
    :return:
    """
    movie = {}
    html = etree.HTML(content)
    try:
        info = html.xpath("//div[@id='info']")[0]
        movie['director'] = info.xpath("./span[1]/span[2]/a/text()")[0]
        movie['screenwriter'] = info.xpath("./span[2]/span[2]/a/text()")[0]
        movie['actors'] = '/'.join(info.xpath("./span[3]/span[2]/a/text()"))
        movie['type'] = '/'.join(info.xpath("./span[@property='v:genre']/"
                                            "text()"))
        movie['initialReleaseDate'] = '/'.\
            join(info.xpath(".//span[@property='v:initialReleaseDate']/text()"))
        movie['runtime'] = \
            info.xpath(".//span[@property='v:runtime']/text()")[0]

        def str_strip(s):
            return s.strip()

        def re_parse(key, regex):
            ret = re.search(regex, content)
            movie[key] = str_strip(ret[1]) if ret else ''

        re_parse('region', r'<span class="pl">制片国家/地区:</span>(.*?)<br/>')
        re_parse('language', r'<span class="pl">语言:</span>(.*?)<br/>')
        re_parse('imdb', r'<span class="pl">IMDb链接:</span> <a href="(.*?)" '
                         r'target="_blank" rel="nofollow">')
    except Exception as e:
        print('解析异常: %s' % e)
    return movie


def spider():
    """
    爬取豆瓣前100部热门电影
    :return:
    """
    recommend_moives = []
    movie_api = 'https://movie.douban.com/j/search_subjects?' \
                'type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend' \
                '&page_limit=100&page_start=0'
    content = get_url_content(movie_api)
    json_dict = json.loads(content)
    subjects = json_dict['subjects']
    for subject in subjects:
        content = get_url_content(subject['url'])
        movie = parse_content(content)
        movie['title'] = subject['title']
        movie['rate'] = subject['rate']
        recommend_moives.append(movie)
        print(len(recommend_moives))
    print(recommend_moives)


if __name__ == '__main__':
    spider()
