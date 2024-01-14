FROM python:3.12-slim

# ensure local python is preferred over distribution python
#ENV PATH /usr/local/bin:$PATH

WORKDIR /code
COPY . .

RUN pip install --no-cache-dir -r /code/requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/code"

# Starting worker using celery module
CMD celery -A app.main_worker worker --loglevel=INFO