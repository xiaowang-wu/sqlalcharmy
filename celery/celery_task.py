from celery import Celery
# import celery_tasks
cel = Celery('celery_demo',
             broker='redis://127.0.0.1:6379/1',
             backend='redis://127.0.0.1:6379/2',
             # 包含以下两个任务文件，去相应的py文件中找任务，对多个任务做分类
             include=['celery_tasks.msg_task',
                      'celery_tasks.order_task',
                      'celery_tasks.sms_send_task'
                      ])
cel.conf.timezone = 'Asia/Shanghai'
# 是否使用UTC
cel.conf.enable_utc = False
cel.conf.update({'broker_connection_retry_on_startup':True})
