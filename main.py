import requests
from bs4 import BeautifulSoup
import lxml


def request_dangdang(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def save_to_excel(soup):
    li_list = soup.find(class_='bang_list clearfix bang_list_mode').find_all('li')
    try:
        for li in li_list:
            list_num = li.find('div').text  #1.
            img = li.find(class_="pic").find('a').find('img').get('src')    #http://img3m4.ddimg.cn/0/32/29276874-1_l_11.jpg
            name = li.find(class_="name").find('a').text    #外婆出租中
            pls = li.find(class_="star").find('a').text #52256条评论
            title = li.find_all(class_="publisher_info")[0].find('a').get('title') #[英]丽芙·阿巴思诺特 ,周唯 译,酷威文化 出品
            cbsj = li.find_all(class_="publisher_info")[1].find('span').text #2021-07-01
            cbs = li.find_all(class_="publisher_info")[1].find('a').text #四川文艺出版社
            biaosheng=li.find(class_="biaosheng").find('span').text #22985次
            price_n=li.find(class_="price_n").text#¥21.00
            price_r=li.find(class_="price_r").text#¥42.00
            price_s=li.find(class_="price_s").terxt#5.0折
            price_e_n = li.find(class_="price_e").find(class_="price_n").text#¥7.98
    except AttributeError:
        return None









def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    html = request_dangdang(url)
    soup = BeautifulSoup(html, 'lxml')
    save_to_excel(soup)


main(1)
