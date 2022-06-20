from kafka import KafkaProducer

from urllib.request import urlopen
from lxml import etree

import sys

htmlparser = etree.HTMLParser()

base_url = 'https://bonbanh.com/'

def crawl_url(url, producer):
    print('[PRODUCER]:\t ', url)
    
    response = urlopen(url)
    
    tree = etree.parse(response, htmlparser)
    
    all_ads = tree.xpath('//li[contains(@class, "car-item")]')
    for ad in all_ads:
        ad_url = ad.xpath('.//a[contains(@itemprop, "url")]/@href')[0]
        ad_url = base_url + ad_url
        print('[SEND]:\t ', ad_url)
        producer.send('bonbanh', str.encode(ad_url))

    producer.flush()
    
def main():
    start_url = 'https://bonbanh.com/oto/page,'
    producer = KafkaProducer()
    for i in range(int(sys.argv[1])):
        crawl_url(start_url + str(i + 1), producer)
        producer.flush()
   
   
main()