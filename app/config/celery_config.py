# CeleryConfig.py

from kombu import Exchange, Queue

broker_url = 'pyamqp://guest:guest@localhost:5672//'  # Replace with your RabbitMQ connection details

# Set the result backend to RabbitMQ
result_backend = 'rpc://'

# Use JSON as the default serializer
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']

# Define the default queue and exchange
task_default_queue = 'tutorial'
task_default_exchange = 'tutorial'
task_default_routing_key = 'tutorial'


# Define additional queues and exchanges if needed
task_queues = (
    Queue(task_default_queue, Exchange(task_default_exchange), routing_key=task_default_routing_key),
    # Add more queues as needed
)

# Additional Celery settings can be added here
# For example, concurrency settings, task time limits, etc.
# For a complete list of settings, see: https://docs.celeryproject.org/en/stable/configuration.html

# Example concurrency settings:
# worker_concurrency = 4
# worker_prefetch_multiplier = 1

broker_connection_retry = True
broker_connection_retry_on_startup = True
