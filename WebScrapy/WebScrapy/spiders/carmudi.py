import scrapy
from pkg_resources import yield_lines
from ..items import CarmudiItem
from datetime import datetime
import uuid

class CarmudiSpider(scrapy.Spider):
    name = 'carmudi'
    page_number = 1
    allowed_domains = ['www.carmudi.vn']
    base_url = "https://www.carmudi.vn/mua-ban-o-to-cu/"
    start_urls = ['http://www.carmudi.vn/']

    def parse(self, response):
        all_ads = response.xpath('//a[@class="title is-5"]/@href').extract()
        for ad_url in all_ads:
            yield scrapy.Request(ad_url, callback=self.parse_ad)

    def parse_ad(self, response):
        item = CarmudiItem()
        item['id'] = str(uuid.uuid4())
        item['url'] = response.url
        item['crawled_date'] = datetime.now()
        item['domain'] = self.allowed_domains[0]
        item['gia'] = response.xpath('//div[@class="price-tag"]/@data-price').get()
        item['dong_xe'] = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "feature-item", " " )) and (((count(preceding-sibling::*) + 1) = 2) and parent::*)]//span/text()').extract()[
            0]
        item['tinh_trang'] = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "feature-item", " " )) and (((count(preceding-sibling::*) + 1) = 5) and parent::*)]//text()').extract()[
            1].replace('\n', '').replace('Tình trạng xe: ', '')
        item['nhien_lieu'] = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "feature-item", " " )) and (((count(preceding-sibling::*) + 1) = 9) and parent::*)]//text()').extract()[
            1].replace('\n', '').replace('Nhiên liệu: ', '')
        item['hop_so'] = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "feature-item", " " )) and (((count(preceding-sibling::*) + 1) = 6) and parent::*)]//text()').extract()[
            1].replace('\n', '').replace('Hộp số: ', '')
        item['xuat_xu'] = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "feature-item", " " )) and (((count(preceding-sibling::*) + 1) = 12) and parent::*)]//text()').extract()[
            1].replace('\n', '').replace('Xuất xứ: ', '')
        item['so_cho_ngoi'] = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "feature-item", " " )) and (((count(preceding-sibling::*) + 1) = 10) and parent::*)]//text()').extract()[
            1].replace('\n', '').replace('Số ghế ngồi: ', '')
        item['mau_xe'] = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "feature-item", " " )) and (((count(preceding-sibling::*) + 1) = 11) and parent::*)]//text()').extract()[
            1].replace('\n', '').replace('Màu ngoại thất: ', '')
        item['nam_sx'] = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "feature-item", " " )) and (((count(preceding-sibling::*) + 1) = 4) and parent::*)]//text()').extract()[
            1].replace('\n', '').replace('Năm sản xuất: ', '')
        # item['mo_ta'] = response.xpath('//*[(@id = "area_description")]//p/text()').extract()
        next_page = 'https://www.carmudi.vn/mua-ban-o-to-cu/index{}.html'.format(CarmudiSpider.page_number)
        if CarmudiSpider.page_number <= 25:
            CarmudiSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
        yield item
