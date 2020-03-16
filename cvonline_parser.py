import requests
import json
from bs4 import BeautifulSoup as bs

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/53.0.2785.143 Safari/537.36 '}

base_url = 'https://www.cv.ee/objavlenija-o-rabote/vene?sort=inserted&dir=desc'

data = []


def cvonline_parse():
    session = requests.Session()
    request = session.get(base_url, headers=headers)

    if request.status_code == 200:

        soup = bs(request.content, "lxml")

        offer_wrapper = soup.find(class_='cvo_module_offers_wrap')
        offers = offer_wrapper.find_all(class_='cvo_module_offer_content')

        for offer in offers:
            item = {}
            item['title'] = offer.find('a', attrs={'itemprop': 'title'}).text
            item['firm_name'] = offer.find('a', attrs={'itemprop': 'name'}).text
            item['link'] = offer.find('a', attrs={'itemprop': 'title'}).get('href')
            item['date'] = offer.find('span', attrs={'itemprop': 'datePosted'}).text
            item['site'] = 'Cv-Online'
            data.append(item)

            print("title: " + item['title'])
            print("firm_name: " + item['firm_name'])
            print("link: " + item['link'])
            print("date: " + item['date'])
            print("site: " + item['site'])

        with open("cvonline.json", "w", encoding='utf8') as writeJSON:
            json.dump(data, writeJSON, ensure_ascii=False, indent=4)
