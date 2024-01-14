# Step1: Start RabbitMq Container - Default user and password: guest
For deamon mode -d
For Interactive mode -it --rm
```
docker run -d --name rabbitmq -p 5672:5672 rabbitmq:latest
```

## Step1: RabbitMq with Management Console instead plain RabbitMq
```
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management
```


## Setp2: Start Celery Worker - Main
```
celery -A app.main_worker worker --loglevel=INFO
```


## Setp3: Publish Message to the worker task
```
python app/publish.py
```


## How to start RabbitMQ in dedicated virtual host
### 1. Start the docker container
```
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management
```
### 2. Go to container inside
```
docker exec -it rabbitmq bash
```
### 3. Add virtual host
```
rabbitmqctl add_vhost tutorial
```
### 4. Update user guest permission to virtual host 
```
rabbitmqctl set_permissions -p tutorial guest ".*" ".*" ".*"
```
### 5. Set broker url - Connect in your backend script segregated queue and exchange
```
amqp://guest@localhost:5672/tutorial
```
### 6. Start celery worker
```
celery -A app.main_worker worker --loglevel=INFO
```

### How to start using docker-compose
## STEP1:
```
docker compose -f docker-compose.yml up --detach --build
```
## STEP2: publish message to RabbitMQ and consumer container will process the message
```
python app/publish.py
```