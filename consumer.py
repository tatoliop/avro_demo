import sys

from confluent_kafka import Consumer, KafkaError, KafkaException

from constants import kafka_url, kafka_topic_temp
from schema_handler import deserialize_temperature

if __name__ == "__main__":
    # Conf for kafka connection
    conf = {'bootstrap.servers': kafka_url,'group.id': 'mypconsumer'}
    # Create the producer
    consumer = Consumer(conf)
    topics = [kafka_topic_temp]
    try:
        consumer.subscribe(topics)
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                item = deserialize_temperature(msg)
                print(f'Subscribed to topic <{msg.topic()}> and consumed msg: <{item}>')
    finally:
        consumer.close()