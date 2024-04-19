from  threading import Thread, Lock
import threading
num = 0
import time

def add1():
    global num
    for i in range(10):
        if mutex.acquire():  # 调用acquire（）方法就会上锁
            num += 1
            print("add1: %s-%s"% (i,num))
        mutex.release()
        time.sleep(1)
        


def add2():
    global num
    for i in range(10):
        if mutex.acquire():
            num += 1
            print("add2: %s-%s"% (i,num))
        mutex.release()
        time.sleep(1)


if __name__ == '__main__':
    mutex = Lock()
    t1 = Thread(target=add1)
    t2 = Thread(target=add2)
    t1.start()
    t2.start()
    while True:
        if len(threading.enumerate()) == 1:
            print(num)
            print("---------end----")
            break
