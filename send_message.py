import pika

credentials = pika.PlainCredentials(username='admin', password='mypass')


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials)
)

channel = connection.channel()

channel.queue_declare(queue="test1")

channel.basic_publish(
    exchange='', routing_key="test1", body="Hello Manuel from python"
)

print(" [x] Sent 'Hello World!'")
connection.close()