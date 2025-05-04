# Лабораторная работа k8s
# Flask + Kubernetes + Minikube
---
## Стек технологий
- Python + Flask
- Docker
- Kubernetes (Minikube)
- Metrics Server
- Horizontal Pod Autoscaler (HPA)
- Prometheus + Grafana

---

##  Шаги по развёртыванию

```bash
# 1. Запуск Minikube
minikube start

# 2. Подключение Docker к Minikube
eval $(minikube docker-env)

# 3. Сборка Docker-образа
docker build -t my-k8s-app .

# 4. Применение манифестов Kubernetes
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# 5. Проверка статуса
kubectl get pods
minikube service my-app-service

# Установка Metrics Server
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# Настройка Horizontal Pod Autoscaler (HPA)
kubectl autoscale deployment my-app --cpu-percent=50 --min=2 --max=5

# Установка Prometheus и Grafana через Helm
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/kube-prometheus-stack

# Подключение к Grafana
kubectl port-forward svc/prometheus-grafana 3000:80
```
