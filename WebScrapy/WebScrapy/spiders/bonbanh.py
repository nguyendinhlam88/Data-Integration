import scrapy
# from ..items import BonbanhItem
from datetime import datetime
import uuid
class BonbanhSpider(scrapy.Spider):
    name = 'bonbanh'
    page_number = 1
    allowed_domains = ['bonbanh.com']
    base_url = "https://bonbanh.com/"
    start_urls = ["https://bonbanh.com/oto/page,2"]

    def parse(self, response):
        all_ads = response.xpath('//li[contains(@class, "car-item")]')
        for ad in all_ads:
            ad_url = ad.xpath('.//a[contains(@itemprop, "url")]/@href').extract_first()
            ad_url = self.base_url + ad_url
            yield scrapy.Request(ad_url, callback=self.parse_ad)

    def parse_ad(self, response):
        # item = BonbanhItem()
        # item['id'] = str(uuid.uuid4())
        # item['domain'] = self.allowed_domains[0]
        # item['url'] = response.url
        # item['crawled_date'] = datetime.now()
        ten_gia = response.xpath('//h1/text()').extract_first().split('-')
        info = response.xpath('//span[@class = "inp"]')
        # item['xuat_xu'] = info[0].xpath('.//text()').extract_first()
        # item['tinh_trang'] = info[1].xpath('.//text()').extract_first()
        # item['dong_xe'] = info[2].xpath('.//text()').extract_first()
        # item['km_da_di'] = info[3].xpath('.//text()').extract_first()
        # item['mau_xe'] = info[4].xpath('.//text()').extract_first()
        # item['so_cua'] = info[6].xpath('.//text()').extract_first()
        # item['so_cho_ngoi'] = info[7].xpath('.//text()').extract_first()
        # item['nhien_lieu'] = info[8].xpath('.//text()').extract_first()
        # item['hop_so'] = info[10].xpath('.//text()').extract_first()
        item = {
        'id' : str(uuid.uuid4()),
        'url' : response.url,
        'crawled_date' : datetime.now(), 
        'domain' :self.allowed_domains[0],
        'ten' :ten_gia[0],
        'gia': ten_gia[1],
        'xuat_xu' : info[0].xpath('.//text()').extract_first(),
        'tinh_trang' : info[1].xpath('.//text()').extract_first(),
        'dong_xe' : info[2].xpath('.//text()').extract_first(),
        'mau_xe': info[4].xpath('.//text()').extract_first(),
        'so_cua': info[6].xpath('.//text()').extract_first(),
        'so_cho_ngoi': info[7].xpath('.//text()').extract_first(),
        'nhien_lieu' : info[8].xpath('.//text()').extract_first(),
        'hop_so' : info[10].xpath('.//text()').extract_first()
        }
        next_page = 'https://bonbanh.com/oto/page,' + str(BonbanhSpider.page_number)
        if BonbanhSpider.page_number <= 15:
            BonbanhSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
        yield item
