import time

from confluent_kafka import Producer

from constants import kafka_url, kafka_topic_temp
from schema_handler import serialize_temperature

if __name__ == "__main__":
    # Conf for kafka connection
    conf = {'bootstrap.servers': kafka_url,'client.id': 'myproducer'}
    # Create the producer
    producer = Producer(conf)
    while True:
        msg = {"id": 123, "temperature": 11, "timestamp": round(time.time() * 1000)}
        raw_bytes = serialize_temperature(msg)
        print(f'Publishing: {msg}')
        producer.produce(kafka_topic_temp, raw_bytes)
        # Wait 1 seconds and publish again
        time.sleep(1)
