# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from bonbanh.mediated_schema import MediatedOtoItem

class BonbanhItem(scrapy.Item):
    # gia = scrapy.Field()
    # dong_xe = scrapy.Field()
    # tinh_trang = scrapy.Field()
    # nhien_lieu = scrapy.Field()
    # # kieu_dang = scrapy.Field()
    # km_da_di = scrapy.Field()
    # hop_so = scrapy.Field()
    # xuat_xu = scrapy.Field()
    # so_cho_ngoi = scrapy.Field()
    # mau_xe = scrapy.Field()
    # so_cua = scrapy.Field()
    # mo_ta = scrapy.Field()
    thuoctinh_1 = scrapy.Field()
    thuoctinh_2 = scrapy.Field()
    thuoctinh_3 = scrapy.Field()
    thuoctinh_4 = scrapy.Field()
    thuoctinh_5 = scrapy.Field()
    thuoctinh_6 = scrapy.Field()
    thuoctinh_7 = scrapy.Field()
    thuoctinh_8 = scrapy.Field()
    thuoctinh_9 = scrapy.Field()
    thuoctinh_10 = scrapy.Field()
    thuoctinh_11 = scrapy.Field()

    def to_sql_record(self) -> str:
        v = MediatedOtoItem()
        v.gia_ban = self['thuoctinh_1']
        v.dong_xe = self['thuoctinh_2']
        v.tinh_trang = self['thuoctinh_3']
        v.nhien_lieu = self['thuoctinh_4']
        v.so_km_da_di = self['thuoctinh_5']
        v.hop_so = self['thuoctinh_6']
        v.xuat_xu = self['thuoctinh_7']
        v.so_cho_ngoi = self['thuoctinh_8']
        v.mau_noi_that = self['thuoctinh_9']
        v.so_cua = self['thuoctinh_10']
        return v.to_sql_record()

    pass
