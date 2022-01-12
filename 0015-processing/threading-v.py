from threading import Thread
import os
import time

def square_numbers(num:int):
    for i in range(num):
        i*i
        time.sleep(0.1)

if __name__=='__main__':
    threads:list[Thread] = []
    num_thread = 10

    # create processes
    for i in range(num_thread):
        th = Thread(target=square_numbers, args=(100,))
        threads.append(th)


    # start
    for th in threads:
        th.start()

    # wait
    for th in threads:
        th.join()

    print("Done")
