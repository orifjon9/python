from multiprocessing import Process
import os
import time

def square_numbers(num:int):
    for i in range(num):
        i*i
        time.sleep(0.1)

if __name__=='__main__':
    processes:list[Process] = []
    num_processes = os.cpu_count()
    print(num_processes)

    # create processes
    for i in range(num_processes):
        p = Process(target=square_numbers, args=(100,))
        processes.append(p)


    # start
    for p in processes:
        p.start()

    # wait
    for p in processes:
        p.join()

    print("Done")
