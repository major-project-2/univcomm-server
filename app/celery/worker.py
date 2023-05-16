from app.celery.celery_app import celery_app
from celery.schedules import crontab


# run on specific time
# @celery_app.on_after_finalize.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(crontab(hour=10, minute=44),
#                              dummy_task.s(), name='everyday at 10:44 AM')


# run every 10 seconds
@celery_app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0,
                             dummy_task.s(), name='every 10 seconds')


@celery_app.task
def dummy_task():
    print("kya bhai celery")


@celery_app.task
def hello():
    print('kngniognio')
