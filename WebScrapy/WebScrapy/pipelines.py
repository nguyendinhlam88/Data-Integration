from itemadapter import ItemAdapter

import json
import dataclasses


class WebscrapyPipeline:
    def process_item(self, item, spider):
        def delivery_report(err, msg):
            """ Called once for each message produced to indicate delivery result.
                Triggered by poll() or flush(). """
            if err is not None:
                print('Message delivery failed: {}'.format(err))
            else:
                print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

        spider.producer.poll(0)
        spider.producer.produce(spider.name,
                                json.dumps(dataclasses.asdict(item)).encode('utf-8'),
                                callback=delivery_report)
        spider.producer.flush()