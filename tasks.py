from conf_celery import make_celery
from flask import Flask
from utils import processing_data

app = Flask(__name__)
app.config.update(CELERY_CONFIG={
    'broker_url': 'redis://localhost:6379',
    'result_backend': 'redis://localhost:6379',
})
celery = make_celery(app)


@celery.task()
def task_upload_file(name_file: str):
    processing_data(name_file)
    return True


@celery.task()
def task_id_state(task_id: str):
    state_id = celery.AsyncResult(task_id)
    return state_id
