from celery import Celery
from celery.task.schedules import crontab
from celery.task import task, periodic_task

from .helpers import igokisen_get_json, update_title


app = Celery('tasks', broker='pyamqp://guest@localhost//')


@periodic_task(run_every=crontab(minute=0, hour=4))
def update_igokisen():
    titles = igokisen_get_json()
    for title in titles:
        if title['changeFlag']:
            update_title(title)
    return


# @task
def upload_igokisen_games(title):
    pass


# @periodic_task(run_every=crontab(minute=0, hour=3))
def update_gokifu():
    pass
