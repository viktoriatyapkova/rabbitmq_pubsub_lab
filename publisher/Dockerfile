FROM python:3.10
WORKDIR /app
COPY publisher.py .
COPY input.txt ./input.txt
RUN pip install pika
CMD ["python", "publisher.py"]
