'''
生产者消费者
'''
import threading
import time
from queue import Queue

class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 1000:
                for i in range(10):
                    msg = '生产成品' + str(count)
                    queue.put(msg)
                    count += 1
                    print(msg)

                time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global  queue
        while True:
            if queue.qsize() > 100:
                for i in range(100):
                    msg = self.name + '消费了' + queue.get()
                    print(msg)
            time.sleep(1)


if __name__ == '__main__':

    queue = Queue()

    # for i in range(500):
        # queue.put('初始化生产' + str(i))

    for a in range(2):
        p = Producer()
        p.start()

    for b in range(5):
        c = Consumer()
        c.start()