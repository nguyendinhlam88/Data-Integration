from kafka import KafkaConsumer

from urllib.request import urlopen
from urllib import parse
from urllib.parse import unquote

from lxml import etree
from lxml import html

import html as _html

import lxml.html.clean as clean

import json

import requests

from filelock import Timeout, FileLock

htmlparser = etree.HTMLParser(encoding='utf-8')


lock_path = 'lock.txt.lock'
lock = FileLock(lock_path, timeout=1)

def post_process_str(s):
    return s.replace('\\t', ' ')
    
def parse_item_url(url):
    print('[CONSUMER]:\t ', url)

    #tree = clean.clean_html(html.fromstring(_html.unescape(requests.get(url).content)))
    response = urlopen(url)
    #print(response)
    
    tree = etree.parse(response, htmlparser) 
    item = dict()
    item['gia'] = tree.xpath('//h1/text()')[0]
    info = tree.xpath('//span[@class = "inp"]')
    item['xuat_xu'] = info[0].xpath('.//text()')[0]
    item['tinh_trang'] = info[1].xpath('.//text()')[0]
    item['dong_xe'] = info[2].xpath('.//text()')[0]
    item['km_da_di'] = info[3].xpath('.//text()')[0]
    item['mau_xe'] = info[4].xpath('.//text()')[0]
    item['so_cua'] = info[6].xpath('.//text()')[0]
    item['so_cho_ngoi'] = info[7].xpath('.//text()')[0]
    item['nhien_lieu'] = info[8].xpath('.//text()')[0]
    item['hop_so'] = info[10].xpath('.//text()')[0]
    
    #for k, v in item.items():
    #    item[k] = post_process_str(v)
    
    return item


def main():
    f = open('results.json', 'a', encoding='utf-8')
    consumer = KafkaConsumer('bonbanh')
    for msg in consumer:
        #print(msg.value.decode('utf-8'))
        item = parse_item_url(msg.value.decode('utf-8'))
        
        lock.acquire()
        
        f.write(post_process_str(json.dumps(item, indent=2, ensure_ascii=False).encode('utf8').decode()))
        f.write(',\n')
        
        lock.release()
    
    f.close()
      
main()
#f = open('test.txt', 'w', encoding='utf-8')
#item = parse_item_url('https://bonbanh.com/xe-volkswagen-passat-1.8tsi-2016-4294468')
#print(f.write(post_process_str(json.dumps(item, indent=2, ensure_ascii=False).encode('utf8').decode())))