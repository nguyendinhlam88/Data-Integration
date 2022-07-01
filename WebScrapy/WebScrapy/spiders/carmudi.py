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
    start_urls = ['http://www.carmudi.vn/']

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
        # item = CarmudiItem()
        item = {
        'id' : str(uuid.uuid4()),
        'url' : response.url,
        'crawled_date' : datetime.now(), 
        'domain' :self.allowed_domains[0],
        'ten' : response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "pages-title-name-detail", " " ))]/text()').extract_first().strip(),
        'gia': response.xpath('//div[@class="price-tag"]/@data-price').get(),
        'nam_san_xuat':  response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "feature-item", " " )) and (((count(preceding-sibling::*) + 1) = 4) and parent::*)]//text()').extract()[
            1].replace('\n', '').replace('Năm sản xuất: ', ''),
        'xuat_xu' : response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "feature-item", " " )) and (((count(preceding-sibling::*) + 1) = 12) and parent::*)]//text()').extract()[
            1].replace('\n', '').replace('Xuất xứ: ', ''),
        'tinh_trang' :response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "feature-item", " " )) and (((count(preceding-sibling::*) + 1) = 5) and parent::*)]//text()').extract()[
            1].replace('\n', '').replace('Tình trạng xe: ', ''),
        'dong_xe' :response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "feature-item", " " )) and (((count(preceding-sibling::*) + 1) = 2) and parent::*)]//span/text()').extract()[
            0],
        'mau_xe': response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "feature-item", " " )) and (((count(preceding-sibling::*) + 1) = 11) and parent::*)]//text()').extract()[
            1].replace('\n', '').replace('Màu ngoại thất: ', ''),
        'so_cua': response.xpath('//*[(@id = "area_basic_information")]//*[contains(concat( " ", @class, " " ), concat( " ", "value", " " ))]/text()').extract()[1],
        'so_cho_ngoi': response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "feature-item", " " )) and (((count(preceding-sibling::*) + 1) = 10) and parent::*)]//text()').extract()[
            1].replace('\n', '').replace('Số ghế ngồi: ', ''),
        'nhien_lieu' :response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "feature-item", " " )) and (((count(preceding-sibling::*) + 1) = 9) and parent::*)]//text()').extract()[
            1].replace('\n', '').replace('Nhiên liệu: ', ''),
        'hop_so' :response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "feature-item", " " )) and (((count(preceding-sibling::*) + 1) = 6) and parent::*)]//text()').extract()[
            1].replace('\n', '').replace('Hộp số: ', ''),
        'dung_tich_xi_lanh': response.xpath('//*[(@id = "area_basic_information")]//*[contains(concat( " ", @class, " " ), concat( " ", "value", " " ))]/text()').extract()[10]
        }

        next_page = 'https://www.carmudi.vn/mua-ban-o-to-cu/index{}.html'.format(CarmudiSpider.page_number)
        if CarmudiSpider.page_number <= 10:
            CarmudiSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
        
        yield   CarmudiItem(id=item.get('id'),
                            domain=item.get('domain'),
                            url=item.get('url'),
                            crawled_date=item.get('crawled_date'),
                            ten=item.get('ten'),
                            gia_ban=item.get('gia'),
                            nam_san_xuat= item.get('nam_san_xuat'),
                            xuat_xu=item.get('xuat_xu'),
                            tinh_trang=item.get('tinh_trang'),
                            dong_xe=item.get('dong_xe'),
                            so_km_da_di=None,
                            mau_ngoai_that=item.get('mau_xe'),
                            mau_noi_that=None,
                            so_cua=item.get('so_cua'),
                            so_cho_ngoi=item.get('so_cho_ngoi'),
                            nhien_lieu=item.get('nhien_lieu'),
                            he_thong_nap_nhien_lieu=None,
                            hop_so=item.get('hop_so'),
                            dan_dong= None,
                            tieu_thu_nhien_lieu=None, 
                            dung_tich_xi_lanh=item.get('dung_tich_xi_lanh'),
                            thong_tin_mo_ta=None
                        )
