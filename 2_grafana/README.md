# Prometheus+Grafana deployment

Port forward:
```
kubectl get po
kubectl port-forward pod/grafana-57b89b4fcf-bxk2h 33000:3000
```