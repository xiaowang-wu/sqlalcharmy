from threading import Thread, Lock
import time
import random
m = 5
number = 0 
class producer(Thread):
    def run(self):
        global m , number
        while True:
            if number < m:
                if mutex.acquire():
                    number+=1
                    print("我是生产者，临界区资源还有%d"%number)
                    
                    mutex.release()
                    time.sleep(random.random())

                


class consumer(Thread):
    def run(self):
        global m , number
        while True:
            if number >0:
                if mutex.acquire():
                    number -= 1
                    print("我是消费者，临界区资源还有%d"%number)
                    
                    mutex.release()
                    time.sleep(random.random())
                



if __name__ == '__main__':
    mutex = Lock()
    consumer().start()
    producer().start()
