import scrapy
import uuid
import re

import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from urllib3.connectionpool import log

log.setLevel(logging.WARNING)
LOGGER.setLevel(logging.WARNING)

from unidecode import unidecode
from datetime import datetime
from confluent_kafka import Producer
from ..items import BonBanhItem


class BonbanhSpider(scrapy.Spider):
    name = 'bonbanh'
    page_number = 1
    allowed_domains = ['bonbanh.com']
    base_url = "https://bonbanh.com/"
    start_urls = ["https://bonbanh.com/oto/page,2"]

    def __init__(self):
        super(BonbanhSpider, self).__init__()
        self.kafka = {'bootstrap.servers': '127.0.0.1:9092'}
        try:
            self.producer = Producer(**self.kafka)
        except:
            self.logger.error('Oto connect to kafka fail')

    def parse(self, response):
        all_ads = response.xpath('//li[contains(@class, "car-item")]')
        for ad in all_ads:
            ad_url = ad.xpath('.//a[contains(@itemprop, "url")]/@href').extract_first()
            ad_url = self.base_url + ad_url
            yield scrapy.Request(ad_url, callback=self.parse_ad)

    def parse_ad(self, response):
        ten_gia = response.xpath('//h1/text()').extract_first().split('-')
        info = response.xpath('//span[@class = "inp"]')
        dong_co = info[8].xpath('.//text()').extract_first().lower()
        item = {
            'id': str(uuid.uuid4()),
            'url': response.url,
            'crawled_date': datetime.now(),
            'domain': self.allowed_domains[0],
            'ten': ' '.join(ten_gia[:-1]).strip().lower(),
            'gia': ten_gia[-1].strip().lower(),
            'xuat_xu': info[0].xpath('.//text()').extract_first().lower(),
            'tinh_trang': info[1].xpath('.//text()').extract_first().lower(),
            'dong_xe': info[2].xpath('.//text()').extract_first().lower(),
            'so_km_da_di': info[3].xpath('.//text()').extract_first().lower(),
            'mau_ngoai_that': info[4].xpath('.//text()').extract_first().lower(),
            'mau_noi_that': info[5].xpath('.//text()').extract_first().lower(),
            'so_cua': info[6].xpath('.//text()').extract_first().lower(),
            'so_cho_ngoi': info[7].xpath('.//text()').extract_first().lower(),
            'nhien_lieu': dong_co.split()[0].lower(),
            'he_thong_nap_nhien_lieu': info[9].xpath('.//text()').extract_first().lower() if info[9].xpath('.//text()').extract_first() else None,
            'hop_so': info[10].xpath('.//text()').extract_first().lower().strip(),
            'dan_dong': info[11].xpath('.//text()').extract_first().lower(),
            'tieu_thu_nhien_lieu': info[12].xpath('.//text()').extract_first().lower(),
            'dung_tich_xi_lanh': ' '.join(dong_co.split()[1:]).lower(),
            'thong_tin_mo_ta': response.xpath('//div[@class="des_txt"]//text()').extract_first()
        }
        next_page = 'https://bonbanh.com/oto/page,' + str(BonbanhSpider.page_number)
        if BonbanhSpider.page_number <= 5000:
            BonbanhSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
        yield BonBanhItem(id=item.get('id'),
                          domain=item.get('domain'),
                          url=item.get('url'),
                          crawled_date=item.get('crawled_date'),
                          ten=item.get('ten'),
                          gia_ban=item.get('gia'),
                          nam_san_xuat=None,
                          xuat_xu=item.get('xuat_xu'),
                          tinh_trang=item.get('tinh_trang'),
                          dong_xe=item.get('dong_xe'),
                          so_km_da_di=item.get('so_km_da_di'),
                          mau_ngoai_that=item.get('mau_ngoai_that'),
                          mau_noi_that=item.get('mau_noi_that'),
                          so_cua=item.get('so_cua'),
                          so_cho_ngoi=item.get('so_cho_ngoi'),
                          nhien_lieu=item.get('nhien_lieu'),
                          he_thong_nap_nhien_lieu=item.get('he_thong_nap_nhien_lieu'),
                          hop_so=item.get('hop_so'),
                          dan_dong=item.get('dan_dong'),
                          tieu_thu_nhien_lieu=item.get('tieu_thu_nhien_lieu'),
                          dung_tich_xi_lanh=item.get('dung_tich_xi_lanh'),
                          thong_tin_mo_ta=item.get('thong_tin_mo_ta')
                          )
