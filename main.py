import requests
import xlwt
from bs4 import BeautifulSoup
import pandas as pd


def request_dangdang(url):
    try:
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44'
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


book = xlwt.Workbook(encoding='utf-8', style_compression=0)

item = []


def save_to_excel(soup):
    global item
    li_list = soup.find(class_='bang_list clearfix bang_list_mode').find_all('li')

    print(li_list.__len__())
    for li in li_list:
        try:
            list_num = li.find('div').text  # 1.
            img = li.find(class_="pic").find('a').find('img').get(
                'src')  # http://img3m4.ddimg.cn/0/32/29276874-1_l_11.jpg
            name = li.find(class_="name").find('a').text  # 外婆出租中
            pls = li.find(class_="star").find('a').text  # 52256条评论
            title = li.find_all(class_="publisher_info")[0].find('a').get('title')  # [英]丽芙·阿巴思诺特 ,周唯 译,酷威文化 出品
            cbsj = li.find_all(class_="publisher_info")[1].find('span').text  # 2021-07-01
            cbs = li.find_all(class_="publisher_info")[1].find('a').text  # 四川文艺出版社
            biaosheng = li.find(class_="biaosheng").find('span').text  # 22985次
            price_n = li.find(class_="price_n").text  # ¥21.00
            price_r = li.find(class_="price_r").text  # ¥42.00
            price_s = li.find(class_="price_s").terxt  # 5.0折
            price_e_n = li.find(class_="price_e").find(class_="price_n")  # ¥7.9
            if price_e_n is not None:
                price_e_n = price_e_n.text
            q = {'排名': list_num, '图片': img, '名字': name, '评论数': pls, '作者': title, '出版时间': cbsj, '出版社': cbs,
                 '五星评论数': biaosheng, '折后价': price_n, '价格': price_r, '打折': price_s, '电子书价': price_e_n}
            print(q)
            item.append(q)
        except AttributeError:
            print("!")

        df = pd.DataFrame(item)
        df.to_csv("x.csv", index=False)


def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    html = request_dangdang(url)
    soup = BeautifulSoup(html, 'lxml')
    save_to_excel(soup)


if __name__ == '__main__':

    for i in range(1, 26):
        main(i)
