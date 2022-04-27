# Prometheus Node-Exporter deployment

Create deployment
```
kubectl apply -f node-exp-depl.yml
```
Get pods:
```
kubectl get po
```
Forward port to localhost:
```
kubectl port-forward pod/node-exp-77b9bf49bc-wcbvp 39100:9100
```