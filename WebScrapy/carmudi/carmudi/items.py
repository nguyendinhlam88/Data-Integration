# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from turtle import Screen
import scrapy

from carmudi.mediated_schema import MediatedOtoItem

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
    # thuoctinh_1 = scrapy.Field()
    # thuoctinh_2 = scrapy.Field()
    # thuoctinh_3 = scrapy.Field()
    # thuoctinh_4 = scrapy.Field()
    # thuoctinh_5 = scrapy.Field()
    # thuoctinh_6 = scrapy.Field()
    # thuoctinh_7 = scrapy.Field()
    # thuoctinh_8 = scrapy.Field()
    # thuoctinh_9 = scrapy.Field()
    # thuoctinh_10 = scrapy.Field()
    # thuoctinh_11 = scrapy.Field()

    def to_sql_record(self) -> str:
        v = MediatedOtoItem()
        v.gia_ban = self['gia']
        v.dong_xe = self['dong_xe']
        v.tinh_trang = self['tinh_trang']
        v.nhien_lieu = self['nhien_lieu']
        v.so_km_da_di = self['so_km_da_di']
        v.hop_so = self['hop_so']
        v.xuat_xu = self['xuat_xu']
        v.so_cho_ngoi = self['tso_cho_ngoi']
        v.mau_noi_that = self['mau_xe']
        v.so_cua = self['so_cua']
        return v.to_sql_record()

    pass
