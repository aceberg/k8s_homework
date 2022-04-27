FROM ubuntu:20.04

RUN apt update && apt -y install python3-pip && pip3 install prometheus_client kubernetes

COPY pods_count.py .

CMD python3 pods_count.py