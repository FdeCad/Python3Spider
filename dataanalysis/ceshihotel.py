from bs4 import BeautifulSoup
import csv

with open('html.txt','r',encoding='utf-8') as f:
    response=f.read()
def parse(response):
    soup=BeautifulSoup(response,'lxml')
    items=soup.find('ul',id='hotel_lst_body').find_all('li')
    for item in items:
        hotel= {}
        hotel['酒店名']=item.contents[0].contents[2].contents[0].contents[1].text
        hotel['价格']=item.contents[0].contents[1].contents[1].text
        hotel['评分']=item.contents[0].contents[2].contents[1].span.text
        hotel['评价']=item.contents[0].contents[2].contents[1].contents[1].text
        hotel['地址']=item.contents[0].contents[2].contents[2].text
        hotel['点评']=item.contents[0].contents[2].contents[1].contents[2].text
        savetocsv(hotel)

def savetocsv(hotel):
    """
    保存到csv文件
    :param hotel: 酒店信息
    :return:
    """
    with open('qunar_routes.csv','a+',newline='',encoding='utf-8') as csvfile:
        fieldnames=['酒店名','价格','评分','评价','地址','点评']
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writerow(hotel)

parse(response)