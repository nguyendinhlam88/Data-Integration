import scrapy
import requests
import re
import uuid

import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from urllib3.connectionpool import log

log.setLevel(logging.WARNING)
LOGGER.setLevel(logging.WARNING)

from datetime import datetime
from unidecode import unidecode
from bs4 import BeautifulSoup
from math import ceil
from confluent_kafka import Producer
from ..items import AnyCarBonBanhItem


class AnycarBonbanhSpider(scrapy.Spider):
    name = 'anycar_bonbanh'
    allowed_domains = ['anycar.bonbanh.com']
    start_urls = ['https://anycar.bonbanh.com/xe-dang-ban/']

    def __init__(self):
        super(AnycarBonbanhSpider, self).__init__()
        self.kafka = {'bootstrap.servers': '127.0.0.1:9092'}
        try:
            self.producer = Producer(**self.kafka)
        except:
            self.logger.error('Anycar connect to kafka fail')

    def parse(self, response):
        page = 1
        soup = BeautifulSoup(requests.get("https://anycar.bonbanh.com/").content, 'html.parser')
        max_car = int(re.sub(r"\D", "", soup.find("div", id="total_car_number").text))
        max_page = ceil(max_car / 18)
        api_url = "https://anycar.bonbanh.com/view-salon-ajax/"
        while page <= max_page:
            body = f"number_page_new={page}&ajax=1"
            yield scrapy.Request(api_url,
                                 method="POST",
                                 headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"},
                                 body=body,
                                 callback=self.get_item_info)
            page += 1

    def get_item_info(self, response):
        url_items = response.xpath('//div[@class="item_title"]//@href').extract()
        for item_url in url_items:
            yield scrapy.Request(item_url, callback=self.parse_item)

    def parse_item(self, response):
        item = {"id": str(uuid.uuid4()),
                "domain": self.allowed_domains[0],
                "url": response.url,
                "crawled_date": datetime.now(),
                "ten": response.xpath('//a[@itemprop="item"]/@title').extract()[-1].lower(),
                "gia_ban": response.xpath('//div[@class="price_list_car"]//b/text()').extract_first().lower()}

        tab_left = response.xpath('//div[@id="tab1default"]//div[@class="tab_left_item row"]')
        for thong_so in tab_left:
            tmp = thong_so.xpath('.//*//text()').extract()
            key, value = tmp if len(tmp) == 2 else tmp + [None]
            key = unidecode(key.replace(":", "").replace(" ", "_").lower())
            item[key] = value.lower().strip() if value else None

        tab_right = response.xpath('//div[@id="tab1default"]//div[@class="tab_right_item row"]')
        for thong_so in tab_right:
            tmp = thong_so.xpath('.//*//text()').extract()
            key, value = tmp if len(tmp) == 2 else tmp + [None]
            key = unidecode(key.replace(":", "").replace(" ", "_").lower())
            item[key] = value.lower().strip() if value else None
        # Dung tích xi lanh
        tab_left_final = response.xpath('//div[@class="tab_left_item row"]')[-1]
        tmp = tab_left_final.xpath('.//*//text()').extract()
        key, value = tmp if len(tmp) == 2 else tmp + [None]
        key = unidecode(key[:-1].strip().replace(" ", "_").lower())
        item[key] = value
        # Mô tả
        tmp = response.xpath('.//div[@class="col-md-12 col-xs-12 tab_bottom"]//div//text()').extract()
        key, value = tmp[0], ' '.join(tmp[1:]).strip()
        key = unidecode(key.replace(":", "").replace(" ", "_").lower())
        item[key] = value
        yield AnyCarBonBanhItem(id=item.get('id'),
                                domain=item.get('domain'),
                                url=item.get('url'),
                                crawled_date=item.get('crawled_date'),
                                ten=item.get('ten'),
                                gia_ban=item.get('gia_ban'),
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
