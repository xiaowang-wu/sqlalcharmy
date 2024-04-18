import time
from celery_task import cel
@cel.task()
def send_msg(a,b):
    time.sleep(5)
    print("phone:{},code:{}".format(a,b))
    return "发送成功"