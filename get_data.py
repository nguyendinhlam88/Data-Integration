import json
import pandas as pd
import sqlalchemy as sa
from json import dump
from sqlalchemy import create_engine
from confluent_kafka import Consumer

c = Consumer({'bootstrap.servers': '127.0.0.1:9092',
              'group.id': 'group_11',
              'auto.offset.reset': 'earliest'})
engine = create_engine('postgresql://root:root@localhost:5005/oto_db')
connection = engine.connect()

list_topic = list(c.list_topics().topics.keys())[:-1]
list_topic.remove('chotot')
# list_topic.remove('anycar_bonbanh')
print(list_topic)
c.subscribe(list_topic)

while True:
    msg = c.poll(1.0)

    if msg is None:
        print("Waiting data ...")
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print(msg.value())
    data_dict = dict(json.loads(msg.value().decode('utf-8')))
    data = pd.DataFrame.from_records([data_dict])
    try:
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

        inspector = sa.inspect(engine)
        if topic not in inspector.get_table_names():
            create_table = pd.io.sql.get_schema(data, name=topic)
            connection.execute(create_table)
        data.to_sql(name=topic, con=engine, if_exists='append', index=False)
        print('Write {} to Postgresql successfully'.format(data_dict['url']))
    except:
        print(f"Error for writing {data_dict['url']} to Postgresql")

c.close()
