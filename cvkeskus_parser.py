import requests
import json
from bs4 import BeautifulSoup as bs

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/53.0.2785.143 Safari/537.36 '}

base_url = 'https://www.cvkeskus.ee/joboffers.php?op=search&search%5Bkeyword%5D=&search%5Bexpires_days%5D=&search' \
           '%5Bjob_lang%5D=ru&search%5Bsalary%5D=&search%5Bjob_salary%5D=3&sort=activation_date&dir=1&start='

pages = [str(i) for i in range(1, 150, 29)]

data = []


def cvkeskus_parse():
    for page in pages:

        session = requests.Session()
        request = session.get(base_url + page, headers=headers)

        if request.status_code == 200:

            soup = bs(request.content, "lxml")

            offer_wrapper = soup.find(id='f_jobs_main')
            offers = offer_wrapper.find_all(class_='f_job_row2')

            for offer in offers:
                item = {}
                item['title'] = offer.find('a', attrs={'class': 'f_job_title'}).text
                item['firm_name'] = offer.find('span', attrs={'class': 'f_job_company'}).text
                raw_link = offer.find('a', attrs={'class': 'f_job_title'}).get('href')
                item['link'] = 'https://cvkeskus.ee' + raw_link
                item['date'] = offer.find('div', attrs={'class': 'time-left-block'}).text
                item['site'] = 'Cvkeskus'
                data.append(item)

                print("title: " + item['title'])
                print("firm_name: " + item['firm_name'])
                print("link: " + item['link'])
                print("date: " + item['date'])
                print("site: " + item['site'])

            with open("cvkeskus.json", "w", encoding='utf8') as writeJSON:
                json.dump(data, writeJSON, ensure_ascii=False, indent=4)


cvkeskus_parse()
