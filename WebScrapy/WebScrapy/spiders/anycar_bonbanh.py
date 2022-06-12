import scrapy
import requests
import re
from unidecode import unidecode
from bs4 import BeautifulSoup
from math import ceil


class AnycarBonbanhSpider(scrapy.Spider):
    name = 'anycar_bonbanh'
    allowed_domains = ['anycar.bonbanh.com']
    start_urls = ['https://anycar.bonbanh.com/xe-dang-ban/']

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
        item = {"ten_xe": response.xpath('//a[@itemprop="item"]/@title').extract()[-1],
                "gia": response.xpath('//div[@class="price_list_car"]//b/text()').extract_first()}
        tab_left = response.xpath('//div[@id="tab1default"]//div[@class="tab_left_item row"]')
        for thong_so in tab_left:
            key, value = thong_so.xpath('.//*//text()').extract()
            key = unidecode(key[:-1].replace(" ", "_").lower())
            item[key] = value
        tab_right = response.xpath('//div[@id="tab1default"]//div[@class="tab_right_item row"]')
        for thong_so in tab_right:
            tmp = thong_so.xpath('.//*//text()').extract()
            key, value = tmp if len(tmp) == 2 else tmp + [None]
            key = unidecode(key[:-1].replace(" ", "_").lower())
            item[key] = value
        yield item
