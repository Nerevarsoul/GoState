from celery import Celery


app = Celery('celery_tasks',
             broker='amqp://',
             backend='amqp://',
             include=['celery_tasks.tasks'])


if __name__ == '__main__':
    app.start()
