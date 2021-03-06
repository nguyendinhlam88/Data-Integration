from typing import Optional, List
from dataclasses import dataclass
import datetime

@dataclass
class MediatedOtoItem:
    id: Optional[str]
    domain: Optional[str]
    url: Optional[str]
    crawled_date: Optional[datetime.date]
    ten: Optional[str]
    gia_ban: Optional[int]
    nam_san_xuat: Optional[int]
    xuat_xu: Optional[str]
    tinh_trang: Optional[str]
    kieu_dang: Optional[str]
    so_km_da_di: Optional[str]
    mau_ngoai_that: Optional[str]
    mau_noi_that: Optional[str]
    so_cua: Optional[str]
    so_cho_ngoi: Optional[int]
    nhien_lieu: Optional[str]
    hop_so: Optional[str]
    dan_dong: Optional[str]
    dung_tich_xi_lanh: Optional[str]
    thong_tin_mo_ta: Optional[str]

    # Tiền xử lý tạm thời ở đây.
    def __post_init__(self):
        pass
