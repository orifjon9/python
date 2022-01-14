from queue import Queue
from threading import Lock, current_thread, Thread


def worker(q:Queue,lock:Lock):
    while True:
        value = q.get()
        with lock:
            print(f"In {current_thread().name} got '{value}' value")
        q.task_done()

if __name__ == "__main__":
    lock = Lock()
    queue = Queue()

    for _ in range(10):
        th = Thread(target=worker, args=(queue, lock))
        th.daemon = True # stops all thread if the main stops
        th.start()

    for num in range(1, 50):
        queue.put(num)

    queue.join()

    print("Done")