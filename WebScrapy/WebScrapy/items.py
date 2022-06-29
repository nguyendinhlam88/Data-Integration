# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from typing import Optional, List
from dataclasses import dataclass
import datetime

from typing import Optional, List
from dataclasses import dataclass
import datetime


@dataclass
class OtoItem:
    id: Optional[str]
    domain: Optional[str]
    url: Optional[str]
    crawled_date: Optional[datetime.date]
    ten: Optional[str]
    gia_ban: Optional[str]
    gia_lan_banh: Optional[str]
    nam_san_xuat: Optional[int]
    kieu_dang: Optional[str]
    tinh_trang: Optional[str]
    xuat_xu: Optional[int]
    tinh_thanh: Optional[str]
    quan_huyen: Optional[str]
    hop_so: Optional[str]
    nhien_lieu: Optional[str]

    def normalize_ten(self, ten: str) -> str:
        ten = ten.lower()
        ten = ' '.join(ten.split('-')[:-1]).strip()
        splitted_ten = ten.split()
        if splitted_ten[-2] == 'at':
            return ' '.join(splitted_ten[:-2])
        else:
            return ' '.join(splitted_ten[:-1])

    def normalize_gia(self, gia: str) -> int:
        gia_normalized = 0
        gia_splitted = gia.split()
        if len(gia_splitted) == 2 and gia_splitted[1] == 'triệu':
            gia_normalized = float(gia_splitted[0]) * 1e6
        elif len(gia_splitted) == 4 and gia_splitted[1] == 'tỉ' and gia_splitted[3] == 'triệu':
            gia_normalized = float(gia_splitted[0]) * 1e9 + float(gia_splitted[2]) * 1e6
        return gia_normalized

    def __post_init__(self):
        self.ten = self.normalize_ten(self.ten)
        self.gia_ban = self.normalize_gia(self.gia)
        self.gia_lan_banh = self.normalize_gia(self.gia_lan_banh)
        self.kieu_dang = self.kieu_dang.lower()
        self.tinh_trang = self.tinh_trang.lower().replace('đã qua sử dụng', 'cũ')
        self.xuat_xu = self.xuat_xu.lower()
        self.tinh_thanh = self.tinh_thanh.lower().replace('tp.hcm', 'thành phố hồ chí minh')
        self.quan_huyen = self.quan_huyen.lower()
        self.hop_so = self.hop_so.lower().replace('số', '')
        self.nhien_lieu = self.nhien_lieu.lower()


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
    crawled_date = scrapy.Field()
    domain = scrapy.Field()
    url = scrapy.Field()
    id = scrapy.Field()
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
    crawled_date = scrapy.Field()
    domain = scrapy.Field()
    url = scrapy.Field()
    id = scrapy.Field()
    pass


class CarmudiItem(scrapy.Item):
    gia = scrapy.Field()
    hang = scrapy.Field()
    dong_xe = scrapy.Field()
    nam_sx = scrapy.Field()
    tinh_trang = scrapy.Field()
    nhien_lieu = scrapy.Field()
    kieu_dang = scrapy.Field()
    dong_xe = scrapy.Field()
    # km_da_di = scrapy.Field()
    hop_so = scrapy.Field()
    xuat_xu = scrapy.Field()
    so_cho_ngoi = scrapy.Field()
    crawled_date = scrapy.Field()
    domain = scrapy.Field()
    url = scrapy.Field()
    id = scrapy.Field()
    pass
