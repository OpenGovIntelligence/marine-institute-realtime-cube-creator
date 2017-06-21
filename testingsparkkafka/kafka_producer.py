from kafka import SimpleProducer, SimpleClient
import avro.schema
import io, random
from avro.io import DatumWriter

# To send messages synchronously
kafka = SimpleClient('localhost:9092')
producer = SimpleProducer(kafka)

# Kafka topic
topic = "new-topic"

# Path to user.avsc avro schema
schema_path = "schema.avsc"
schema = avro.schema.parse(open(schema_path).read())

for i in xrange(10):
    writer = avro.io.DatumWriter(schema)
    bytes_writer = io.BytesIO()
    encoder = avro.io.BinaryEncoder(bytes_writer)
    writer.write({"name": "123",  "favorite_number": random.randint(0, 10), "favorite_color": "green"}, encoder)
    raw_bytes = bytes_writer.getvalue()
    producer.send_messages(topic, raw_bytes)

print "done"
