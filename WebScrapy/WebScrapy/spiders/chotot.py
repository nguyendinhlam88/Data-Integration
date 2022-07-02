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
from ..items import ChototItem


class ChototSpider(scrapy.Spider):
    name = 'chotot'
    page_number = 2
    allowed_domains = ['xe.chotot.com']
    base_url = "https://xe.chotot.com"
    start_urls = ["https://xe.chotot.com/mua-ban-o-to?page=1"]

    def __init__(self):
        super(ChototSpider, self).__init__()
        self.kafka = {'bootstrap.servers': '127.0.0.1:9092'}
        try:
            self.producer = Producer(**self.kafka)
        except:
            self.logger.error('Oto connect to kafka fail')

    def parse(self, response):
        all_ads = response.xpath('//li[contains(@class, "AdItem")]').xpath(
            './/a[contains(@class, "AdItem")]/@href').extract()

        for ad_url in all_ads:
            ad_url = self.base_url + ad_url
            yield scrapy.Request(url=ad_url, callback=self.parse_ad)

    def parse_ad(self, response):
        item = {
            'id': str(uuid.uuid4()),
            'url': response.url,
            'crawled_date': datetime.now(),
            'domain': self.allowed_domains[0],
            'ten': response.xpath(
                '//*[contains(concat( " ", @class, " " ), concat( " ", "AdDecription_adTitle__2I0VE", " " ))]/text()').extract()[
                1].lower(),
            'gia': response.xpath('//span[contains(@itemprop, "price")]/text()').extract_first().replace(' đ', '').lower(),
        }

        basic_information = response.xpath('//div[@data-testid="param-item"]//text()').extract()
        key = None
        for _, info in enumerate(basic_information):
            if _ % 2 == 0:
                key = unidecode(info.replace(":", "").strip().replace(" ", "_").lower())
            else:
                item[key] = info.lower()

        item['mo_ta'] = response.xpath('//p[@itemprop="description"]//text()').extract_first()

        next_page = 'https://xe.chotot.com/mua-ban-o-to-o-to-dien?page=' + str(ChototSpider.page_number)
        if ChototSpider.page_number <= 15:
            ChototSpider.page_number += 1
            yield response.follow(url=next_page, callback=self.parse)

        yield ChototItem(id=item.get('id'),
                         domain=item.get('domain'),
                         url=item.get('url'),
                         crawled_date=item.get('crawled_date'),
                         ten=item.get('ten'),
                         gia_ban=item.get('gia'),
                         hang=item.get('hang'),
                         nam_san_xuat=item.get('nam_san_xuat'),
                         tinh_trang=item.get('tinh_trang'),
                         nhien_lieu=item.get('nhien_lieu'),
                         kieu_dang=item.get('kieu_dang'),
                         dong_xe=item.get('dong_xe'),
                         so_km_da_di=item.get('so_km_da_di'),
                         hop_so=item.get('hop_so'),
                         xuat_xu=item.get('xuat_xu'),
                         so_cho=item.get('so_cho'),
                         mo_ta=item.get('mo_ta')
                         )
