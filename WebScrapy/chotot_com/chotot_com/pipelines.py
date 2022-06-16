# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import MySQLdb
from itemadapter import ItemAdapter



table = 'oto'
conf = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'database': 'oto-db',
    'raise_on_warnings': True
}

class MySQLPipeLine:
    def __init__(self):
        self.conn = MySQLdb.connect(conf['host'], conf['user'], conf['password'], 
                                    conf['database'], charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(f'INSERT INTO oto (domain, crawled_date, ten, gia_ban, xuat_xu, tinh_trang, dong_xe, so_km_da_di, mau_ngoai_that, mau_noi_that, so_cua, so_cho_ngoi, nhien_lieu, he_thong_nap_nhien_lieu, hop_so, dan_dong, tieu_thu_nhien_lieu, dung_tich_xi_lanh) VALUES{item.to_sql_record()}')        

            self.conn.commit()

            #print(f'INSERT INTO oto (domain, crawled_date, ten, gia_ban, xuat_xu, tinh_trang, dong_xe, so_km_da_di, mau_ngoai_that, mau_noi_that, so_cua, so_cho_ngoi, nhien_lieu, he_thong_nap_nhien_lieu, hop_so, dan_dong, tieu_thu_nhien_lieu, dung_tich_xi_lanh) VALUES{item.to_sql_record()}')

            pass            
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

        return item
