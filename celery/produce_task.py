from celery_tasks import msg_task, order_task, sms_send_task
from celery_task import cel

def send_task():

    res = order_task.make_order.delay()
    print('order_task',res)
    res = msg_task.send_msg('19513328985','5201')
    print('msg',res)

def get_result(task_id):
    from celery.result import AsyncResult
    a = AsyncResult(id=task_id, app=cel)
    if a.successful():
        print('任务执行成功了')
        result = a.get()  # 异步任务执行的结果
        print(result)
    elif a.failed():
        print('任务失败')
    elif a.status == 'PENDING':
        print('任务等待中被执行')
    elif a.status == 'RETRY':
        print('任务异常后正在重试')
    elif a.status == 'STARTED':
        print('任务已经开始被执行')
def delay_task():
    from datetime import datetime, timedelta
    eta = datetime.now()+timedelta(seconds=5)
    res = sms_send_task.send_sms.apply_async(args=('12345566650', '8888'), eta=eta)
    print(res)

if __name__ == '__main__':
    # send_task()
    delay_task()
    # task_dict={'order_task':'de38381c-767b-498a-ae47-f9f51cf402a7',
    #            'compute_task':'bff48f2c-63ab-48c3-9659-f8efdb961656'}
    # for _,task_id in task_dict.items():
    #     print(get_result(task_id))