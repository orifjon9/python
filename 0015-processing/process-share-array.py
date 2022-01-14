from multiprocessing import Process, Value, Lock
import time


def add_num(shared_number, lock):
    for i in range(100):
        time.sleep(0.1)
        with lock:
            shared_number.value += 1


if __name__ == "__main__":

    lock = Lock()
    shared_number = Value('i', 0)

    p1 = Process(target=add_num, args=(shared_number, lock))
    p2 = Process(target=add_num, args=(shared_number, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Final value is", shared_number.value)
    print("Done")
