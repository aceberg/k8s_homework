#!/bin/python3

import prometheus_client
import time
from kubernetes import client, config

SERVER_PORT = 9999
UPDATE_PERIOD = 5
PODCOUNT = prometheus_client.Gauge('pods_count','Count pods in cluster')

def count_pods():
  # config.load_kube_config()
  config.load_incluster_config()
  v1 = client.CoreV1Api()
  ret = v1.list_pod_for_all_namespaces(watch=False)
  number = len(ret.items)
  # print("Number of elements in the list: ", number)
  return(number)


if __name__ == '__main__':
  prometheus_client.start_http_server(SERVER_PORT)

  
while True:
  PODCOUNT.set(count_pods())
  time.sleep(UPDATE_PERIOD)