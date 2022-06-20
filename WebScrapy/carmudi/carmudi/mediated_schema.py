from typing import Optional, List
#from dataclasses import dataclass
import datetime

from pymysql import NULL

#@dataclass
class MediatedOtoItem:
    id: Optional[str]
    domain: Optional[str]
    crawled_date: Optional[datetime.date]
    ten: Optional[str]
    gia_ban: Optional[int]
    xuat_xu: Optional[str]
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

    def __init__(self) -> None:
        self.domain = NULL
        self.crawled_date = datetime.datetime.utcnow()
        self.ten = NULL
        self.gia_ban = NULL
        self.xuat_xu = NULL
        self.tinh_trang = NULL
        self.dong_xe = NULL
        self.so_km_da_di = NULL
        self.mau_ngoai_that = NULL
        self.mau_noi_that = NULL
        self.so_cua = NULL
        self.so_cho_ngoi = NULL
        self.nhien_lieu = NULL
        self.he_thong_nap_nhien_lieu = NULL
        self.hop_so = NULL
        self.dan_dong = NULL
        self.tieu_thu_nhien_lieu = NULL
        self.dung_tich_xi_lanh = NULL

        pass

    # Tiền xử lý tạm thời ở đây.
    def __post_init__(self):
        pass


    def to_sql_record(self) -> str:
        return f'(\'{self.domain}\', \'{self.crawled_date}\', \'{self.ten}\', \'{self.gia_ban}\', \'{self.xuat_xu}\', \'{self.tinh_trang}\', \'{self.dong_xe}\', \'{self.so_km_da_di}\', \'{self.mau_ngoai_that}\', \'{self.mau_noi_that}\', \'{self.so_cua}\', \'{self.so_cho_ngoi}\', \'{self.nhien_lieu}\', \'{self.he_thong_nap_nhien_lieu}\', \'{self.hop_so}\', \'{self.dan_dong}\', \'{self.tieu_thu_nhien_lieu}\', \'{self.dung_tich_xi_lanh}\')'
