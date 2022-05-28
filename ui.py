from bs4 import BeautifulSoup
import requests
import lxml
import json


def api():
    url = 'https://auchan.zakaz.ua/ru/categories/frozen-for-gourmet-auchan/'
    # url=url+f'/?page={x}'
    # requests.post(url, payload)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    id = soup.find_all('div', 'ProductsBox__listItem')[1].find('a')['data-productkey']

    #print(id)#item id
    #id='04820212330612'
    new_url=f"https://auchan.zakaz.ua/ru/products/{id}"
    res=requests.get(new_url).text
    su=BeautifulSoup(res,'html.parser')
    a=su.select('script[type="application/ld+json"]')
    ap1=(a[1].string)#create Api
    ap2=json.loads(ap1)
    print(ap2['offers']['price'])
    print(ap2['name'])
    print(ap2['offers']['availability'][19:])
    # for app in su.find_all('script'):
    #     print(app)
    # print(response.text)
api()