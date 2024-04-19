import time, threading
def sing():
    for i in range(3):
        print('sing:',i)
        time.sleep(1)

def dance():
    for i in range(3):
        print('dance:',i)
        time.sleep(2)

t1 = threading.Thread(target=sing)
t2 = threading.Thread(target=dance)

print('--------start--------')
print(t1.name)
t1.start()
t2.start()
print('-----------end----------')
while True:
    length = len(threading.enumerate())
    print('thread numnbers:%s'% length)
    if length <=1:
        break
    time.sleep(1)