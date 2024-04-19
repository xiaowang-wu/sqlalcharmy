import threading, time

class TestThread(threading.Thread):
    def run(self):
        for i in range(3):
            msg = self.name + ":" + str(i)
            print(msg)
            time.sleep(1)

if __name__ == '__main__':
    # t = TestThread()
    # t.start()
    for  i in range(5):
        t = TestThread()
        t.start()