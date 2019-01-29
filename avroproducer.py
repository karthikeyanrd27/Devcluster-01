from kafka import SimpleProducer, KafkaClient
import avro.schema
import io, random
from avro.io import DatumWriter
 
# To send messages synchronously
kafka = KafkaClient('ashaplq00003:9192')
producer = SimpleProducer(kafka)
 
# Kafka topic
topic = "testtopic"
 
# Path to user.avsc avro schema
schema_path="/Users/KarthikeyanDurairaj/Desktop/AvroFileschema.txt"
schema = avro.schema.Parse(open(schema_path).read())
 
 
for i in range(10):
    writer = avro.io.DatumWriter(schema)
    bytes_writer = io.BytesIO()
    encoder = avro.io.BinaryEncoder(bytes_writer)
    writer.write({"name": "karthikeyan is great guy always ", "favorite_color": "green iieieei eeieeiei eieie ", "favorite_number": random.randint(0,10)}, encoder)
    raw_bytes = bytes_writer.getvalue()
    producer.send_messages(topic, raw_bytes)
