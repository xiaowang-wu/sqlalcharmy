from celery_task import cel
import time


@cel.task()
def send(phone,code):
    print('短信发送成功，手机号是：{}验证码是{}'.format(phone,code))
    return '短信发送成功'