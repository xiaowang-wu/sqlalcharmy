def run():
    from threading import Thread, Lock
    import time
    class task1(Thread):
        def run(self):
            for i in range(3):
                if lock1.acquire():
                    print('task1')
                time.sleep(0.5)
                lock2.release()
    class task2(Thread):
        def run(self):
            for i in range(3):
                if  lock2.acquire():
                    print("task2")
                time.sleep(0.5)
                lock3.release()
    class task3(Thread):
        def run(self):
            for i in range(3):
                if  lock3.acquire():
                    print("task3")
                time.sleep(0.5)
                lock1.release()
    lock1 = Lock()
    lock2 = Lock()
    lock3 = Lock()
    lock2.acquire()
    lock3.acquire()
    task1().start()
    task2().start()
    task3().start()

