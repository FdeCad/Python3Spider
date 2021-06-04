import requests
from bs4 import BeautifulSoup as BS
import pandas as pd
import time
import random
import json
import csv
import urllib.parse as p


#读取上次爬取的CSV文件,以便断点爬取
def init_df():
    global df_sights
    try:
        df_sights=pd.read_csv('qunaer_sights.csv')
    except:
        df_sights=pd.DataFrame()


#初始化CSV writer,第一次需写入列名
def init_csv():
    global f
    global writer
    global df_sights
    csvfile='qunaer_sights.csv'
    f=open(csvfile,'a+',newline='',encoding='utf-8')
    writer=csv.writer(f)
    if df_sights.columns.empty:
        writer.writerow(['景点名','等级','地址','介绍','热度','价格','月销量','经度','纬度'])
        #writer.writerow(['景点名', '等级', '地址', '介绍', '热度', '价格', '月销量'])


#程序结束前关闭CSV文件
def close_csv():
    global f
    f.close()


#调用百度地图API获取景点地址对应的经纬度
def get_geo_info(address):
    geo_uri='http://api.map.baidu.com/geocoder/v2/?'
    geo_params={
        'output':'json',
        'ak':'qmnKZsgNE3NWxwRvoiuVrhuRujDRDQQa'
    }
    #更新url中的地址参数
    geo_params.update({'address':address})
    data=p.urlencode(geo_params)
    cur_geo_uri=geo_uri+data
    geo_resp=requests.get(cur_geo_uri)
    json_data=json.loads(geo_resp.text)

    #调用成功,获取JSON data中的经纬度信息
    if json_data['status']==0:
        longitude=json_data['result']['location']['lng']
        latitude=json_data['result']['location']['lat']
    else:
        longitude=''
        latitude=''

    return longitude,latitude


#抓取去哪儿网站热门景点销售信息
def dump_qunaer_sights(pages):
    global df_sights
    global writer
    base_url='http://piao.qunar.com/ticket/list.htm?keyword=热门景点&page='
    headers={'cookie':'QN99=8770; QN1=eIQjmVtYQgbBDaEiPevvAg==; csrfToken=zKMVroGqYK6fdBphXg8rqQ3MpcaiZ7TZ; QN269=AA9586A58FEC11E88A24FA163E233FC1; QN601=3f55b4673bbd18ac3206bfea7c5996d3; QunarGlobal=10.86.213.148_6291bf49_164d0ba9dbf_-1a4d|1532510727219; _i=RBTKSaIAM3KBlurx6OwRjfuQ8pEx; QN300=auto_4e0d874a; QN163=0; QN6=auto_4e0d874a; QN48=tc_427b9f2555dccb4c_164d9787381_d960; _RSG=Ue4lzWGVuXAKnGpozKI.OB; _RDG=28c738c8ddc979203b2642a9f86b2ac273; _RGUID=a8787d08-3dbc-4a1e-b63e-494f72cd0c54; QN205=auto_4e0d874a; QN234=home_free_t; _vi=Xan8_FldA2NGBwqzRSKDNIYHisxd4ARxiomsg1mowQsC4OV3wCXnooJECkbZWsL9_3XGq9mmj5lTyMlGPRfgZD0jC_eS-Vas8fJyOdtOVO02USpBUqqwRZ1LfhiofVGvkPVi9NW0omogB1BkpWCaX2atkxba7uWItHjFuSd5R2NK; QN162=%E6%B7%B1%E5%9C%B3; _pk_ref.1.8600=%5B%22%22%2C%22%22%2C1533374400%2C%22http%3A%2F%2Ftouch.qunar.com%2F%22%5D; _pk_ses.1.8600=*; QN233=FreetripTouchin; _RF1=122.91.2.150; DJ12=eyJxIjoi5p2t5bee6Ieq55Sx6KGMIiwic3UiOiI0MDk1MTE3NjY5IiwiZCI6Iua3seWcsyIsImUiOiJBIiwibCI6IjAsMjgiLCJ0cyI6IjgxYmUwZjQ3LTdmYTAtNDliYy1iYTA0LWFlYTU4NzM0ZmRkMSJ9; _pk_id.1.8600=92302397325aca81.1533353790.3.1533375421.1533368101.; QN243=125',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37'}
    for i in range(pages):
        print('page:{0}'.format(i+1))
        url=base_url+str(i+1)
        resp=requests.get(url,headers=headers)
        print(resp.status_code)
        time.sleep(random.uniform(1,3))

        #通过BeautifulSoup解析当前页面HTML,获取景点列表信息
        soup=BS(resp.text,'lxml')
        sight_list=soup.select('.sight_item')
        for sight in sight_list:
            #获取景点名
            name=sight.select('.name')[0].text
            #如该景点已存在CSV文件中,则跳过该页,继续抓取下一页(断点续爬)
            if not df_sights.empty and not df_sights[df_sights['景点名']==name].empty:
                break

            #获取景点等级
            try:
                level=sight.select('.level')[0].text.replace('景区','')
            except:
                level=''

            #获取景点地址
            address=sight.select('.area > a')[0].text.split('·')[-1]
            # address = sight.select('.address color999 > span')[0].text.replace('地址:','')


            #获取景点介绍
            intro=sight.select('.intro.color999')[0].text

            #获取景点热度
            star=sight.select('.product_star_level em span')[0].text.replace('热度 ','')

            #获取门票价格,月销量
            try:
                price=sight.select('.sight_item_price em')[0].text
                sales=sight.select('.hot_num')[0].text
            except:
                continue

            #将景点地址转换为经纬度
            longitude,latitude=get_geo_info(address)

            #向CSV文件中插入一条景点信息
            #sight_item=[name,level,address,intro,star,price,sales]
            sight_item = [name, level, address, intro, star, price, sales,longitude,latitude]
            print(sight_item)
            writer.writerow(sight_item)



if __name__ == '__main__':
    init_df()
    init_csv()
    dump_qunaer_sights(5)
    close_csv()
