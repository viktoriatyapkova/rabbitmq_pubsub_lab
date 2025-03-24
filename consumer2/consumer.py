import pika

def callback(ch, method, properties, body):
    message = body.decode()
    print(f"Получено: {message}")
    with open('consumer2_output.txt', 'a') as f:
        f.write(message + '\n')

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='logs', queue=queue_name)

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
print('Consumer2 ждет сообщений...')
channel.start_consuming()
