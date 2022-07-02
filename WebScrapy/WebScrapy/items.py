# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from dataclasses import dataclass
from typing import Optional, List
from dataclasses import dataclass
from datetime import datetime


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
    mo_ta: Optional[str]

    def normalize_ten(self, ten: str) -> str:
        ten = ' '.join(ten.split('-')[:-1]).strip()
        splitted_ten = ten.split()
        if splitted_ten:
            if len(splitted_ten) >= 2 and splitted_ten[-2] == 'at':
                return ' '.join(splitted_ten[:-2])
            else:
                return ' '.join(splitted_ten[:-1])
        return None

    def normalize_gia(self, gia: str) -> int:
        gia_normalized = 0
        gia_splitted = gia.split()
        if len(gia_splitted) == 2 and gia_splitted[1] == 'triệu':
            gia_normalized = float(gia_splitted[0]) * 1e6
        elif len(gia_splitted) == 4 and gia_splitted[1] == 'tỉ' and gia_splitted[3] == 'triệu':
            gia_normalized = float(gia_splitted[0]) * 1e9 + float(gia_splitted[2]) * 1e6
        return gia_normalized

    def __post_init__(self):
        self.crawled_date = str(datetime.timestamp(self.crawled_date))
        self.ten = self.normalize_ten(self.ten) if isinstance(self.ten, str) else None
        self.gia_ban = self.normalize_gia(self.gia_ban)
        self.gia_lan_banh = self.normalize_gia(self.gia_lan_banh)
        self.tinh_trang = self.tinh_trang.replace('đã qua sử dụng', 'cũ') if isinstance(self.tinh_trang,
                                                                                        str) else None
        self.tinh_thanh = self.tinh_thanh.replace('tp.hcm', 'thành phố hồ chí minh') if isinstance(
            self.tinh_thanh, str) else None
        self.hop_so = self.hop_so.replace('số', '') if isinstance(self.hop_so, str) else None


@dataclass
class AnyCarBonBanhItem:
    id: Optional[str]
    domain: Optional[str]
    url: Optional[str]
    crawled_date: Optional[datetime.date]
    ten: Optional[str]
    gia_ban: Optional[str]
    nam_san_xuat: Optional[int]
    xuat_xu: Optional[int]
    tinh_trang: Optional[str]
    dong_xe: Optional[str]
    so_km_da_di: Optional[str]
    mau_ngoai_that: Optional[str]
    mau_noi_that: Optional[str]
    so_cua: Optional[str]
    so_cho_ngoi: Optional[int]
    nhien_lieu: Optional[str]
    he_thong_nap_nhien_lieu: Optional[str]
    hop_so: Optional[str]
    dan_dong: Optional[str]
    tieu_thu_nhien_lieu: Optional[str]
    dung_tich_xi_lanh: Optional[str]
    thong_tin_mo_ta: Optional[str]

    def normalize_ten(self, ten: str) -> str:
        splitted_ten = ten.split()
        if splitted_ten:
            if len(splitted_ten) >= 2 and splitted_ten[-2] == 'at':
                self.nam_san_xuat = splitted_ten[-1]
                return ' '.join(splitted_ten[:-2])
            else:
                self.nam_san_xuat = splitted_ten[-1]
                return ' '.join(splitted_ten[:-1])
        return None

    def normalize_gia(self, gia: str) -> int:
        gia_normalized = 0
        gia_splitted = gia.split()
        if len(gia_splitted) == 2 and gia_splitted[1] == 'triệu':
            gia_normalized = float(gia_splitted[0]) * 1e6
        elif len(gia_splitted) == 4 and (gia_splitted[1] == 'tỉ' or gia_splitted[1] == 'tỷ') and gia_splitted[
            3] == 'triệu':
            gia_normalized = float(gia_splitted[0]) * 1e9 + float(gia_splitted[2]) * 1e6

        return gia_normalized

    def __post_init__(self):
        self.crawled_date = str(datetime.timestamp(self.crawled_date))
        self.ten = self.normalize_ten(self.ten)
        self.gia_ban = self.normalize_gia(self.gia_ban)
        self.tinh_trang = 'cũ' if self.tinh_trang == 'xe đã dùng' else 'mới'
        self.xuat_xu = self.xuat_xu.replace('lắp ráp ', '')
        self.hop_so = self.hop_so.replace('số', '')
        self.dan_dong = self.dan_dong.split('-')[0].strip()


@dataclass
class BonBanhItem:
    id: Optional[str]
    domain: Optional[str]
    url: Optional[str]
    crawled_date: Optional[datetime.date]
    ten: Optional[str]
    gia_ban: Optional[str]
    nam_san_xuat: Optional[int]
    xuat_xu: Optional[int]
    tinh_trang: Optional[str]
    dong_xe: Optional[str]
    so_km_da_di: Optional[str]
    mau_ngoai_that: Optional[str]
    mau_noi_that: Optional[str]
    so_cua: Optional[str]
    so_cho_ngoi: Optional[int]
    nhien_lieu: Optional[str]
    he_thong_nap_nhien_lieu: Optional[str]
    hop_so: Optional[str]
    dan_dong: Optional[str]
    tieu_thu_nhien_lieu: Optional[str]
    dung_tich_xi_lanh: Optional[str]
    thong_tin_mo_ta: Optional[str]

    def normalize_ten(self, ten: str) -> str:
        splitted_ten = ten.split()
        if splitted_ten:
            if len(splitted_ten) >= 2 and splitted_ten[-2] == 'at':
                self.nam_san_xuat = splitted_ten[-1]
                return ' '.join(splitted_ten[:-2])
            else:
                self.nam_san_xuat = splitted_ten[-1]
                return ' '.join(splitted_ten[:-1])
        return None

    def normalize_gia(self, gia: str) -> int:
        gia_normalized = 0
        gia_splitted = gia.split()
        if len(gia_splitted) == 2 and gia_splitted[1] == 'triệu':
            gia_normalized = float(gia_splitted[0]) * 1e6
        elif len(gia_splitted) == 4 and (gia_splitted[1] == 'tỉ' or gia_splitted[1] == 'tỷ') and gia_splitted[
            3] == 'triệu':
            gia_normalized = float(gia_splitted[0]) * 1e9 + float(gia_splitted[2]) * 1e6

        return gia_normalized

    def __post_init__(self):
        self.crawled_date = str(datetime.timestamp(self.crawled_date))
        self.ten = self.normalize_ten(self.ten)
        self.gia_ban = self.normalize_gia(self.gia_ban)
        self.tinh_trang = 'cũ' if self.tinh_trang == 'xe đã dùng' else 'mới'
        self.xuat_xu = self.xuat_xu.replace('lắp ráp ', '')
        self.hop_so = self.hop_so.replace('số', '')
        self.tieu_thu_nhien_lieu = ' '.join(self.tieu_thu_nhien_lieu.split('\t')).strip()
        self.dan_dong = self.dan_dong.split('-')[0].strip()


@dataclass
class CarmudiItem:
    id: Optional[str]
    domain: Optional[str]
    url: Optional[str]
    crawled_date: Optional[datetime.date]
    ten: Optional[str]
    gia_ban: Optional[str]
    hang_xe: Optional[str]
    phien_ban: Optional[str]
    tinh_trang_xe: Optional[str]
    tinh_thanh: Optional[str]
    nhien_lieu: Optional[str]
    mau_ngoai_that: Optional[str]
    dong_xe: Optional[str]
    nam_san_xuat: Optional[int]
    hop_so: Optional[str]
    kieu_dang: Optional[str]
    xuat_xu: Optional[int]
    so_cua: Optional[str]
    so_ghe_ngoi: Optional[str]
    dong_co: Optional[float]
    dung_tich_xi_lanh: Optional[float]
    dung_tich_binh_nhien_lieu: Optional[float]
    dan_dong: Optional[str]
    mo_ta: Optional[str]

    def normalize_ten(self, ten: str) -> str:
        splitted_ten = ten.split()
        if splitted_ten[-2] == 'at':
            return ' '.join(splitted_ten[:-2])
        else:
            return ' '.join(splitted_ten[:-1])

    def __post_init__(self):
        self.crawled_date = str(datetime.timestamp(self.crawled_date))
        self.ten = self.ten.lower()
        self.gia_ban = float(self.gia_ban.strip().replace('.', ''))
        self.nam_san_xuat = self.nam_san_xuat.strip() if self.nam_san_xuat else None
        self.xuat_xu = 'trog nước' if self.xuat_xu == 'Lắp ráp' else 'nhập khẩu'


@dataclass
class ChototItem:
    id: Optional[str]
    domain: Optional[str]
    url: Optional[str]
    crawled_date: Optional[datetime.date]
    ten: Optional[str]
    gia_ban: Optional[str]
    hang: Optional[int]
    nam_san_xuat: Optional[int]
    tinh_trang: Optional[str]
    nhien_lieu: Optional[str]
    kieu_dang: Optional[str]
    dong_xe: Optional[str]
    so_km_da_di: Optional[str]
    hop_so: Optional[str]
    xuat_xu: Optional[int]
    so_cho: Optional[str]
    mo_ta: Optional[str]

    def normalize_ten(self, ten: str) -> str:
        ten = ten.lower()
        ten = ' '.join(ten.split('-')[:-1]).strip()
        splitted_ten = ten.split()
        if splitted_ten[-2] == 'at':
            return ' '.join(splitted_ten[:-2])
        else:
            return ' '.join(splitted_ten[:-1])

    def __post_init__(self):
        self.crawled_date = str(datetime.timestamp(self.crawled_date))
        self.gia_ban = float(self.gia_ban.strip().replace('.', ''))
        self.tinh_trang = self.tinh_trang.lower().replace('xe mới', 'mới').replace('đã sử dụng', 'cũ')
        self.xuat_xu = 'trong nước' if self.xuat_xu == 'Việt Nam' else 'nhập khẩu'
