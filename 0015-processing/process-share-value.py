from multiprocessing import Process, Array, Lock
import time


def add_nums(shared_numbers, lock):
    for i in range(len(shared_numbers)):
        for _ in range(100):
            time.sleep(0.1)
            with lock:
                shared_numbers[i] += 1


if __name__ == "__main__":

    lock = Lock()
    shared_numbers = Array('d', [0.0, 100.0, 200.0])

    print("Staring a processes", shared_numbers[:])

    p1 = Process(target=add_nums, args=(shared_numbers, lock))
    p2 = Process(target=add_nums, args=(shared_numbers, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Final values are", shared_numbers[:])
    print("Done")
