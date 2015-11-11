from pyquery import PyQuery as Pq
import requests
import random
import time
import re


def crawl(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}
    cookies = {'_ts_id': ''}
    uid = re.search('\d{5,}', url).group()
    page = 1
    qa = []
    while True:
        url = 'http://goods.ruten.com.tw/item/qa_full?{uid}&page={page}'.format(uid=uid, page=page)
        print(url)
        resp = requests.get(url, headers=headers, cookies=cookies)
        raw = resp.content.decode('cp950')
        dom = Pq(raw)
        eles = dom('.q,.a')
        if eles:
            qa += [i.text() for i in eles.items()]
            page += 1
            time.sleep(random.random() * 0.5)
        else:
            return qa
