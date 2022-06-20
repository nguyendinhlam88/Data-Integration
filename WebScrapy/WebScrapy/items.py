# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BonbanhItem(scrapy.Item):
    gia = scrapy.Field()
    # hang = scrapy.Field()
    dong_xe = scrapy.Field()
    # nam_sx = scrapy.Field()
    tinh_trang = scrapy.Field()
    nhien_lieu = scrapy.Field()
    kieu_dang = scrapy.Field()
    dong_xe = scrapy.Field()
    km_da_di = scrapy.Field()
    hop_so = scrapy.Field()
    xuat_xu = scrapy.Field()
    so_cho_ngoi = scrapy.Field()
    mau_xe = scrapy.Field()
    so_cua = scrapy.Field()
    pass


class ChototItem(scrapy.Item):
    gia = scrapy.Field()
    hang = scrapy.Field()
    dong_xe = scrapy.Field()
    nam_sx = scrapy.Field()
    tinh_trang = scrapy.Field()
    nhien_lieu = scrapy.Field()
    kieu_dang = scrapy.Field()
    dong_xe = scrapy.Field()
    km_da_di = scrapy.Field()
    hop_so = scrapy.Field()
    xuat_xu = scrapy.Field()
    so_cho_ngoi = scrapy.Field()
    pass


class CarmudiItem(scrapy.Item):
    gia = scrapy.Field()
    dong_xe = scrapy.Field()
    tinh_trang = scrapy.Field()
    nhien_lieu = scrapy.Field()
    # kieu_dang = scrapy.Field()
    km_da_di = scrapy.Field()
    hop_so = scrapy.Field()
    xuat_xu = scrapy.Field()
    so_cho_ngoi = scrapy.Field()
    mau_xe = scrapy.Field()
    so_cua = scrapy.Field()
    mo_ta = scrapy.Field()
