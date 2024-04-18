from celery_task import cel
@cel.task()
def make_order():
    with open(r'/home/root-w/celery/celery_tasks/data/order.txt','a',encoding='utf-8') as f:
        f.write("生成一条订单\n")