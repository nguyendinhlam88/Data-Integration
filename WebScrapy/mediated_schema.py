from typing import Optional, List
from dataclasses import dataclass
import datetime

@dataclass
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

    # Tiền xử lý tạm thời ở đây.
    def __post_init__(self):
        pass


    def to_sql_record(self) -> str:
        return f'(\'{self.domain}\', \'{self.crawled_date}\', \'{self.ten}\', {self.gia_ban}, \'{self.xuat_xu}\', \'{self.tinh_trang}\', \'{self.dong_xe}\', \'{self.so_km_da_di}\', \'{self.mau_ngoai_that}\', \'{self.mau_noi_that}\', \'{self.so_cua}\', {self.so_cho_ngoi}, \'{self.nhien_lieu}\', \'{self.he_thong_nap_nhien_lieu}\', \'{self.hop_so}\', \'{self.dan_dong}\', \'{self.tieu_thu_nhien_lieu}\', \'{self.dung_tich_xi_lanh}\')'
