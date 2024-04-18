from celery_task import cel
@cel.task()
def send_sms(phone, code):
    print('短信发送成功，手机号是：%s验证码是%s' % (phone, code))
    return '短信发送成功'