import logging, os
from celery import Celery
from celery.utils.log import get_logger

my_tutorial_app = Celery('MyTutorialApp')
my_tutorial_app.config_from_object("app.config.celery_config")

log_level = os.environ.get('LOG_LEVEL', logging.DEBUG)

logger = get_logger(__name__)
logger.setLevel(level=log_level)

@my_tutorial_app.task(name='add', bind=True)
def add(self, x, y):
    logger.info(f"Adding {x} + {y}")
    return x + y
