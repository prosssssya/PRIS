# Работу выполнили: Исмагилова Карина, Шурубова Прасковья  
---
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
##  Ссылка на видеообзор работы: https://drive.google.com/file/d/1pcItkeOUR1YqPM599I9Rq0yX7SFEVStl/view?usp=sharing 
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
---
## Наш дашборд :)
<img width="1009" alt="image" src="https://github.com/user-attachments/assets/cb66ed8e-d1d8-4a85-8644-d1843436effb" />

# Лабораторная работа разработка микросервисной архитектуры с GraphQL 
# Django + JavaScript + HTML
---
## Стек технологий
- Python + Django
- Apollo Server/Gateway 
- PostgreSQL 
- MondoDb
- GraphQL
- JavaScript
- HTML
---
##  Ссылка на видеообзор работы: https://drive.google.com/file/d/13786XVTTbwIokRwFTCGOM3jY8uA3sxDq/view?usp=sharing 
---
##  Шаги по развёртыванию
Во-первых необходимо установить все зависимости из requirements.txt
1. Запускаем все сервисы
```bash
# Из папки services/users
 uvicorn main:app --port 8001
# Из папки services/orders
 uvicorn main:app --port 8002
# Из папки services/products
 uvicorn main:app --port 8003
```
---
2. Затем запускаем gateway.js из директории gateway
```bash
node gateway.js 
```
---
Переходим по необходимым адресам и производим проверку работы
Ниже скрипты для запросов:
```bash
# Создание пользователя  CREATE
mutation {
  createUser(input: {name: "John", email: "john@example.com"}) {
    id
    name
    email
  }
}

# Получение всех пользователей READ
query {
  users {
    id
    name
    email
  }
}

# Обновление пользователя UPDATE
mutation {
  updateUser(id: 1, input: {name: "John Updated", email: "john.updated@example.com"}) {
    id
    name
    email
  }
}

# Удаление пользователя DELETE
mutation {
  deleteUser(id: 2)
}

# Создание продукта CREATE
createProduct(input: {name: "Пылесос", description:  "Лучший пылесос на свете",  price: 34343})
 {
    id
    name
    description
    price
 }
}

# Создание заказа CREATE
mutation {
  createOrder (input: {
    userId: 3,
    productId: 1, 
    quantity: 2
  }) {
    id
    userId
    productId
    quantity
  }
}
```
Аналогичные запросы для обновления и удаления продуктов и заказов, ниже приведены скриншоты с обработкой запросов  
---
![IMAGE 2025-05-17 18:02:58](https://github.com/user-attachments/assets/caf030ed-7298-4af8-b689-fcf61b34157f)
![IMAGE 2025-05-17 18:03:08](https://github.com/user-attachments/assets/96b9f9c4-8719-42ed-b89b-4a2720ce7d5e)
![IMAGE 2025-05-17 18:03:20](https://github.com/user-attachments/assets/4add76c2-0d2e-4dfd-9743-2f09d987d1a1)
![IMAGE 2025-05-17 18:03:29](https://github.com/user-attachments/assets/1a947773-6e0d-4625-ac2b-89c679bc183d)
![IMAGE 2025-05-17 18:03:38](https://github.com/user-attachments/assets/a0b3c421-b9e5-4500-b44d-8a6a3485b9d9)

# Лабораторная работа "Работа с Big Data"
# Flask + ML WebApp для анализа данных
---
## Стек технологий
- Python + Flask
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
---
##  Ссылка на видеообзор работы: 
---
##  Шаги по развёртыванию

```bash
# 1. Клонируем или переходим в папку проекта
cd lab-3

# 2. Создание виртуального окружения
python -m venv venv
venv\Scripts\activate        

# 3. Установка зависимостей
pip install -r requirements.txt

# 4. Запуск Flask-приложения
python app.py
```
---
## Шаги после запуска:
- Загружаем CSV-файлы с числовыми признаками
- Выбираем нужные столбцы X и Y
- Запускаем процесс обучения модели
- Получем  график "Факт vs Прогноз", тепловую карту, рассчитанные метрики MSE и R²
## Результат работы с небольшим набором данных и с 100000 строками:)
![image](https://github.com/user-attachments/assets/6c4285ec-d89c-4eec-be96-40b8626b881c)
![image](https://github.com/user-attachments/assets/abfe8164-a70a-4068-82bf-9eb54443a2c5)
![image](https://github.com/user-attachments/assets/6c510e9b-1892-4d98-8f7a-9f04ac006201)


