import io

import avro
from avro.io import DatumWriter

SCHEMA_PATH_TEMP = "schemas/temperature_v1.avsc"
SCHEMA_TEMP = avro.schema.parse(open(SCHEMA_PATH_TEMP).read())
SCHEMA_PATH_HUMI = "schemas/humidity_v1.avsc"
SCHEMA_HUMI = avro.schema.parse(open(SCHEMA_PATH_HUMI).read())

def serialize_temperature(msg):
    raw_bytes = serialize(msg, SCHEMA_TEMP)
    return raw_bytes

def serialize_humidity(msg):
    raw_bytes = serialize(msg, SCHEMA_HUMI)
    return raw_bytes

def deserialize_temperature(msg):
    item = deserialize(msg, SCHEMA_TEMP)
    return item

def derialize_humidity(msg):
    item = deserialize(msg, SCHEMA_HUMI)
    return item

def serialize(msg,schema):
    writer = DatumWriter(schema)
    bytes_writer = io.BytesIO()
    encoder = avro.io.BinaryEncoder(bytes_writer)
    writer.write(msg, encoder)
    raw_bytes = bytes_writer.getvalue()
    return raw_bytes

def deserialize(msg,schema):
    bytes_reader = io.BytesIO(msg.value())
    decoder = avro.io.BinaryDecoder(bytes_reader)
    reader = avro.io.DatumReader(schema)
    item = reader.read(decoder)
    return item