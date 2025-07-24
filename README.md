# Avro-Kafka demo

A demo architecture with Kafka and Zookeeper as the message bus and coordinator and the Avro library for schema management.

### Schemas

Two json files that represent the schemas are available in the `schemas` directory. These are read by the Avro library to serialize/deserialize messages send on Kafka.

### Kafka producer/consumer

Two python files for a producer and a consumer are available in the codebase. 

1. The producer continuously produces random values, serializes the message with the respective schema and publishes it in the message bus.
2. The consumer continuously reads messages from the message bus, deserializes them through the Avro library and the respective schema file and prints them in the console.

### Deployment

The `docker-compose.yml` file contains the stack for **Kafka**, **Zookeeper**, and the **Kafdrop** services. Kafdrop is used as a visualizer for Kafka topics and messages on the fly.

The file `requirements.txt` contains the python libraries needed to run the demo.

The `producer.py` file runs the producer and the `consumer.py` file runs the consumer both in infinite loops.

### Todo tasks

* Schema evolution (removing/adding fields on the schema over different compatibility types)
* Schema registry (incorporate a schema registry to store the schemas and have a better overview instead of simple json files)