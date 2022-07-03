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
from ..items import OtoItem


class OtoSpider(scrapy.Spider):
    name = 'oto'
    allowed_domains = ['oto.com.vn']
    start_urls = ['https://oto.com.vn/mua-ban-xe']
    last_url = None

    def __init__(self):
        super(OtoSpider, self).__init__()
        self.kafka = {'bootstrap.servers': '127.0.0.1:9092'}
        try:
            self.producer = Producer(**self.kafka)
        except:
            self.logger.error('Oto connect to kafka fail')

    def parse(self, response):
        items_url = response.xpath('//div[@class="photo"]//@href').extract()
        if self.last_url == items_url[-1]:
            return
        for url in items_url:
            if "www" in url:
                continue
            absolute_path = response.urljoin(url)
            yield scrapy.Request(absolute_path, callback=self.parse_oto)
        self.last_url = items_url[-1]
        if response.url.split('/')[-1][0] != 'p':
            next_page = self.start_urls[0] + '/p2?_' + str(int(datetime.now().timestamp()))
            yield scrapy.Request(next_page, callback=self.parse)
        else:
            current_page = re.sub(r'\D', '', response.url.split('/')[-1].split('?')[0])
            next_page = self.start_urls[0] + f'/p{int(current_page) + 1}?_' + str(int(datetime.now().timestamp()))
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_oto(self, response):
        item = {"id": str(uuid.uuid4()),
                "domain": self.allowed_domains[0],
                "url": response.url,
                "crawled_date": datetime.now(),
                "anh_xe": response.xpath('//div[@class="swiper-wrapper"]//@src').extract_first(),
                "ten": response.xpath('//h1[@class="title-detail"]/text()').extract_first().lower().strip(),
                "gia_ban": ' '.join(response.xpath('//span[contains(@class, "price-big")]/text()').extract()).strip().lower(),
                "gia_lan_banh": response.xpath('//span[@id="chiphilanbanh"]//text()').extract()[-1].lower()
                }
        tmp = response.xpath('//div[@class="box-info-detail"]//ul[@class="list-info"]//li//text()').extract()
        thong_so_ky_thuat = []
        for _ in tmp:
            _ = _.strip()
            if len(_) > 1:
                thong_so_ky_thuat.append(_)
        key = None
        for _, tmp in enumerate(thong_so_ky_thuat):
            if _ % 2 == 0:
                key = unidecode(tmp.replace(" ", "_").lower())
            else:
                item[key] = tmp.lower()

        # Mô tả
        tmp = ' '.join(response.xpath('.//div[@id="tab-desc"]//text()').extract()).strip()
        item["mo_ta"] = tmp

        yield OtoItem(id=item.get('id'),
                      domain=item.get('domain'),
                      url=item.get('url'),
                      crawled_date=item.get('crawled_date'),
                      anh_xe=item.get('anh_xe'),
                      ten=item.get('ten'),
                      gia_ban=item.get('gia_ban'),
                      gia_lan_banh=item.get('gia_lan_banh'),
                      nam_san_xuat=item.get('nam_san_xuat'),
                      kieu_dang=item.get('kieu_dang'),
                      tinh_trang=item.get('tinh_trang'),
                      xuat_xu=item.get('xuat_xu'),
                      tinh_thanh=item.get('tinh_thanh'),
                      quan_huyen=item.get('quan_huyen'),
                      hop_so=item.get('hop_so'),
                      nhien_lieu=item.get('nhien_lieu'),
                      mo_ta=item.get('mo_ta')
                      )
