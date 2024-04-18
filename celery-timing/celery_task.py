from celery import Celery

cel = Celery('test',broker="redis://127.0.0.1:6379/1",backend="redis://127.0.0.1:6379/2",include=['smg_task'])

cel.conf.update({'broker_connection_retry_on_startup': True})

cel.conf.timezone='Asia/Shanghai'
cel.conf.enable_utc = False

from datetime import timedelta
from celery.schedules import crontab
cel.conf.beat_schedule={
    'send_msg_every_e_seconds':{
        'task':'smg_task.send',
        'schedule':timedelta(seconds=3),
        #'schedule':crontab(hour=8,day_of_week=1), # 每周一早八点
        'args':('19513328658','4564')
    }
}