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
from ..items import CarmudiItem


class CarmudiSpider(scrapy.Spider):
    name = 'carmudi'
    page_number = 1
    allowed_domains = ['www.carmudi.vn']
    base_url = "https://www.carmudi.vn/mua-ban-o-to-cu/"
    start_urls = ['https://www.carmudi.vn/mua-ban-o-to-cu/']

    def __init__(self):
        super(CarmudiSpider, self).__init__()
        self.kafka = {'bootstrap.servers': '127.0.0.1:9092'}
        try:
            self.producer = Producer(**self.kafka)
        except:
            self.logger.error('Oto connect to kafka fail')

    def parse(self, response):
        all_ads = response.xpath('//a[@class="title is-5"]/@href').extract()
        for ad_url in all_ads:
            yield scrapy.Request(ad_url, callback=self.parse_ad)

    def parse_ad(self, response):
        item = {
            'id': str(uuid.uuid4()),
            'url': response.url,
            'crawled_date': datetime.now(),
            'domain': self.allowed_domains[0],
            'ten': ' '.join(response.xpath('//div[@class="pages-title"]//text()').extract()).lower().strip(),
            'gia_ban': response.xpath('//div[@class="price-tag"]/@data-price').get(),
        }

        features = response.xpath('//div[@class="feature-item"]//text()').extract()
        tmp = []
        for feature in features:
            feature = feature.strip()
            if len(feature) > 1:
                tmp.append(feature)
        feature_0 = tmp[0] + tmp[1]
        feature_1 = tmp[2] + tmp[3]
        tmp = tmp[4:]
        tmp.append(feature_0)
        tmp.append(feature_1)

        for feature in tmp:
            key, value = feature.split(':')
            key = unidecode(key.replace(":", "").replace(" ", "_").lower())
            item[key] = value.lower().strip()

        basic_information = response.xpath('//div[@id="area_basic_information"]//text()').extract()
        tmp = []
        for info in basic_information:
            info = info.strip()
            if len(info) >= 1:
                tmp.append(info)

        key = None
        for _, info in enumerate(tmp):
            if _ % 2 == 0:
                key = unidecode(info.replace(" ", "_").lower())
            else:
                item[key] = info.lower().strip()

        item['mo_ta'] = ' '.join(response.xpath('//div[@id="area_description"]//p//text()').extract()).strip()

        next_page = 'https://www.carmudi.vn/mua-ban-o-to-cu/index{}.html'.format(CarmudiSpider.page_number)
        if CarmudiSpider.page_number <= 10:
            CarmudiSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

        yield CarmudiItem(id=item.get('id'),
                          domain=item.get('domain'),
                          url=item.get('url'),
                          crawled_date=item.get('crawled_date'),
                          ten=item.get('ten'),
                          gia_ban=item.get('gia_ban'),
                          hang_xe=item.get('hang_xe'),
                          phien_ban=item.get('phien_ban'),
                          tinh_trang_xe=item.get('tinh_trang_xe'),
                          tinh_thanh=item.get('tinh/_thanh_pho'),
                          nhien_lieu=item.get('nhien_lieu'),
                          mau_ngoai_that=item.get('mau_ngoai_that'),
                          dong_xe=item.get('dong_xe'),
                          nam_san_xuat=item.get('nam_san_xuat'),
                          hop_so=item.get('hop_so'),
                          kieu_dang=item.get('kieu_dang'),
                          xuat_xu=item.get('xuat_xu'),
                          so_cua=item.get('so_cua'),
                          so_ghe_ngoi=item.get('so_ghe_ngoi'),
                          dong_co=item.get('dong_co'),
                          dung_tich_xi_lanh=item.get('dung_tich_xi_lanh_(cc)'),
                          dung_tich_binh_nhien_lieu=item.get('dung_tich_binh_nhien_lieu'),
                          dan_dong=item.get('dan_dong'),
                          mo_ta=item.get('mo_ta')
                          )
