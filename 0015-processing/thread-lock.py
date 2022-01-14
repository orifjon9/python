from threading import Thread, Lock
import time

database_value = 0

def increase(lock):
    global database_value

    with lock:
        __count = database_value
        __count +=1
        time.sleep(0.5)
        database_value = __count

if __name__ == "__main__":
    lock = Lock()
    th1 = Thread(target=increase, args=(lock,))
    th2 = Thread(target=increase, args=(lock,))

    th1.start()
    th2.start()

    th1.join()
    th2.join()
    print("Total is", database_value)
    print("Done")
