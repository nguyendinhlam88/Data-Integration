import json
import os

import pandas as pd
import sqlalchemy as sa
import pickle
from sqlalchemy import create_engine
from confluent_kafka import Consumer

c = Consumer({'bootstrap.servers': '127.0.0.1:9092',
              'group.id': 'group_11',
              'auto.offset.reset': 'earliest'})
engine = create_engine('postgresql://root:root@localhost:5005/oto_db')
connection = engine.connect()

config_mapping = os.getcwd() + '/config_mapping/'

mediated_schema_cols = ["id", "domain", "url", "crawled_date", "ten", "gia_ban", "nam_san_xuat", "xuat_xu",
                        "tinh_trang", "kieu_dang", "so_km_da_di", "mau_ngoai_that",
                        "mau_noi_that", "so_cua", "so_cho_ngoi", "nhien_lieu", "hop_so", "dan_dong",
                        "dung_tich_xi_lanh", "thong_tin_mo_ta"]

while True:
    list_topic = list(c.list_topics().topics.keys())[:-1]
    c.subscribe(list_topic)

    msg = c.poll(1.0)

    if msg is None:
        print("Waiting data ...")
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    try:
        data_dict = dict(json.loads(msg.value()))
        topic = None
        if data_dict['domain'] == 'anycar.bonbanh.com':
            topic = 'anycar_bonbanh'
        elif data_dict['domain'] == 'oto.com.vn':
            topic = 'oto'
        elif data_dict['domain'] == 'www.carmudi.vn':
            topic = 'carmudi'
        elif data_dict['domain'] == 'bonbanh.com':
            topic = 'bonbanh'
        else:
            topic = 'chotot'

        with open(f'{config_mapping}/mediated_schema_{topic}.pkl', 'rb') as file:
            mapping = pickle.load(file)

        data = pd.DataFrame.from_records([], mediated_schema_cols)
        for key, value in mapping.items():
            data[key] = data_dict[value]

        inspector = sa.inspect(engine)
        if 'mediated_schema' not in inspector.get_table_names():
            create_table = pd.io.sql.get_schema(pd.read_csv(os.getcwd() + '/WebScrapy/Crawl_Data/mediated_schema.csv'),
                                                name='mediated_schema')
            connection.execute(create_table)
        data.to_sql(name='mediated_schema', con=engine, if_exists='append', index=False)
        print('Write {} to Postgresql successfully'.format(data_dict['url']))
    except:
        print(f"Error for writing to Postgresql")

c.close()
