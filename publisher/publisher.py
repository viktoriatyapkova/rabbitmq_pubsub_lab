import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')

with open('input.txt', 'r') as file:
    for line in file:
        message = line.strip()
        channel.basic_publish(exchange='logs', routing_key='', body=message)
        print(f"Отправлено: {message}")
        time.sleep(1)

connection.close()
