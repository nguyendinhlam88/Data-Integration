import scrapy
import uuid
import re
from unidecode import unidecode
from datetime import datetime


class OtoSpider(scrapy.Spider):
    name = 'oto'
    allowed_domains = ['oto.com.vn']
    start_urls = ['https://oto.com.vn/mua-ban-xe']
    last_url = None

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
                "ten": response.xpath('//h1[@class="title-detail"]/text()').extract_first().strip(),
                "gia_ban": ' '.join(response.xpath('//span[contains(@class, "price-big")]/text()').extract()).strip(),
                "gia_lan_banh": response.xpath('//span[@id="chiphilanbanh"]//text()').extract()[-1]
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
                item[key] = tmp

        # Mô tả
        tmp = ' '.join(response.xpath('.//div[@id="tab-desc"]//text()').extract()).strip()
        # item["mo_ta"] = tmp
        yield item
